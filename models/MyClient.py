import paho.mqtt.client as mqtt_client


class MyClient:
    broker = "broker.emqx.io"
    path = "lab/leds/state"

    @staticmethod
    def get_uuid():
        pass
