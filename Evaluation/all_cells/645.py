# set root logger level
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

# setup custom logger
logger = logging.getLogger(__name__)
handler = logging.FileHandler('geolocation.log')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# log
logger.info('This file is used to debug the next code part related to geolocation of universities/institutions')