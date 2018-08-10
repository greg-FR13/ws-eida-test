
""" You must create TEST_dataselect.py and TEST_station.py"""

TESTS = [
    {
        "id": " S01 ",
        "get": "fdsnws/station/1/query?network=Z3&level=network&format=text&starttime=2015-01-01",
        "statuscode": "200",
        "test": "in",
    },
    {
        "id": " S02 -  ",
        "get": "fdsnws/station/1/query?network=FR&format=text&starttime=2015-01-01",
        "statuscode": "200",
        "test": "==",
    },
    {
        "id": " S03 get stations of 4C network ",
        "get": "fdsnws/station/1/query?network=4C&format=text&endtime=2012-12-31&starttime=2011-01-01",
        "statuscode": "200",
        "test": "in",
    },
    {
        "id": " S04 get all networks ",
        "get": "fdsnws/station/1/query?level=network&format=text",
        "statuscode": "200",
        "test": "in", 
        }
]
