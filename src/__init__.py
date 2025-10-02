import logging

from .module1 import Module1
from .module2 import Module2

__all__ = ["Module1", "Module2", "logger"]

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

logger.info("src package initialized")
