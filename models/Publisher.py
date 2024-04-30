import paho.mqtt.client as mqtt_client
from models.MyClient import MyClient
from models.Logger import Logger


class Publisher(MyClient):
    def __init__(self):
        self.logger = Logger("publisher")

        client = mqtt_client.Client(
            mqtt_client.CallbackAPIVersion.VERSION1,
            Publisher.get_uuid()
        )
        self.logger.add_info("Connecting to broker: " + Publisher.broker)
        self.connection = str(client.connect(Publisher.broker))
        self.logger.add_info("Connection to broker: " + self.connection)

        self.client = client

    def start(self):
        self.logger.add_info("Start publisher loop")
        self.client.loop_start()

    def stop(self):
        self.logger.add_info("Stop publisher loop")
        self.client.disconnect()
        self.client.loop_stop()

    def publish(self, text: str):
        length_limit = 15
        self.logger.add_info("Publish message: " + (text if len(text) <= length_limit else text[:length_limit]+"..."))
        self.client.publish(text)
