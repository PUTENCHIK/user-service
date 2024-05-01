import logging, socket
import sys
import time
from logging.handlers import TimedRotatingFileHandler

FORMATTER_STRING = f"%(asctime)s — %(name)s — %(levelname)s — %(message)s - {socket.gethostbyname(socket.gethostname())}"
FORMATTER = logging.Formatter(FORMATTER_STRING)
LOG_FILE = "../logs.log"


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    logger.addHandler(console_handler)

    file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
    file_handler.setFormatter(FORMATTER)
    logger.addHandler(file_handler)

    return logger
