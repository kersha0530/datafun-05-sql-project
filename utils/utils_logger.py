"""
utils_logger.py

This module configures logging for the project.
"""

import logging

# Configure logger
logging.basicConfig(
    filename="logs/project_log.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Logger initialized successfully.")
