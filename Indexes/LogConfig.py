import logging
from decouple import config

FILE_NAME=config('logFilePath')
logging.basicConfig(filename=FILE_NAME,level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

