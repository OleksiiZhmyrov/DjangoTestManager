import logging

from DjangoTestManager.settings import LOG_FILENAME


LOG_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'


def __get_logger():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)-8s %(message)s',
        datefmt=LOG_DATETIME_FORMAT,
        filename=LOG_FILENAME)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s: %(levelname)-8s %(message)s', datefmt=LOG_DATETIME_FORMAT)
    console.setFormatter(formatter)
    logger = logging.getLogger('')
    logger.addHandler(console)
    return logger


LOGGER = __get_logger()
