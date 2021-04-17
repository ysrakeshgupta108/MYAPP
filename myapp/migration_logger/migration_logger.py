import os
import logging.config
import sys
import yaml
from pprint import pprint
OFFMODE = False
def setup_logging(
    default_path='logger_config.yaml',
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """Setup logging configuration

    """
    sys.path.insert(0, os.path.dirname(__file__))
    filename = os.path.join(sys.path[0],default_path)
    path = filename
    #path = default_path
    value = os.getenv(env_key, None)

    if value:
        path = value
    if os.path.exists(path):
        #print('reading from config',path)
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
            logfile = config['handlers']['file_handler']['filename']
        pprint(config['handlers']['file_handler']['filename'])
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

setup_logging()

def get_logger():
    global OFFMODE
    if OFFMODE:
        logger = logging.getLogger('noLogger')
    else:
        logger = logging.getLogger('sampleLogger')

    #logger.getLogger('snowflake.connector').disabled = True
    #logger.getLogger("snowflake.connector.network").disabled = True
    return logger

def off_logger():
    global OFFMODE
    OFFMODE = True
    logger = logging.getLogger('sampleLogger')
    logger.disabled = True
    logger = logging.getLogger('noLogger')
    return logger

def log_result(result):
    '''to display the log of result of snowflake execution of sql query'''
    logger = get_logger()
    for row in result:
        logger.debug(row)

logger = get_logger()
logger.debug("debugging mode")
logger.info("info mode")
logger.error("error mode")
logger.warning("warning mode")

