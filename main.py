# publisher
# import time
# import paho.mqtt.client as mqtt_client
# import random
#
# broker = "broker.emqx.io"
#
# # client = mqtt_client.MyClient('isu100123234235')
# # FOR new version change ABOVE line to
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
# try:
#     for i in range(10):
#         state = "on" if random.randint(0, 1) == 0 else "off"
#         state = state + "ArtemV"
#         print(f"State is {state}")
#         client.publish("lab/leds/state", state)
#         time.sleep(2)
# except KeyboardInterrupt:
#     print("stop app")
#     client.disconnect()
#     client.loop_stop()


from models.Publisher import Publisher
import time, random


pub = Publisher()
pub.start()

try:
    for _ in range(10):
        first = 'Shadow Storm Vengeful Omni Winter'.split()
        second = 'Knight Fiend Magnus Ranger'.split()
        pub.publish(f"{random.choice(first)} {random.choice(second)}")
        time.sleep(random.randint(1, 2))
except KeyboardInterrupt:
    pub.stop()
