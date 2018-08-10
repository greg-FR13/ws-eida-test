""" Globals Varibles"""

NODES = ["RESIF", "GFZ", "INGV", "ODC", "ETHZ", "BGR", "KOERI", "LMU", "NOA", "NIEP"]

URLS = {
    "EIDA": "http://federator-testing.ethz.ch",
    "RESIF": "http://ws.resif.fr",
    "GFZ": "http://geofon.gfz-potsdam.de",
    "INGV": "http://webservices.ingv.it",
    "ODC": "http://www.orfeus-eu.org",
    "ETHZ": "http://eida.ethz.ch",
    "BGR": "http://eida.bgr.de",
    "NIEP": "http://eida-sc3.infp.ro",
    "KOERI": "http://eida-service.koeri.boun.edu.tr",
    "LMU": "http://erde.geophysik.uni-muenchen.de",
    "NOA": "http://eida.gein.noa.gr",
}


def validate_node(nodes):

    for node in nodes:
        if node not in NODES:
            return False, node
    return True, None


ERROR_NODE = "The Node {} is not recognized.\
You can add  your node and the URL \
to access to your webservice FDSN \
in file utils.py in liste URLS."
