import serial
from serial.serialutil import SerialException
import time
from serial import Serial
import sys

Usb_Port="/dev/ttyUSB0"



def Test_Serial_Port () :
    try:
        xbee=Serial(Usb_Port, 9600)
        xbee.close()
    except SerialException :
        print("Error Check the usb_port of the xbee or change the 'Usb_port' variale")
        sys.exit() 

#get data gets data from the xbee of the arduino (with the particular name)
#        *since for now we are using only one arduino* 
def getData():
    xbee=Serial(Usb_Port, 9600) # opening the port connected to the xbeee coordinator
    data = xbee.readline()#receive data from the xbee which was called
    #xbee.flush()
    #xbee.close()
    print(str(data.decode().strip()))



def writeData(msg):
    msg = msg.encode()
    xbee=Serial(Usb_Port, 9600) # opening the port connected to the xbeee coordinator
    xbee.write(msg)#encode converts the string into bytes
   # print( msg + " sent")
    #xbee.flush()
    #xbee.close()
    
