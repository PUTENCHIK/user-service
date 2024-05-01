from time import sleep
from logs import get_logger


out = 1

if __name__ == "__main__":
    logger1 = get_logger("logger1")
    logger1.info("Start logging")
    while True:
        try:
            sleep(out)
            logger1.info("Keeping logging")
        except KeyboardInterrupt:
            logger1.error("KeyboardInterrupt")
            break

    logger1.info("End logging")
