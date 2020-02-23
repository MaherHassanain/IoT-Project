import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect('localhost',1883) #as Broker

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("connected OK Returned code= ",rc)
        client.subscribe("topic/test")
    else:
        print("Bad connection Returned code=",rc)


while True:
    client.on_connect = on_connect
    client.publish("topic/test", input('Message : '))
