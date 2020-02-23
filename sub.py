import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect('localhost',1883) #as Broker

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("connected OK Returned code= ",rc)
        client.subscribe("topic/test")
    else:
        print("Bad connection Returned code=",rc)


def on_message(client, userdata , message):
    print(message.paylaod.decode())
    print("message receieved")


while True:
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()
