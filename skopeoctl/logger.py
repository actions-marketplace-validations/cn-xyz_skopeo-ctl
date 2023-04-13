"""python logger utils."""

import logging
import sys

from skopeoctl import constants


def gen_logger():
    # create logger
    if constants.LOG_LEVEL == 'DEBUG':
        log_level = logging.DEBUG
    elif constants.LOG_LEVEL == 'INFO':
        log_level = logging.INFO
    elif constants.LOG_LEVEL == 'WARN':
        log_level = logging.WARN
    elif constants.LOG_LEVEL == 'ERROR':
        log_level = logging.ERROR
    elif constants.LOG_LEVEL == 'FATAL':
        log_level = logging.FATAL
    else:
        log_level = logging.DEBUG
    formatter = logging.Formatter(
        fmt="%(asctime)-15s %(process)d %(levelname)s %(message)s - %(filename)s %(lineno)d",
        datefmt="%a %d %b %Y %H:%M:%S")

    _logger = logging.getLogger(name="cis")
    _logger.setLevel(log_level)

    fh = logging.FileHandler(filename="log.txt")
    fh.setLevel(log_level)
    fh.setFormatter(formatter)
    _logger.addHandler(fh)

    oh = logging.StreamHandler(sys.stdout)
    oh.setLevel(log_level)
    oh.setFormatter(formatter)
    _logger.addHandler(oh)
    return _logger


logger = gen_logger()
