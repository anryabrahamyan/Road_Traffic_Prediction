"""
Main recording loop
"""
from datetime import datetime
import time
from utils import *
from params_and_keys import FRAME_PATH,COLUMN_NAMES


def record()->List[str]:
    """
    Create recording row
    """
    try:
        record_and_store()
        number_info = model_predictor(FRAME_PATH,detector)
    except:
        number_info = {f"info_{i}":None for i in range(45)}
    api_responses = call_apis()
    api_responses.extend(number_info.values())
    final_row = [str(info) for info in api_responses]
    
    return final_row
    
    
def store():
    """Store the recorded rows
    """
    # with open("dataset/data.csv","a") as data:
    #     data.write(",".join(COLUMN_NAMES)+"\n")
    while True:
        start = time.time()
        try:
            current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            new_row = record()
            total_row = [current_time]+new_row
            
            with open("dataset/data.csv","a") as data:
                data.write(",".join(total_row)+"\n")
        except:
            print('something went wrong')
        end = time.time()
        elapsed = end-start
        if elapsed<WAIT_TIME:
            time.sleep(WAIT_TIME-elapsed)


if __name__ =="__main__":
    print("starting...")
    store()
