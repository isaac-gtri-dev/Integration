from pubnub.callbacks import SubscribeCallback 
from pubnub.enums import PNStatusCategory  
from pubnub.pnconfiguration import PNConfiguration  
from pubnub.pubnub import PubNub  

pnconfig = PNConfiguration() 

pnconfig.subscribe_key = "sub-c-bab9dc6c-912f-11e9-9769-e24cdeae5ee1" 
pnconfig.publish_key = "pub-c-14a2c33b-ff74-4bb7-8139-ff46eed621cc" 

pubnub = PubNub(pnconfig)
 
 
def publish_callback(envelope, status):
    # Check whether request successfully completed or not
    if not status.is_error():
        pass  # Message successfully published to specified channel.
    else:
        pass  # Handle message publish error. Check 'category' property to find out possible issue
        # because of which request did fail.
        # Request can be resent using: [status retry];
msg = raw_input("enter your message: ")
while msg != "":
	
	msg = raw_input("enter your message: ")
	pubnub.publish().channel('awesomeChannel').message(msg).pn_async(publish_callback)
	if msg == "bye":
		break
print("Disconnected")

