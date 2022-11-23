import logging
import time
from logging.handlers import TimedRotatingFileHandler
from logging.handlers import RotatingFileHandler

class logging_module():
    # get the name of the class to know the type of attack
    def __init__(self):
        logging.info(self.__class__.__name__)
        
    # comment below to get granular debug information
    #logging.basicConfig(filename='./test_logging_debug.log',  level=logging.DEBUG)

    # change filename to set where the log file stored
    # default format for date/time display (shown above) is in ISO8601 
    logging.basicConfig(filename='./test_logging_info.log', 
                            level=logging.INFO, format='%(asctime)s %(message)s')

    #using naming loggers to ouput module-level's name
    logger = logging.getLogger(__name__)
    logging.info(logger)

    #logging the start_time and finish_time of attack
    logging.info('Started')
    logging.warning(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    logging.info('Finished')
   

    # create a logger object
    logger_fh = logging.getLogger()
    logger_fh.setLevel(logging.DEBUG)
    #create a handler object 
    fh = logging.FileHandler('./1111test.log') 
    fh.setLevel(logging.DEBUG) 
    # set formatter for the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') 
    #add formatter to handler
    fh.setFormatter(formatter) 

    # print to screen
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    #add handler to logger
    logger_fh.addHandler(fh) 
    logger_fh = logging.getLogger() 
    #sector log 
    handler = logging.handlers.TimedRotatingFileHandler('./test_logging_handler.log', 'S', 1, 0) 
    #add suffix to the log 
    handler.suffix = '%Y%m%d' 
    #add logger to handler
    logger_fh.addHandler(handler) 
    logger_fh.warning('test_handler') 
