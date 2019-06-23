""" Logging for blm simulator """

import logging
import os.path

import blmsim

if os.path.isdir(blmsim.LOG_DIR) is False:
    os.mkdir(blmsim.LOG_DIR)


class BLMLog:

    def __init__(self, name, verbosity=0):
        self.name = name
        # self.path = os.path.join(blmsim.LOG_DIR, f'{self.name}')
        self.logger = logging.getLogger(self.name)
        log_format = logging.Formatter('s:%(levelname)s:%(message)s')
        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setFormatter(log_format)
        self.logger.addHandler(self.stream_handler)
        self.set_verbosity(verbosity)
        self.logger.setLevel(logging.DEBUG)

    def set_verbosity(self, verbosity=0):
        log_level = max(0, logging.INFO - logging.DEBUG*verbosity)
        self.stream_handler.setLevel(log_level)


BLMLOG = BLMLog('blmlog')
