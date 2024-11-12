#  Copyright Arcane Dreams Limited (c) 2024. All rights reserved.
import logging
import os
from logging import Logger
from logging.handlers import RotatingFileHandler

from rich.logging import RichHandler

from jcasc_tool import __project__

from jcasc_tool.helpers.helpers_date import get_time_formatted

_logger = None


def get_default_log_path() -> str:
    """
    Get the absolute path to where the log files should be stored.
    :return:
    """
    if __debug__:
        return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'logs'))
    else:
        return os.path.abspath(os.path.join(os.getcwd(), 'logs'))


def get_default_log_filename() -> str:
    """
    The name of the log file
    :return:
    """
    return f"{__project__}_{get_time_formatted()}.log"


def get_default_log_filepath() -> str:
    """
    Get the absolute path to where the log file is stored.
    :return: Returns the absolute path to where the log file is stored.
    """
    return os.path.join(get_default_log_path(), get_default_log_filename())


def _create_log_file_hanlder() -> logging.handlers.RotatingFileHandler:
    """
    Instantiate a new log file handler instance and return it
    :return:
    """
    file_handler = logging.handlers.RotatingFileHandler(get_default_log_filepath())
    return file_handler


def get_or_create_logger() -> logging.Logger:
    """
    Get or create the logger if it doesn't exist.
    :return:
    """
    global _logger
    if _logger is None:
        _logger = create_logger()

    return _logger


def create_logger() -> logging.Logger:
    """

    :return:
    """
    global _logger
    _logger = Logger(__project__)
    _logger.addHandler(
        RotatingFileHandler(os.path.join(os.getcwd(), get_default_log_filename())))
    _logger.addHandler(RichHandler(rich_tracebacks=True))

    return _logger
