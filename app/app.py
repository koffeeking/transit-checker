"""print the next g train"""
import time
from utils import get_next_g_train

if __name__ == "__main__":
    while True:
        # run the function
        get_next_g_train()
        # pause for 5 seconds before the next run
        time.sleep(5)
