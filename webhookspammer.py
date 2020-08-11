import requests

webhook = input(">>Please enter the Webhook: ") #input for webhook url
print("Weebhook " + webhook + " set") #debug point
text = input(">>Please enter the Message that should be spammed: ") #asks for message
print("Message " + text + " set") #debug point


data = {
    "content": text #data for webhook as json
}

while True: #loop
    if True:
        requests.post(webhook, data=data) #sends data to webhook
        print("Sent Message " + text + " successful") #message for feedback lol