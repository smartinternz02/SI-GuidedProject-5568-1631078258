import json
import wiotp.sdk.device
import time


myConfig={
    "identity": {
        "orgId": "f6tnf7",
        "typeId": "rsip",
        "deviceId": "1001"
        },
    "auth":{
        "token" :"1234567890"
    }
     }   

client = wiotp.sdk.device.DeviceClient(config=myConfig,logHandlers=None)
client.connect()

while True:
    name="sakshi"
    #in area location
    #latitude=17.4225176
    #longitude=70.5450042

    #out area location
    latitude=17.4225176
    longitude=78.5450042
    myData={'name':name,'lat':latitude,'lon':longitude}
    client.publishEvent(eventId="status",msgFormat="json",data=myData,qos=0,onPublish=None)
    print("Data published to IBM IoT platform :",myData)
    time.sleep(5)

client.disconnect()    
    
