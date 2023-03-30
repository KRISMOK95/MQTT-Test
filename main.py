import paho.mqtt.publish as publish
import time
import json

# Set up the MQTT broker and topic
MQTT_BROKER = "test.mosquitto.org"
MQTT_TOPIC = "AAS/data"

# Define a list of data to send
data_list = [2, 3, 4, 5, 6]

# Convert the data to a JSON string and send it via MQTT
while True:
    for data in data_list:
        payload = json.dumps([data])
        publish.single(MQTT_TOPIC, payload, hostname=MQTT_BROKER)
        print("Data sent via MQTT:", data)
        time.sleep(2)
