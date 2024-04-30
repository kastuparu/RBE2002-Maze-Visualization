from paho.mqtt import client as mqtt_client
from ast import literal_eval as make_tuple
import time
import random


class MQTTClient:

    def __init__(self, server="robomqtt.cs.wpi.edu", port=1883, username="team4", password="sjaelland3453"):

        def on_connect(client: mqtt_client, userdata, flags, rc, properties):
            if rc == 0:
                print(f"Connected to {server}")
            else:
                print(f"Failed to connect to {server}, return code %d\n", rc)

        self.name = username
        client_id = f'python-mqtt-{random.randint(0, 1000)}'
        self.client = mqtt_client.Client(client_id=client_id,
                                         callback_api_version=mqtt_client.CallbackAPIVersion.VERSION2)
        self.client.username_pw_set(username, password)
        self.client.on_connect = on_connect
        self.client.connect(server, port)

        self.coordinates = []
        self.complete = False

    def publish(self, topic, msg):
        topic = self.name + "/" + topic
        result = self.client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print(f"Sent '{topic}:{msg}'")
        else:
            print(f"Failed to send '{topic}:{msg}'")

    def subscribe(self):
        def on_message(client: mqtt_client, userdata, msg):
            print(f"Received '{msg.topic}:{msg.payload.decode()}'")
            if msg.topic == coordinates_topic:
                self.coordinates.append(make_tuple(msg.payload.decode()))
            elif msg.topic == complete_topic:
                self.complete = True

        coordinates_topic = self.name + "/robot-d/(i, j)"
        complete_topic = self.name + "/robot-d/complete"
        self.client.subscribe(coordinates_topic)
        self.client.subscribe(complete_topic)
        self.client.on_message = on_message


def get_coordinates():
    client = MQTTClient()
    client.subscribe()
    client.client.loop_start()
    while not client.complete:
        time.sleep(0.1)
    client.client.loop_stop()
    return client.coordinates
