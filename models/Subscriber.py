import time
from models.MyClient import MyClient


class Subscriber(MyClient):
    def __init__(self):
        super(Subscriber, self).__init__("subscriber")
        self.client.on_message = self.on_message
        self.connect()

    def on_message(self, client, userdata, message):
        data = str(message.payload.decode("utf-8"))
        self.logger.add_info("Received message: " + data)

    def subscribe(self):
        self.logger.add_debug(f"Subscribing on {Subscriber.path}")
        self.client.subscribe(Subscriber.path)

    def simulate(self, delay: int = 0):
        self.start()
        self.subscribe()
        try:
            time.sleep(delay)
            self.logger.add_info("Subscriber ended simulation")
        except:
            self.stop()
            self.logger.add_error("Subscriber's simulation stopped by force")