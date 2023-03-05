'''print the next g train'''
from utils import get_next_g_train

get_next_g_train(direction='Church')

# from google.transit import gtfs_realtime_pb2
# import urllib3

# http = urllib3.PoolManager()
# feed = gtfs_realtime_pb2.FeedMessage()
# response = http.request('GET', r"https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-g")
# feed.ParseFromString(response.read())

# print(feed.entity)
# for entity in feed.entity:
#     if entity.HasField('trip_update'):
#         print(entity.trip_update)
