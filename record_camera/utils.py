"""
File for data recording utilities
"""
import sys
from typing import List
import requests
import tensorflow_hub as hub
from params_and_keys import *

sys.path.append('predictor/')
from detect_cars import model_predict

module_handle = "https://tfhub.dev/google/faster_rcnn/openimages_v4/inception_resnet_v2/1"
detector = hub.load(module_handle).signatures['default']


def record_and_store(link: str) -> None:
    """Records and stores the frames of the video
    """
    pass


### API part ##################################################
def extract_weather_info(weather_api_response: dict[str, float]) -> list[str]:
    """Extract info from the weather API response
    """
    weather_part = weather_api_response.get("weather", WEATHER_ERROR_WEATHER)[0]
    weather_main, weather_desc = weather_part["main"], weather_part["description"]

    temp_data = weather_api_response.get("main", WEATHER_ERROR_TEMP)
    temp, feels_like, temp_min, temp_max, pressure, humidity = temp_data.values()

    visibility = weather_api_response.get("visibility", WEATHER_ERROR_VISIBILITY)

    wind_info = weather_api_response.get("wind", WEATHER_ERROR_WIND)
    # print(wind_info)
    wind_speed, wind_angle = wind_info.values()

    cloud_info = weather_api_response.get("clouds", WEATHER_ERROR_CLOUD)
    clouds = cloud_info["all"]

    total_info = [weather_main, weather_desc, temp, feels_like, temp_min, temp_max,
                  pressure, humidity, visibility, wind_speed, wind_angle, clouds]

    return total_info


def extract_traffic_info(traffic_api_response: dict[str, float]) -> list[str]:
    """Extract info from the traffic API response
    """
    # TODO same for rest of accident types
    incidents = traffic_api_response.get("incidents", None)
    if incidents:
        maximum_severity = max([incident.get("severity", 0) for incident in incidents])
        total_impacting = sum([incident.get("impacting", 0) for incident in incidents])
        total_delays_free_flow = sum([incident.get("delayFromFreeFlow", 0) for incident in incidents])
        total_delays_typical = sum([incident.get("delayFromTypical", 0) for incident in incidents])
    else:
        return [None, None, None, None]

    return [maximum_severity, total_impacting, total_delays_free_flow, total_delays_typical]


def call_apis(LAT=LAT_TIMES, LONG=LONG_TIMES, box_left=LEFT_TIMES,
              box_up=UP_TIMES, box_right=RIGHT_TIMES, box_down=DOWN_TIMES) -> List[str]:
    """Call the extra data apis
    """
    weather_call = create_weather_link(LAT, LONG, WEATHER_API_KEY)

    traffic_call = create_incidents_link(TRAFFIC_API_KEY, box_left, box_up, box_right, box_down)

    weather_info = requests.get(weather_call).json()
    traffic_info = requests.get(traffic_call).json()

    weather_info = extract_weather_info(weather_info)
    traffic_info = extract_traffic_info(traffic_info)

    for info in traffic_info:
        weather_info.append(info)

    all_api_responses = [str(column) for column in weather_info]
    return all_api_responses


#################################################################

def model_predictor(img_path, detector):
    """Predictions on the stores frames
    """
    return model_predict(img_path, detector)


if __name__ == "__main__":
    print(call_apis())
