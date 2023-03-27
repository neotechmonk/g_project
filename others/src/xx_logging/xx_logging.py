import logging
logurl = '_outputs/log.log'
#Root level Logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s -  [%(levelname)s] - %(message)s",
    handlers=[
        logging.FileHandler(logurl),
        logging.StreamHandler()
    ]
)


#Module level logger
import xx_logging_helper as helper_logger
helper_logger = logging.getLogger(__name__)
helper_logger.info("Module logger from the custom code")

            
# Logging using the main logger
#------------------------------#
#By default DEBUG and INFO are disabled
# logging.debug('DEBUG') 
# logging.info('INFO')
# logging.warning('WARNING') #WARNING:root:WARNING
# logging.error('ERROR') #ERROR:root:ERROR
# logging.critical('CRITICAL') #CRITICAL:root:CRITICAL

