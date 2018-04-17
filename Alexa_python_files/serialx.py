import serial
from serial.serialutil import SerialException
import time
from serial import Serial
import sys

Usb_Port="/dev/ttyUSB0"



def Test_Serial_Port () :
    try:
        xbee=Serial(Usb_Port, 9600,timeout=3)
        xbee.close()
    except SerialException :
        print("Error Check the usb_port of the xbee or change the 'Usb_port' variale")
        sys.exit() 

#get data gets data from the xbee of the arduino (with the particular name)
#        *since for now we are using only one arduino* 
def getData():
    xbee=Serial(Usb_Port, 9600,timeout=3) # opening the port connected to the xbeee coordinator
    data = xbee.readline()#receive data from the xbee which was called
    #xbee.flush()
    #xbee.close()
    print(str(data.decode().strip()))



def writeData(msg):
    try:
        
        msg = msg.encode()
        xbee=Serial(Usb_Port, 9600,timeout=2) # opening the port connected to the xbeee coordinator
        xbee.write(msg)
        temp = str(xbee.readline().decode().strip())

        while temp is "":
            xbee.write(msg)
            temp = str(xbee.readline().decode().strip())

        print(temp)
    except Exception as e:
        print(e)
    return temp
   # print( msg + " sent")
    #xbee.flush()
    #xbee.close()

    
