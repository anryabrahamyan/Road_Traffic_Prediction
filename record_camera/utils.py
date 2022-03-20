"""
File for data recording utilities
"""
import os
from typing import List
import requests
import cv2
import matplotlib.pyplot as plt 
from params_and_keys import *


def record_and_store():
    """Records and stores the frames of the video
    """
    pass


### API part ##################################################
def extract_weather_info(weather_api_response):
    """Extract info from the weather API response
    """
    weather_part= weather_api_response.get("weather", WEATHER_ERROR_WEATHER)[0]
    weather_main, weather_desc = weather_part["main"], weather_part["description"]
    
    temp_data =weather_api_response.get("main",WEATHER_ERROR_TEMP )
    temp,feels_like,temp_min,temp_max,pressure,humidity = temp_data.values()

    visibility = weather_api_response.get("visibility",WEATHER_ERROR_VISIBILITY )
    
    wind_info = weather_api_response.get("wind",WEATHER_ERROR_WIND )
    # print(wind_info)
    wind_speed,wind_angle  = wind_info.values()
    
    cloud_info = weather_api_response.get("clouds",WEATHER_ERROR_CLOUD )
    clouds = cloud_info["all"]
    
    
    
    total_info = [weather_main, weather_desc,temp,feels_like,temp_min,temp_max,
                  pressure,humidity,visibility,wind_speed,wind_angle,clouds]
    
    
    return total_info

def extract_traffic_info(traffic_api_response):
    """Extract info from the traffic API response
    """
    #TODO same for rest of accident types
    incidents = traffic_api_response.get("incidents",None)
    if incidents:
        maximum_severity = max([incident.get("severity",0) for incident in incidents])
        total_impacting = sum([incident.get("impacting",0) for incident in incidents])
        total_delays_free_flow = sum([incident.get("delayFromFreeFlow",0) for incident in incidents])
        total_delays_typical = sum([incident.get("delayFromTypical",0) for incident in incidents])
    else:
        return [None,None,None,None]
    
    return [maximum_severity,total_impacting,total_delays_free_flow,total_delays_typical]
        
def call_apis(LAT = LAT_TIMES,LONG = LONG_TIMES,box_left = LEFT_TIMES,
             box_up = UP_TIMES, box_right =RIGHT_TIMES,box_down = DOWN_TIMES) ->List[str]:
    """Call the extra data apis
    """
    weather_call = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LONG}&appid={WEATHER_API_KEY}&units=metric"
    
    traffic_call = f"http://www.mapquestapi.com/traffic/v2/incidents?key={TRAFFIC_API_KEY}&boundingBox={box_left},{box_up},{box_right},{box_down}&filters=construction,incidents,event,accident"
    
    weather_info = requests.get(weather_call).json()
    traffic_info = requests.get(traffic_call).json()

    weather_info = extract_weather_info(weather_info)
    traffic_info = extract_traffic_info(traffic_info)
    
    all_api_responses = weather_info+traffic_info
    all_api_responses = [str(column) for column in all_api_responses]
    return all_api_responses


#################################################################

def model_predict():
    """Predictions on the stores frames
    """
    pass

if __name__ == "__main__":
    print(call_apis())