#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
  A basic test suite for EIDA NG Mediator/Federator webservices
Tests cases should be filled in TESTS_dataselect.py and TESTS_station.py
"""

from utils import *

try :
    from TESTS_station import TESTS as station_tests
    from TESTS_dataselect import TESTS as dataselect_tests
except Exception as e:
    print("TESTS_station.py and TESTS_dataselect.py must be created ")
    exit(-1)

import argparse
import requests
import os
import logging
from colorama import Fore, Style

#  To print colored text 
CYAN_COLOR = lambda x: f"{Fore.CYAN}{x}{Style.RESET_ALL}"
YELLOW_COLOR = lambda x: f"{Fore.YELLOW}{x}{Style.RESET_ALL}"
RED_COLOR = lambda x: f"{Fore.RED}{x}{Style.RESET_ALL}"
GREEN_COLOR = lambda x: f"{Fore.GREEN}{x}{Style.RESET_ALL}"
BLUE_COLOR = lambda x: f"{Fore.BLUE}{x}{Style.RESET_ALL}"


def hundler_request(node, test, dumpresponse, count_size, nodes,FormatText=False):
    """
      Execute "test" on "node" 

    """
    logging.info(f"\t|-----{node}: ")
    starttime = os.times()[4]
    if 'get' in test:
        query = "/".join([URLS[node], test["get"]])
        logging.info(f"\t|\tQuery: {Fore.BLUE} {query} ...{Style.RESET_ALL}")
        response = requests.get(query, auth=None, stream=True)
    elif 'post' in test :
        query = "/".join([URLS[node],"fdsnws/dataselect/1/query"])
        f = open ( test['post'], 'r' )
        logging.info ( "\t|\tPOSTing %s" % test['post'] )
        response = requests.post (query, data=f.read(),  stream = True )
        f.close() 
    else:
        logging.info('no get an no post in  TESTS files')
        exit(-1)


    duration = os.times()[4] - starttime
    logging.info(f"\t|\tStatus code : {response.status_code}")
    logging.info(f"\t|\tRequest duration time : {duration}")

    # get result if format is text to compare it 
    result = None
    size = 0.0
    if response.status_code == 200:
        if nodes and FormatText : 
            logging.info(f"\t|\tGetting results to make comparison  ...")
            result = response.text

        if dumpresponse:
            filename = f'{"".join([x if x.isalnum() else "_" for x in test["id"]])}.{node}.dump'
            dumpfile = open(filename, "wb")
            logging.info(f"\t|\tDumping response to {filename} ...")
            count_size = True

        if count_size or dumpresponse :  
            for chunk in response.iter_content(chunk_size=2 ** 18):
                if dumpresponse:
                    dumpfile.write(chunk)
                size = size + len(chunk)
        if dumpresponse:
            dumpfile.close()
        if count_size:
            size = float(size / 1024 ** 2)
            logging.info("\t|\tResponse size = %.4f Mb " % size)

    elif dumpresponse:
        logging.info(
            YELLOW_COLOR(
                f"\t|\tDumping not possible for {response.status_code} request..."
            )
        )

    return result, response.status_code


def compare_result(node, test, node_result, federator_result):
    """ Compare FEDERATOR  result's and NODE(X) result's"""
    if test == "in":

        if all(row in federator_result for row in node_result):
            logging.info(f"\t|\tResult {node} {GREEN_COLOR('IN') } Result EIDA ")
        else:
            logging.info(f"\t|\tResult {node}  {RED_COLOR('NOT IN') } Result EIDA ")
    else:

        if federator_result == node_result:
            logging.info(f"\t|\tResult {node}  {GREEN_COLOR('==') } Result EIDA ")
        else:
            logging.info(f"\t|\tResult {node} {RED_COLOR('!=') }  Result EIDA ")


def isFormatText(url):
    
    occurence = url.find("format=text")
    if occurence > 0:
        return True

    return False


def run(TESTS, dumpresponse, count_size, nodes):

    for test in TESTS:
        federator_result_sorted = False
        if args.idcontains:
            if args.idcontains not in test["id"]:
                continue
        logging.info(CYAN_COLOR(f"Running test .......{test['id']}"))
        federator_status_code = None
        if 'get' in test :
            FormatText = isFormatText(test["get"])
        else:
            FormatText = isFormatText(test["post"])

        if not noeida:
            # test federator
            federator_result, federator_status_code = hundler_request(
                "EIDA", test,  dumpresponse, count_size, nodes, FormatText
            )
        # test others nodes, if --nodes selected
        if nodes is not None:

            # tests author nodes
            for node in nodes:

                node_result, node_status_code = hundler_request(node, test, dumpresponse, count_size,nodes, FormatText)

                if node_status_code == 200 and federator_status_code == 200:

                    if FormatText:
                        if not federator_result_sorted:
                            federator_result.split("\n").sort()
                            federator_result_sorted = True
                        node_result.split("\n").sort()
                        compare_result(node, test["test"], node_result, federator_result)
                    else:
                        logging.info(
                            f'\t|\t{YELLOW_COLOR("Only a TEXT format comparison is possible" )}'
                        )
                else:
                    logging.info(
                        f'\t|\t{YELLOW_COLOR("Comparaison  not possible if code status is  different to 200")}'
                    )


if __name__ == "__main__":

    # change level of requests module logging
    logging.getLogger("requests").setLevel(logging.CRITICAL)

    # Configure the logging
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dump", help="dump HTTP response to disk", action="store_true"
    )
    parser.add_argument(
        "--size", help=" Calculate the size ", action="store_true"
    )
    parser.add_argument("--dataselect", help=" dataselect tests", action="store_true")

    parser.add_argument("--station", help=" station tests", action="store_true")
    parser.add_argument(
        "--noeida", help=" no tests on EIDA-Federator ", action="store_true"
    )

    parser.add_argument("--nodes", help="Nodes or 'ALL'", metavar="STR")

    parser.add_argument(
        "--idcontains",
        help="only run tests with id containing <STR> string",
        metavar="STR",
    )

    # get input arguments 
    args = parser.parse_args()
    dumpresponse = args.dump
    dataselect = args.dataselect
    station = args.station
    noeida = args.noeida
    count_size = args.size

    if not dataselect and not station:
        TESTS = dataselect_tests + station_tests
    else:
        TESTS = dataselect_tests if dataselect else []
        TESTS += station_tests if station else []

    nodes = None
    nodes_args = args.nodes
    if nodes_args:
        if nodes_args == "ALL":
            nodes = NODES
        else:
            nodes = args.nodes.split(",")
            valid, node = validate_node(nodes)
            if not valid:
                logging.info(ERROR_NODE.format(node))
                exit(-1)

    if nodes or not noeida:
        run(TESTS, dumpresponse, count_size,nodes)
    else:
        print(" No node selected to test")