import paho.mqtt.client as mqtt

# Set up the MQTT broker and topic
MQTT_BROKER = "test.mosquitto.org"
MQTT_TOPIC = "example/topic"

# Define a callback function to handle incoming messages
def on_message(client, userdata, message):
    payload_str = message.payload.decode('utf-8')
    data = eval(payload_str)  # Convert the string back to a dictionary
    print("Data received via MQTT:")
    print(data)

# Set up the MQTT client and connect to the broker
client = mqtt.Client()
client.connect(MQTT_BROKER, 1883)

# Set up the callback function to be called when a message is received
client.on_message = on_message

# Subscribe to the MQTT topic
client.subscribe(MQTT_TOPIC)

# Start the MQTT client loop to listen for incoming messages
client.loop_forever()
