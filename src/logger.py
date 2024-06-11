import os
import logging
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"    # format of the log file

log_path = os.path.join(os.getcwd(), "log", LOG_FILE)               # path of log file
os.makedirs(log_path,exist_ok=True)                                 # directory for log file

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)                    # we will get log file and its path

logging.basicConfig(filename=LOG_FILE_PATH, level=logging.INFO, format="[%(asctime)s] %(lineno)d %(name)s -%(levelname)s %(message)s")
