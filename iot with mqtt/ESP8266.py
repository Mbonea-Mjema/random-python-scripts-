def callback(topic,message):
    Ledpin = machine.Pin(0)
    topic=topic.decode()
    message=message.decode()
    if topic =='auto/humidity':
        #value=call the dht fuction
        client.publish('auto/auck/temperature',value)
    if topic =='auto/temperature':
        #value=call the dht fuction
        client.publish('auto/auck/temperature',value)
    if message =='on':
        Ledpin.value(1)
        client.publish('auto/auck/light','on')
    if message =='off':
        Ledpin.value(1)
        client.publish('auto/auck/light','off')
    
