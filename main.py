from cellSegmentation.logger import logging
from cellSegmentation.exception import CustomException 

try:
    a = 1/0 
    print(a)
except Exception as e:
    logging.info(e)
