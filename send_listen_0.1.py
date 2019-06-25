from pubnub.callbacks import SubscribeCallback 
from pubnub.enums import PNStatusCategory  
from pubnub.pnconfiguration import PNConfiguration  
from pubnub.pubnub import PubNub, SubscribeListener   
import threading 
pnconfig = PNConfiguration() 

pnconfig.subscribe_key = "sub-c-bab9dc6c-912f-11e9-9769-e24cdeae5ee1" 
pnconfig.publish_key = "pub-c-14a2c33b-ff74-4bb7-8139-ff46eed621cc" 

pubnub = PubNub(pnconfig)
 
msg = raw_input("enter your message: ")

my_listener = SubscribeListener()
pubnub.add_listener(my_listener)
 
pubnub.subscribe().channels('awesomeChannel').execute()
my_listener.wait_for_connect()
print('connected')



result = my_listener.wait_for_message_on('awesomeChannel')

def publish_callback(envelope, status):
    # Check whether request successfully completed or not
    if not status.is_error():
        pass  # Message successfully published to specified channel.
    else:
        pass  # Handle message publish error. Check 'category' property to find out possible issue
        # because of which request did fail.
        # Request can be resent using: [status retry];

pubnub.publish().channel('awesomeChannel').message(msg).pn_async(publish_callback)

def send_listen (msg, result) :
	while msg and result != "":

	
		msg = raw_input("enter your message: ")
	
		print(result.message)
		
		if msg == "bye":
			break
	
t = threading.Thread(target = send_listen)

t.start()


print("Disconnected")

