from fastapi import FastAPI, Request
from fastapi.exceptions import FastAPIError
from models.Publisher import Publisher


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello on publisher!"}


@app.exception_handler(FastAPIError)
async def exception_handler(request: Request, exc: Exception):
    print(f"Exception: {exc}")


@app.on_event("startup")
def start_app():
    publisher = Publisher()
    publisher.start()
    publisher.simulate()
    publisher.stop()


@app.on_event("shutdown")
def stop_app():
    pass

# publisher
# import time
# import paho.mqtt.client as mqtt_client
# import random

# broker = "broker.emqx.io"

# client = mqtt_client.MyClient('isu100123234235')
# FOR new version change ABOVE line to
# client = mqtt_client.Client(
#    mqtt_client.CallbackAPIVersion.VERSION1,
#    'isu1001230012312312'
# )
#
# print("Connecting to broker", broker)
# print(client.connect(broker))
# client.loop_start()
# print("Publishing")
#
# for i in range(10):
#     state = "on" if random.randint(0, 1) == 0 else "off"
#     state = state + "ArtemV"
#     print(f"State is {state}")
#     client.publish("lab/leds/state", state)
#     time.sleep(2)
#
# client.disconnect()
# client.loop_stop()


# from models.Publisher import Publisher
# import time, random
#
#
# pub = Publisher()
# pub.start()
#
# for _ in range(10):
#     first = 'Shadow Storm Vengeful Omni Winter'.split()
#     second = 'Knight Fiend Magnus Ranger'.split()
#     time.sleep(random.randint(1, 2))
#     pub.publish(f"{random.choice(first)} {random.choice(second)}")
#
# pub.stop()
