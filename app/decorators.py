import logging
from datetime import datetime

from app.settings import CACHED_DATA, TIME_TO_CLEAN_CACHED_VAR

logger = logging.getLogger(__name__)


def clean_cache(func):
    """
    Decorator that will clean all cached data every "TIME_TO_CLEAN_CACHED_VAR" minutes.
    :param func:
    :return:
    """
    def func_wrapper(*args, **kwargs):
        if CACHED_DATA:
            try:
                diff = datetime.now() - CACHED_DATA.get("created_at")

                if (diff.seconds / 60) >= TIME_TO_CLEAN_CACHED_VAR:
                    CACHED_DATA.clear()
            except TypeError:
                logger.info("created_at is not defined in CACHED_DATA. Error in clean_cache wrapper")

        return func(*args, **kwargs)

    return func_wrapper
