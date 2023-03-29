import paho.mqtt.publish as publish
import time

# Set up the MQTT broker and topic
MQTT_BROKER = "test.mosquitto.org"
MQTT_TOPIC = "example/topic"

# Define some data to send
data = {"temperature": 25.5, "humidity": 60}

# Convert the data to a string and send it via MQTT
payload = str(data)
publish.single(MQTT_TOPIC, payload, hostname=MQTT_BROKER)

print("Data sent via MQTT.")

