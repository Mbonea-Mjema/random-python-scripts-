import paho.mqtt.publish as publish
import time
import random
count=0

publish.single("esp8266/data/",'get' ,hostname = "iot.eclipse.org")
print('published')
count+=1
time.sleep(1)

print("Done")
