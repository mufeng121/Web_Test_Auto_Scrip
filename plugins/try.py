import logging

from logging.handlers import TimedRotatingFileHandler
from logging.handlers import RotatingFileHandler

logging.basicConfig(filename='./test_logging_info.log', encoding='utf-8',
                            level=logging.INFO, format='%(asctime)s %(message)s')

#using naming loggers to ouput module-level's name
logger = logging.getLogger("attack1")
logging.info(logger)

#logging the start_time and finish_time of attack
logging.info('Started')


logging.info('Finished')
