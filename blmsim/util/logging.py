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
        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setFormatter(BLMFormatter())
        self.logger.addHandler(self.stream_handler)
        self.set_verbosity(verbosity)
        self.logger.setLevel(logging.DEBUG)

    def set_verbosity(self, verbosity=0):
        log_level = max(0, logging.INFO - logging.DEBUG*verbosity)
        self.stream_handler.setLevel(log_level)

class BLMFormatter(logging.Formatter):

    FORMATS = {
        logging.INFO: '{message}',
        'default': '[{levelname}]: {message}',
        }

    def __init__(self):
        super().__init__('', style='{')

    def format(self, record):
        self._fmt = self.FORMATS.get(record.levelno, self.FORMATS['default'])
        self._style = logging.StrFormatStyle(self._fmt)
        return super().format(record)

BLMLOG = BLMLog('blmlog').logger
