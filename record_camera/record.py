"""
Main recording loop
"""
from datetime import datetime
import time
from utils import *
from params_and_keys import LINK


def record(link:str = LINK )->List[str]:
    """
    Create recording row
    """
    record_and_store( link )
    api_responses = call_apis()
    number_info = model_predictor()
    final_row = [str(info) for info in number_info.extend(api_responses)]
    
    return final_row
    
    
def store():
    """Store the recorded rows
    """
    while True:
        start = time.time()
        current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        new_row = record(link=LINK)
        total_row = [current_time]+new_row
        
        with open("dataset/data.csv","a") as data:
            data.write(",".join(total_row)+"\n")
        end = time.time()
        elapsed = end-start
        if elapsed<WAIT_TIME:
            time.sleep(WAIT_TIME-elapsed)


if __name__ =="__main__":
    print("starting...")
    store()
