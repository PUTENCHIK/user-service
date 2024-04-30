# from fastapi import FastAPI
#
#
# app = FastAPI()
# port = 5002
#
#
# @app.get("/")
# def root():
#     return {"message": "Hello on publisher!"}

# publisher
import time
import paho.mqtt.client as mqtt_client
import random

broker = "broker.emqx.io"

# client = mqtt_client.MyClient('isu100123234235')
# FOR new version change ABOVE line to
client = mqtt_client.MyClient(
   mqtt_client.CallbackAPIVersion.VERSION1,
   'isu1001230012312312'
)

print("Connecting to broker", broker)
print(client.connect(broker))
client.loop_start()
print("Publishing")

for i in range(10):
    state = "on" if random.randint(0, 1) == 0 else "off"
    state = state + "ArtemV"
    print(f"State is {state}")
    client.publish("lab/leds/state", state)
    time.sleep(2)

client.disconnect()
client.loop_stop()