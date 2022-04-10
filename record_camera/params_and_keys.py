"""
File for storing parameters and keys
"""
import os
from os.path import dirname
os.environ['TFHUB_DOWNLOAD_PROGRESS'] = "1"
os.environ['TFHUB_CACHE_DIR'] = 'tf_cache'
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

WAIT_TIME = 300
LONG_TIMES = -73.985130
LAT_TIMES = 40.758896
LEFT_TIMES,UP_TIMES,RIGHT_TIMES,DOWN_TIMES = 40.74,-73.8,40.77,-74.1
LINK = "https://www.youtube.com/watch?v=AdUw5RdyZxI"

WEATHER_ERROR_WEATHER = [{"main":None,"description":None}]
WEATHER_ERROR_TEMP = {"temp":None,
      "feels_like":None,
      "temp_min":None,
      "temp_max":None,
      "pressure":None,
      "humidity":None}
WEATHER_ERROR_VISIBILITY = None
WEATHER_ERROR_WIND = {
      "speed":None,
      "deg":None,
      "gust":None
   }
WEATHER_ERROR_CLOUD = {"all":None}
FRAME_PATH = os.path.join(dirname(dirname(__file__)),"dataset","frame.jpg")

WEATHER_API_KEY = ''#api key for the weather api (don't save)
TRAFFIC_API_KEY = ''#api key for the traffic api (don't save)


CAR_NAMES = ['Car', 'Taxi', 'Land vehicle', 'Van', 'Truck', 'Vehicle', 'Bus', 'Motorcycle', 'Ambulance']
THRESHOLDS = [0.9,0.7,0.5,0.3,0.1]

COLUMN_NAMES = ['datetime',"weather_main", "weather_desc", "temp", "feels_like", "temp_min", "temp_max",
                  "pressure", "humidity", "visibility", "wind_speed", "wind_angle", "clouds","maximum_severity", "total_impacting", "total_delays_free_flow", "total_delays_typical",'Car_0.9', 'Car_0.7', 'Car_0.5', 'Car_0.3', 'Car_0.1', 'Taxi_0.9', 'Taxi_0.7', 'Taxi_0.5', 'Taxi_0.3', 'Taxi_0.1', 'Land vehicle_0.9', 'Land vehicle_0.7', 'Land vehicle_0.5', 'Land vehicle_0.3', 'Land vehicle_0.1', 'Van_0.9', 'Van_0.7', 'Van_0.5', 'Van_0.3', 'Van_0.1', 'Truck_0.9', 'Truck_0.7', 'Truck_0.5', 'Truck_0.3', 'Truck_0.1', 'Vehicle_0.9', 'Vehicle_0.7', 'Vehicle_0.5', 'Vehicle_0.3', 'Vehicle_0.1', 'Bus_0.9', 'Bus_0.7', 'Bus_0.5', 'Bus_0.3', 'Bus_0.1', 'Motorcycle_0.9', 'Motorcycle_0.7', 'Motorcycle_0.5', 'Motorcycle_0.3', 'Motorcycle_0.1', 'Ambulance_0.9', 'Ambulance_0.7', 'Ambulance_0.5', 'Ambulance_0.3', 'Ambulance_0.1']

def create_weather_link(LAT,LONG,WEATHER_API_KEY):
      return f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LONG}&appid={WEATHER_API_KEY}&units=metric"

def create_incidents_link(TRAFFIC_API_KEY,box_left,box_up,box_right,box_down):
      return f"http://www.mapquestapi.com/traffic/v2/incidents?key={TRAFFIC_API_KEY}&boundingBox={box_left},{box_up},{box_right},{box_down}&filters=construction,incidents,event,accident"
