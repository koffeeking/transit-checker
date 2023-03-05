'''utils for printing the next g train time'''
from datetime import datetime
import re
import requests
from google.transit import gtfs_realtime_pb2


def get_next_g_train(direction: str):
    # determine direction ID based on input
    direction_id = 0
    if re.fullmatch(pattern=r'[Cc][Hh][Uu][Rr][Cc][Hh]', string=direction):
        direction_id = "0"
    elif re.fullmatch(pattern=r'[Qq][Uu][Ee][Ee][Nn][Ss]', string=direction):
        direction_id = "1"

    # Set up the API endpoint and parameters
    url = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-g"
    params = {
        "key": "Gb8N3T90sX2Nc6h3DBZhT8ixHwlUAjpT59tS9HO3",
        "feed_id": "31",
        "station_id": "G26S",
        "direction_id": direction_id,
        "time": datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    }
    headers = {
        "x-api-key": "Gb8N3T90sX2Nc6h3DBZhT8ixHwlUAjpT59tS9HO3",
        "Content-Type": "application/json"
    }

    # Make the API request and parse the responsed
    response = requests.get(url, params=params, headers=headers)
    feed = gtfs_realtime_pb2.TripUpdate.StopTimeUpdate()
    feed.ParseFromString(response.content)

    # with open('test_file.json','w+') as test_file:
    #     test_file.write(str(feed.entity))

    print(feed)

    #         print(entity.trip_update)

    # next_arrival = data["data"][0]["attributes"]["arrival_time"]

    # # Return the time of the next G train's arrival
    # return datetime.strptime(next_arrival, "%Y-%m-%dT%H:%M:%S%z").strftime("%I:%M %p")
