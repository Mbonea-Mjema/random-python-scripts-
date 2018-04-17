# -*- coding: utf-8 -*-
import re
from wikiquote import quote_of_the_day
from wikipedia import summary as ans
import DSE
import os, subprocess, time
import RPi.GPIO as GPIO
from DSE import init
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

from yowsup.layers.interface                           import YowInterfaceLayer                 #Reply to the message
from yowsup.layers.interface                           import ProtocolEntityCallback            #Reply to the message
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity         #Body message
from yowsup.layers.protocol_presence.protocolentities  import AvailablePresenceProtocolEntity   #Online
from yowsup.layers.protocol_presence.protocolentities  import UnavailablePresenceProtocolEntity #Offline
from yowsup.layers.protocol_presence.protocolentities  import PresenceProtocolEntity            #Name presence
from yowsup.layers.protocol_chatstate.protocolentities import OutgoingChatstateProtocolEntity   #is writing, writing pause
from yowsup.common.tools                               import Jid                               #is writing, writing pause

#Log, but only creates the file and writes only if you kill by hand from the console (CTRL + C)
#import sys
#class Logger(object):
#    def __init__(self, filename="Default.log"):
#        self.terminal = sys.stdout
#        self.log = open(filename, "a")
#
#    def write(self, message):
#        self.terminal.write(message)
#        self.log.write(message)
#sys.stdout = Logger("/1.txt")
#print "Hello world !" # this is should be saved in yourlogfilename.txt
#------------#------------#------------#------------#------------#------------

allowedPersons=['919818748617','2348140636025','255764967956',"255754528638","447706788830","255766822850","255699210076"] #Filter the senders numbers
#'255754528638',
ap = set(allowedPersons)

name = "NAMEPRESENCE"
filelog = "/root/.yowsup/Not allowed.log"

class EchoLayer(YowInterfaceLayer):
    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        if messageProtocolEntity.getType() == 'text':
            time.sleep(0.5)
            self.toLower(messageProtocolEntity.ack()) #Set received (double v)
            time.sleep(0.5)
            self.toLower(PresenceProtocolEntity(name = name)) #Set name Presence
            time.sleep(0.5)
            self.toLower(AvailablePresenceProtocolEntity()) #Set online
            time.sleep(0.5)
            self.toLower(messageProtocolEntity.ack(True)) #Set read (double v blue)
            time.sleep(0.5)
            self.toLower(OutgoingChatstateProtocolEntity(OutgoingChatstateProtocolEntity.STATE_TYPING, Jid.normalize(messageProtocolEntity.getFrom(False)) )) #Set is writing
            time.sleep(2)
            self.toLower(OutgoingChatstateProtocolEntity(OutgoingChatstateProtocolEntity.STATE_PAUSED, Jid.normalize(messageProtocolEntity.getFrom(False)) )) #Set no is writing
            time.sleep(1)
            self.onTextMessage(messageProtocolEntity) #Send the answer
            time.sleep(3)
            self.toLower(UnavailablePresenceProtocolEntity()) #Set offline

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        print (entity.ack())
        self.toLower(entity.ack())

    def onTextMessage(self,messageProtocolEntity):
        namemitt   = messageProtocolEntity.getNotify()
        message    = messageProtocolEntity.getBody().lower()
        recipient  = messageProtocolEntity.getFrom()
        textmsg    = TextMessageProtocolEntity
        print(namemitt+" :"+message)
    

        #For a break to use the character \n
        #The sleep you write so #time.sleep(1)

        if True:
            if message == 'hi':
                answer = "Hi "+namemitt+" " 
                self.toLower(textmsg(answer, to = recipient ))
                print (answer)

            elif message == 'list':
                answer = "Hi "+namemitt+"\n\nYou can ask me these things:\n\nTemperature\nRestart\nOn GPIO14\nOff GPIO14\nDse"
                self.toLower(textmsg(answer, to = recipient ))
                print (answer)

            elif message == 'temperature':
                t=float(subprocess.check_output(["/opt/vc/bin/vcgencmd measure_temp | cut -c6-9"], shell=True)[:-1])
                ts=str(t)
                answer = 'My temperature is '+ts+' °C'
                self.toLower(textmsg(answer, to = recipient ))
                print (answer)

            elif message == 'restart':
                answer = "Ok "+namemitt+", rebooting. Bye bye."
                self.toLower(textmsg(answer, to = recipient ))
                print (answer)
                time.sleep(3)
                self.toLower(UnavailablePresenceProtocolEntity())
                time.sleep(2)
                os.system('reboot')

            elif message == 'on gpio14':
                GPIO.output(14, True) # Pin 2 in up
                answer = "Ok, its turning on"
                self.toLower(textmsg(answer, to = recipient ))
                print (answer)

            elif message == 'off gpio14':
                GPIO.output(14, False) # Pin 2 in down
                answer = "Ok, its turning off"
                self.toLower(textmsg(answer, to = recipient ))
                print (answer)

            elif message == 'dse':
                answer = init()
                self.toLower(textmsg(answer, to = recipient ))
                print (answer)

            elif "hello" in message:
                answer="Hi am raspi how can I help u :)"
                self.toLower(textmsg(answer, to = recipient))
                print (answer)

                
            elif "wiki" in message:
                keyWord=re.compile(r'\wiki (.*)')
                answer=ans(keyWord.findall(message),sentences=3)
                self.toLower(textmsg(answer, to = recipient))
                print ("sent the details")

            elif "quote" in message:
                answer=quote_of_the_day()
                self.toLower(textmsg(answer, to = recipient))
                print ("sent the details")
                


            else:
                answer = "Sorry "+namemitt+", I can not understand what you're asking me.." 
                self.toLower(textmsg(answer, to = recipient))
                print (answer)

            

        else:
            if "quote" in message:
                quote,person=(quote_of_the_day())
                answer=quote
                self.toLower(textmsg(answer, to = recipient))
                answer=person
                self.toLower(textmsg(answer, to = recipient))
                print ("sent the details")
    
            if(not 'wiki' in message):
                answer = "Hi "+namemitt+",am Rapy type 'wiki raspberry pi ' to know more about me,you can search wikipedia here too just type wiki followed by what you want eg 'wiki Obama'"
                time.sleep(20)
                self.toLower(textmsg(answer, to = recipient))
                            
            elif "wiki" in message:
                keyWord=re.compile(r'\wiki (.*)')
                answer=ans(keyWord.findall(message),sentences=3)
                self.toLower(textmsg(answer, to = recipient))
                print ("sent the details")
            elif "quote" in message:
                answer=quote_of_the_day()
                self.toLower(textmsg(answer, to = recipient))
                print ("sent the details")
            elif "hello" in message:
                answer="Hi am raspi how can I help u :)"
                self.toLower(textmsg(answer, to = recipient))
                print (answer)
                        
            elif message == 'dse':
                 answer = init()
                 self.toLower(textmsg(answer, to = recipient ))
                 print (answer)



                


        print("\n"*4)
        

