
import logging
# logging.propagate = False #To turn off the module logger sending logs to the root logger
# Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Set up logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Set up file handler
file_handler = logging.FileHandler('_outputs/log.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Add file handler to logger
logger.addHandler(file_handler)

logger.info('Customer Logger called')

# Log messages
# logger.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is a critical message')
