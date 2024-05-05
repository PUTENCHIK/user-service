import time
from models.MyClient import MyClient
from src.config import config


class Publisher(MyClient):
    def __init__(self):
        super(Publisher, self).__init__("publisher")
        self.connect()

    def publish(self, text: str):
        # length_limit = 15
        # self.logger.add_info("Published message: " + (text if len(text) <= length_limit else text[:length_limit]+"..."))
        self.logger.add_info("Published message: " + text)
        self.client.publish(Publisher.path, text)

    def simulate(self, amount: int = 5):
        self.logger.add_debug(f"Start simulating work by publisher")
        try:
            self.start()
            for _ in range(amount):
                delay = Publisher.random_publish_delay()
                time.sleep(delay)
                self.publish(f"some test text for delay {delay}")
        except:
            self.logger.add_error(f"Simulating was canceled")
            self.stop()
        finally:
            self.logger.add_info("Simulating ended")
            self.stop()
