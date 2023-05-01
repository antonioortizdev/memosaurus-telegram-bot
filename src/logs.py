import logging


def log(msg: str) -> None:
    print(msg)
    logging.log(msg=msg, level=logging.INFO)


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)
