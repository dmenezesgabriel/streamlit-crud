import logging
from typing import Union


class SingletonLogger:
    _instance = None
    logger = None

    def __new__(cls) -> "SingletonLogger":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            logger = logging.getLogger("app")
            logger.setLevel(logging.INFO)

            # Create a console handler and set the level to INFO
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)

            # Create a formatter and add it to the handlers
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            console_handler.setFormatter(formatter)

            # Add the handlers to the logger
            logger.addHandler(console_handler)
            cls._instance.logger = logger

        return cls._instance


def get_logger() -> Union[logging.Logger, None]:
    return SingletonLogger().logger
