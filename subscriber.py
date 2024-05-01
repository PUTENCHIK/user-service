from fastapi import FastAPI
from models.Subscriber import Subscriber


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello on subscriber!"}


@app.on_event("startup")
def start_app():
    subscriber = Subscriber()
    subscriber.start()
    subscriber.simulate()
    subscriber.stop()

# #subscriber
# import time
# import paho.mqtt.client as mqtt_client
# import random
#
# broker = "broker.emqx.io"
#
# def on_message(client, userdata, message):
#     time.sleep(1)
#     data = str(message.payload.decode("utf-8"))
#     print("received message =", data)
#
# # client = mqtt_client.Client('isu100123123123')
# # FOR new version change ABOVE line to
# client = mqtt_client.Client(
#    mqtt_client.CallbackAPIVersion.VERSION1,
#    'isu10012300'
# )
# client.on_message=on_message
#
# print("Connecting to broker",broker)
# client.connect(broker)
# client.loop_start()
# print("Subcribing")
# client.subscribe("lab/leds/state")
# time.sleep(1800)
# client.disconnect()
# client.loop_stop()

from models.Subscriber import Subscriber
import time


sub = Subscriber()
sub.start()
sub.subscribe()
try:
    time.sleep(15)
except KeyboardInterrupt:
    sub.stop()
    exit()

sub.stop()