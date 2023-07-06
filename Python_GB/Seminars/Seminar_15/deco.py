import logging
from typing import Callable

FORMAT = "{levelname} - {asctime}: {msg}"
logging.basicConfig(format=FORMAT, style="{", filename='info.log', level=logging.INFO, encoding="UTF-8")

logger = logging.getLogger(__name__)


def deco_logger(func: Callable):
    def wrapper(*args, **kwargs):
        a, b = args
        res = func(a, b)
        logger.info(f"{func.__name__} {a} * {b} = {res}  ")

    return wrapper


@deco_logger
def multy(a: int, b: int, *args, **kwargs) -> int:
    return a * b


if __name__ == '__main__':
    multy(2, 5)
