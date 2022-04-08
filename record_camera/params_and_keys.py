"""
File for storing parameters and keys
"""
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
      "deg":None
   }
WEATHER_ERROR_CLOUD = {"all":None}


WEATHER_API_KEY = ''#api key for the weather api (don't save)
TRAFFIC_API_KEY = ''#api key for the traffic api (don't save)


CAR_NAMES = ['Car', 'Taxi', 'Land vehicle', 'Van', 'Truck', 'Vehicle', 'Bus', 'Motorcycle', 'Ambulance']
THRESHOLDS = [0.9,0.7,0.5,0.3,0.1]

def create_weather_link(LAT,LONG,WEATHER_API_KEY):
      return f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LONG}&appid={WEATHER_API_KEY}&units=metric"

def create_incidents_link(TRAFFIC_API_KEY,box_left,box_up,box_right,box_down):
      return f"http://www.mapquestapi.com/traffic/v2/incidents?key={TRAFFIC_API_KEY}&boundingBox={box_left},{box_up},{box_right},{box_down}&filters=construction,incidents,event,accident"
