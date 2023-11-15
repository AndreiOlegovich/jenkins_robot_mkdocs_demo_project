from random import randrange
from robot.api import logger


# mode = "python"
mode = "robot"
if mode == "robot":
    def print(s: str):
        logger.info(s)


def get_unstable_url() -> str:
    if randrange(2) == 1:
        url = "https://www.urn.su"
    else:
        url = "https://www.heihei.ru"    
    print(f"\nunstable url is: {url}\n")

    return url
