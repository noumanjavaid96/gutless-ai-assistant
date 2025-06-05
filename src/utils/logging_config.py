# src/utils/logging_config.py
import logging
import sys

def setup_logging(level=logging.INFO):
    """Configures basic logging for the application."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)  # Log to stdout
            # You can add FileHandler here if needed
            # logging.FileHandler("app.log")
        ]
    )
    # Quieten overly verbose libraries if necessary
    # logging.getLogger("slack_bolt.App").setLevel(logging.WARNING)
    # logging.getLogger("slack_sdk.web.client").setLevel(logging.WARNING)

if __name__ == '__main__':
    setup_logging(logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")
