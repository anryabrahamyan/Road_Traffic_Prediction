"""
Main recording loop
"""
import time
import os
from utils import *

def record():
    """
    Create recording row
    """
    pass

def store():
    """Store the recorded rows
    """
    while True:
        new_row = record()
        with open("../dataset/data.csv","a") as data:
            data.write(new_row)
        time.wait(WAIT_TIME)
    pass