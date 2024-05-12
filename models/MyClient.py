import random
import requests
import paho.mqtt.client as mqtt_client
from fastapi.exceptions import FastAPIError

from models.Logger import Logger
from exceptions.NotReceivedUuid import NotReceivedUuid
from src.config import config
from src.connections import get_ip


class MyClient:
    broker = "broker.emqx.io"
    path = "lab/leds/state"

    def __init__(self, logger_name: str):
        self.logger_name = logger_name
        self.logger = Logger(logger_name)

        if self.check_connection():
            uuid = self.get_uuid()
        else:
            raise FastAPIError("UserClient doesn't answer")

        client = mqtt_client.Client(
            mqtt_client.CallbackAPIVersion.VERSION1,
            uuid
        )

        self.client = client

    def connect(self):
        self.logger.add_info("Connecting to broker: " + MyClient.broker)
        connection = self.client.connect(MyClient.broker)
        self.logger.add_info("Connection to broker: " + str(connection))

    def start(self):
        self.logger.add_info(f"Start {self.logger_name} loop")
        self.client.loop_start()

    def stop(self):
        self.logger.add_info(f"Stop {self.logger_name} loop")
        self.client.disconnect()
        self.client.loop_stop()

    def get_uuid(self) -> str:
        self.logger.add_debug("Request to get uuid")

        ip_service = get_ip()
        port = config['user_service_port']
        url = f"http://{ip_service}:{port}/get_uuid"

        try:
            response = requests.get(url)
        except:
            self.logger.add_error("No response from UserService's /get_uuid")
            raise NotReceivedUuid()

        obj = response.json()
        if "uuid" not in obj:
            self.logger.add_error("No uuid in response from UserService")
        else:
            self.logger.add_debug("Returning uuid")
            return obj["uuid"]

    def check_connection(self) -> bool:
        url = f"http://{get_ip()}:{config['user_service_port']}"
        try:
            self.logger.add_debug(f"Try to request: {url}")
            requests.get(url)
            self.logger.add_debug(f"Connection to {url} is okay")
            return True
        except:
            self.logger.add_error(f"Connection to {url} is failed")
            return False

    @staticmethod
    def random_publish_delay():
        minn = config["publish_delay_min"]
        maxx = config["publish_delay_max"]
        return minn + random.random()*(maxx - minn)


