import paho.mqtt.client as mqtt

# Define MQTT callback functions
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("sensor/node1")  # Subscribe to the topic where the sensor node publishes data

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    # Process incoming message - extract sensor data and handle as needed

def initialize_mqtt_client():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("broker.example.com", 1883, 60) #change this
    client.loop_start()
    
def start_mqtt_client():
    initialize_mqtt_client()
    # Add any additional logic or operations here if needed
