import importlib
import logging.config
import os

from decouple import config  # type: ignore
from src.common.utils.singleton import Singleton


class ConfigDefault(metaclass=Singleton):
    DATABASE_URI = config(
        "DATABASE_URI", default="sqlite+aiosqlite:///./books.db", cast=str
    )
    LOG_LEVEL = config("LOG_LEVEL", default="INFO", cast=str)


class ConfigDevelopment(ConfigDefault):
    LOG_LEVEL = config("LOG_LEVEL", default="DEBUG", cast=str)


def get_config() -> ConfigDefault:
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    app_config: ConfigDefault = getattr(
        importlib.import_module("src.config"),
        f"Config{ENVIRONMENT.capitalize()}",
    )
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": (
                    "%(asctime)s = %(levelname)s -%(name)s - %(message)s"
                ),
                "datefmt": "%Y-%m-%d %H:%M:%s",
            }
        },
        "handlers": {
            "stdout_logger": {
                "formatter": "standard",
                "class": "logging.StreamHandler",
            }
        },
        "loggers": {
            "": {
                "level": app_config.LOG_LEVEL,
                "handlers": ["stdout_logger"],
                "propagate": False,
            }
        },
    }
    logging.config.dictConfig(LOGGING)
    return app_config
