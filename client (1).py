import paho.mqtt.client as mqtt
import serial
import  serialx as x
import vlctrial as m
import random

x.Test_Serial_Port()
#communication with arduino
playlist = ["favourite","other"]
ch = random.choice(playlist)
song = m.music().music(ch)
def subroutine(topic , payload):
    global song
    topic = topic.replace("eee/","")
    if(payload == "ON" and topic == "light"):
        x.writeData("LON")
        x.getData()
    elif(payload == "OFF" and topic == "light"):
        x.writeData("LOFF")
        x.getData()
    elif(payload == "ON" and topic == "fan"):
        x.writeData("FON")
        x.getData()
    elif(payload == "OFF" and topic == "fan"):
        x.writeData("FOFF")
        x.getData()
    elif(payload == "ON" and topic == "music"):
        playlist = ["favourite","other"]
        ch = random.choice(playlist)
        song = m.music().music(ch)
        song.play()
    elif(payload == "awesome" and topic == "music"):
        song = m.music().music("favourite")
        song.play()
    elif(payload == "other" and topic == "music"):
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
        x.writeData("FORWARD")
        #x.getData()
    elif(payload == "backward" and topic == "robot"):
        x.writeData("BACKWARD")
        #x.getData()
    elif(payload == "right" and topic == "robot"):
        x.writeData("BACKWARD")
        #x.getData()
    elif(payload == "left" and topic == "robot"):
        x.writeData("FORWARD")
        #x.getData()
    elif(topic == "flash"):
        payload = payload
        x.writeData("flash")
        x.writeData(payload)
        x.getData()
    else:
        print("None matches the topic and the payload")

def payload(msg):
    nmess = msg.replace("b","")
    nmess = nmess.replace("'","")
    return nmess

def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))


def on_message(mqttc, obj, msg):
    msgg = payload(str(msg.payload))
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


