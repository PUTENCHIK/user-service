from models.MyClient import MyClient


class Subscriber(MyClient):
    def __init__(self, number: int):
        super(Subscriber, self).__init__(f"subscriber{number}")
        self.client.on_message = self.on_message
        self.connect()

    def on_message(self, client, userdata, message):
        data = str(message.payload.decode("utf-8"))
        self.logger.add_info("Received message: " + data)

    def subscribe(self):
        self.logger.add_debug(f"Subscribing on {Subscriber.path}")
        self.client.subscribe(Subscriber.path)
