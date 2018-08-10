
# Introduction
This tool allows to test automatically the EIDA-FEDERATOR and to compare its results to a node.The code is adapted from WS-RESIF code’s

# Requirements
* Python 3
* requests==2.19.1 To make http calls
* colorama==0.3.9  for printing colored terminal text

# Architecture
* WSEIDAtest:  general script to run all tests
* TESTS_dataselect.py : the list of tests for station query
* TESTS_station.py : the list of tests for station query
* config.py :  Contains login and password to access restricted-data
* utils: global varibales

# Installation
* pip3 install -r requirements.text
* Pour définir  Edit files "TESTS_dataselect.py" and "TESTS_station.py"to define  tests.

# Fonctionnement

### Fonctionnement general

There are two types of tests dataslect and station. You have to define the queries to test in files : ..and ...

to choose the test’s type select options --station and --dataselect

By default, the script executes queries test in eida-FEDERATOR. It is possible to choose other  nodes with the option –nodes. With this option is selected, a comparison is realized on results in text format between the  node(s) and the federator.

The tests on federator can be deactivated with –noeida but in this case, a node is to be chosen. 

to execute a specific test, indicate its id with --id contains option.



### Configuration des fichiers tests 

  A variable TESTS  is declared in the files TESTS_dataselect et TESTS_station as below: 


    TESTS = [

    {

     'id':'a description of the test, It is used by option --contains'.

     'get': ' The query to test without the domain of node. It will be added automatically.',
     
     'test': ' Can contains IN** or ==**. It is used to compare results with text format. '
    }

    ]

** The results comparison is made only on format text results, ‘IN’ verify if the result of node X is in federator results ‘==’ compare if the results are the same

Some examples are availibale in TESTS_dataselect.py et TESTS_station.py.

# Utilisation 
    usage: WSEIDAtest.py [-h] [--dump] [--dataselect] [--station] [--noeida]

                     [--nodes STR] [--idcontains STR]
                     

    optional arguments:
      -h, --help        show this help message and exit

      --dump            dump HTTP response to disk

      --size            Calculate the size


      --dataselect      dataselect tests

      --station         station tests

      --noeida          no tests on EIDA-Federator

      --nodes STR       Nodes or 'ALL'

      --idcontains STR  only run tests with id containing <STR> string


# OUTPUT

The output contains : The status code, The duration of the  execution, a size of results(with --size ) and results of the comparison ( with --nodes)



# Examples


WSEIDAtest.py --nodes RESIF

  Execute all tests (dataselect and station) on eida-federator and RESIF.

WSEIDAtest --dataselact --noeida --nodes RESIF,GFZ --dump

  Execute all tests dataselect on RESIF and GFZ but  not on eida-federator with  downloading the results on disk.


    ./WSEIDAtest.py --idcontains S03 --nodes ALL --size
    Running test ....... S03 get stations of 4C network 
      |-----EIDA: 
      | Query:  http://federator-testing.ethz.ch/fdsnws/station/1/query?network=4C&format=text ...
      | Status code : 200
      | Request duration time : 0.5
      | Getting results to make comparison  ...
      | Response size = 0.0013 Mb 
      |-----RESIF: 
      | Query:  http://ws.resif.fr/fdsnws/station/1/query?network=4C&format=text ...
      | Status code : 200
      | Request duration time : 0.06999999936670065
      | Getting results to make comparison  ...
      | Response size = 0.0011 Mb 
      | Result RESIF IN Result EIDA 
      |-----GFZ: 
      | Query:  http://geofon.gfz-potsdam.de/fdsnws/station/1/query?network=4C&format=text ...
      | Status code : 200
      | Request duration time : 0.14000000059604645
      | Getting results to make comparison  ...
      | Response size = 0.0033 Mb 
      | Result GFZ  NOT IN Result EIDA 
      |-----INGV: 
      | Query:  http://webservices.ingv.it/fdsnws/station/1/query?network=4C&format=text ...
      | Status code : 200
      | Request duration time : 0.1699999999254942
      | Getting results to make comparison  ...
      | Response size = 0.0016 Mb 
      | Result INGV  NOT IN Result EIDA 
      |-----ODC: 
      | Query:  http://www.orfeus-eu.org/fdsnws/station/1/query?network=4C&format=text ...
      | Status code : 204
      | Request duration time : 0.2099999999627471
      | Comparaison  not possible if code status is  different to 200
      |-----ETHZ: 
      | Query:  http://eida.ethz.ch/fdsnws/station/1/query?network=4C&format=text ...
      | Status code : 204
      | Request duration time : 0.049999999813735485
      | Comparaison  not possible if code status is  different to 200
      |-----BGR: 
      | Query:  http://eida.bgr.de/fdsnws/station/1/query?network=4C&format=text ...
      | Status code : 204
      | Request duration time : 2.6299999998882413
      | Comparaison  not possible if code status is  different to 200
      |-----KOERI: 
      | Query:  http://eida-service.koeri.boun.edu.tr/fdsnws/station/1/query?network=4C&format=text ...
      | Status code : 204
      | Request duration time : 0.26000000070780516
      | Comparaison  not possible if code status is  different to 200
      |-----LMU: 
      | Query:  http://erde.geophysik.uni-muenchen.de/fdsnws/station/1/query?network=4C&format=text ...
      | Status code : 204
      | Request duration time : 0.08999999985098839
      | Comparaison  not possible if code status is  different to 200
      |-----NOA: 
      | Query:  http://eida.gein.noa.gr/fdsnws/station/1/query?network=4C&format=text ...
      | Status code : 204
      | Request duration time : 0.1600000001490116
      | Comparaison  not possible if code status is  different to 200
      |-----NIEP: 
      | Query:  http://eida-sc3.infp.ro/fdsnws/station/1/query?network=4C&format=text ...
      | Status code : 204
      | Request duration time : 0.23999999929219484
      | Comparaison  not possible if code status is  different to 200






