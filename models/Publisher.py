import time
from models.MyClient import MyClient


class Publisher(MyClient):
    def __init__(self, number):
        super(Publisher, self).__init__(f"publisher{number}")
        self.connect()

    def publish(self, text: str):
        self.logger.add_info("Published message: " + text)
        self.client.publish(Publisher.path, text)

    def simulate(self, amount: int = 5):
        self.logger.add_debug(f"Start simulating publisher's work")
        try:
            self.start()
            for _ in range(amount):
                delay = Publisher.random_publish_delay()
                time.sleep(delay)
                self.publish(f"some test text for delay {delay}")
        except KeyboardInterrupt:
            self.logger.add_error(f"Simulating was canceled")
            self.stop()
        finally:
            self.logger.add_info("Simulating ended")
            self.stop()
