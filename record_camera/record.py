"""
Main recording loop
"""
from datetime import datetime
import time
from utils import *

def record()->List[str]:
    """
    Create recording row
    """
    api_responses = call_apis()
    return api_responses
    #TODO return list of strings
    
    
def store():
    """Store the recorded rows
    """
    while True:
        start = time.time()
        current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        new_row = record()
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