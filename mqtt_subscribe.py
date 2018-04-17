import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("outTopic")
    client.subscribe("auto")
    #client.subscribe("outTopic")
def on_message(client, userdata, msg):
    print(msg.topic+" "+msg.payload.decode())

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)
client.loop_start()

