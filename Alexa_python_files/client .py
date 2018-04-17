import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import serial
import  serialx as x
import vlctrial as m
import random

#x.Test_Serial_Port()
#communication with arduino
playlist = ["favourite","other"]
ch = random.choice(playlist)
song = m.music().music(ch)
def subroutine(topic , payload):
    global song
    topic = topic.replace("eee/","")
    if(payload == "ON" and topic == "light"):
        res = x.writeData("LON")
        publish.single("eee/ack",res,hostname="iot.eclipse.org")
    elif(payload == "bedroom On" and topic == "light"):
        res = x.writeData("bedroom on")
        publish.single("eee/ack","The bedroom lights are on",hostname="iot.eclipse.org")
    elif(payload == "bedroom Off" and topic == "light"):
        x.writeData("bedroom off")
        publish.single("eee/ack","The bedroom lights are off",hostname="iot.eclipse.org")
    elif(payload == "living room On" and topic == "light"):
        x.writeData("living on")
        publish.single("eee/ack","The living room lights are on",hostname="iot.eclipse.org")
    elif(payload == "living room Off" and topic == "light"):
        x.writeData("living off")
        publish.single("eee/ack","The living room lights are on",hostname="iot.eclipse.org")
    elif(payload == "OFF" and topic == "light"):
        res = x.writeData("LOFF")
        publish.single("eee/ack",res,hostname="iot.eclipse.org")
    elif(payload == "ON" and topic == "fan"):
        x.writeData("FON")
        publish.single("eee/ack","The fan has been turned on",hostname="iot.eclipse.org")
    elif(payload == "OFF" and topic == "fan"):
        x.writeData("FOFF")
        publish.single("eee/ack","The fan has been turned on",hostname="iot.eclipse.org")
    elif(payload == "ON" and topic == "music"):
        playlist = ["favourite","other"]
        song.stop()
        ch = random.choice(playlist)
        song = m.music().music(ch)
        song.play()
    elif(payload == "awesome" and topic == "music"):
        song.stop()
        song = m.music().music("favourite")
        song.play()
    elif(payload == "other" and topic == "music"):
        song.stop()
        song = m.music().music(payload)
        song.play()
    elif(payload == "OFF" and topic == "music"):
        song.stop()
    elif(payload == "pause" and topic == "music"):
        song.pause()
    elif(payload == "play" and topic == "music"):
        song.play()
    elif(payload == "next" and topic == "music"):
        song.next()
    elif(payload == "previous" and topic == "music"):
        song.previous()
    elif(payload == "forward" and topic == "robot"):
        print(payload)
        x.writeData("8")
        #publish.single("eee/ack","",hostname="iot.eclipse.org")
    elif(payload == "backward" and topic == "robot"):
        x.writeData("2")
        #publish.single("eee/ack","",hostname="iot.eclipse.org")
    elif(payload == "right" and topic == "robot"):
        x.writeData("6")
        #publish.single("eee/ack","",hostname="iot.eclipse.org")
    elif(payload == "left" and topic == "robot"):
        x.writeData("4")
        #publish.single("eee/ack","",hostname="iot.eclipse.org")
    elif(payload == "stop" and topic == "robot"):
        x.writeData("5")
    elif(topic == "flash"):
        payload = payload
        x.writeData("flash")
        x.writeData(payload)
        publish.single("eee/ack","",hostname="iot.eclipse.org")
    else:
        print("None matches the topic and the payload")

def payload(msg):
    nmess = msg.replace("b","")
    nmess = nmess.replace("'","")
    return nmess

def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))


def on_message(mqttc, obj, msg):
    #msgg = payload(str(msg.payload))
    msgg = msg.payload.decode()
    print("recieved payload " + msgg)
    subroutine(str(msg.topic) , msgg)


def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)


# If you want to use a specific client id, use
# mqttc = mqtt.Client("client-id")
# but note that the client id must be unique on the broker. Leaving the client
# id parameter empty will generate a random id for you.
mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
##mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Uncomment to enable debug messages
# mqttc.on_log = on_log
mqttc.connect("m2m.eclipse.org", 1883, 60)
mqttc.subscribe("eee/light")
mqttc.subscribe("eee/fan")
mqttc.subscribe("eee/flash")
mqttc.subscribe("eee/music")
mqttc.subscribe("eee/robot")

mqttc.loop_forever()


