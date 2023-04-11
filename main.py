import paho.mqtt.publish as publish
import time

# Set up the MQTT broker and topic
MQTT_BROKER = "test.mosquitto.org"
MQTT_TOPIC = "example/topic"

# Define the data as a list
data = [216, 0, 0, 0, 32, 0, 0, 0, 0, 0, 0, 230, 0]

# Loop and send the data via MQTT every second
while True:
    # Convert the list to a string and send it via MQTT
    payload = str(data)
    publish.single(MQTT_TOPIC, payload, hostname=MQTT_BROKER)
    print("Data sent via MQTT.")
    print(type(data))

    # Wait for 1 second before sending the next data
    time.sleep(1)
