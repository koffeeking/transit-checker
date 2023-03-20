"""utils for printing the next g train time"""
from datetime import datetime
import re
import requests
from google.transit import gtfs_realtime_pb2
from pytz import timezone


def get_next_g_train():
    """returns a list of the next G trains departing from Bedford-Nostrand"""

    # Set up the API endpoint and parameters
    url = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-g"
    headers = {
        "x-api-key": "Gb8N3T90sX2Nc6h3DBZhT8ixHwlUAjpT59tS9HO3",
        "Content-Type": "application/json",
    }

    # Make the API request and parse the responsed
    response = requests.get(
        url,
        headers=headers,
    )
    feed = gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(response.content)

    arrivals = {"Queens": [], "Church": []}

    # ------Queens------
    for entity in feed.entity:
        for update in entity.trip_update.stop_time_update:
            # north-bound ID for the stop
            if update.stop_id == "G26N":
                utc_time = datetime.fromtimestamp(update.arrival.time)
                ny_time = utc_time.astimezone(timezone("US/Eastern")).strftime("%H:%M")
                time_til = int((utc_time - datetime.utcnow()).total_seconds() / 60)
                arrivals["Queens"].append(time_til)
    # ------Church------
    for entity in feed.entity:
        for update in entity.trip_update.stop_time_update:
            # south-bound ID for the stop
            if update.stop_id == "G26S":
                utc_time = datetime.fromtimestamp(update.arrival.time)
                ny_time = utc_time.astimezone(timezone("US/Eastern")).strftime("%H:%M")
                time_til = int((utc_time - datetime.utcnow()).total_seconds() / 60)
                arrivals["Church"].append(time_til)

    # sort the arrivals by time
    for direction in arrivals:
        arrivals[direction].sort()

    print(str(arrivals) + "                 ", end="\r")
