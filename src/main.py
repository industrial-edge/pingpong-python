# Copyright 2020 Siemens AG
# This file is subject to the terms and conditions of the MIT License.  
# See LICENSE file in the top-level directory

# Simple demonstation of MQTT functionality in python for edge apps.

import paho.mqtt.client as mqtt
import os
import json

print("start")

#============================
# Reading Configuration
#============================

def read_parameter(jsonfile):
    with open(jsonfile) as params:
        data = json.load(params)
        return data

# Read config file if existing
try:
   params = read_parameter('/cfg-data/mqtt-config.json')
   MQTT_USER = params['MQTT_USER']
   MQTT_PASSWORD = params['MQTT_PASSWORD']
   MQTT_IP = params['MQTT_IP']
   TOPIC_1 = params['TOPIC_1']
   TOPIC_2 = params['TOPIC_2']

# If no config file exists e.g in standalone application, configure with environment variables
except:
   print("Warning, using default environment values because reading config json file failed")
   MQTT_USER = os.environ['MQTT_USER']
   MQTT_PASSWORD = os.environ['MQTT_PASSWORD']
   MQTT_IP = os.environ['MQTT_IP']
   TOPIC_1 = os.environ['TOPIC_1']
   TOPIC_2 = os.environ['TOPIC_2']

print(f"user: {MQTT_USER}, pw:{MQTT_PASSWORD}, IP:{MQTT_IP}, topic1:{TOPIC_1}, topic2:{TOPIC_2}")


#============================
# Main Function
#============================


def on_message(client, userdata, message):
   print("recieved message: " ,message.payload.decode("utf-8"), "on: " ,message.topic)
   if message.payload.decode("utf-8") == "Ping":
      client.publish(TOPIC_2,"Pong")
   elif message.payload.decode("utf-8") == "Pong":
      client.publish(TOPIC_2,"Ping")
   else:
      client.publish(TOPIC_2,"I only answer to Ping or Pong") 


#as soon as the client connects successfully, it subscribes to topic1
def on_connect(client, userdata, flags, rc):
    print("Connected to " + MQTT_IP)
    client.subscribe(TOPIC_1)


client = mqtt.Client()
#set username and password, must be created it databus configurator
client.username_pw_set(os.environ['MQTT_USER'],os.environ['MQTT_PASSWORD'])
#add callback functions
client.on_message = on_message
client.on_connect = on_connect
#MQTT_IP must contain the service name of the databus app of the device
client.connect(MQTT_IP)
#clients always waits for messages
client.loop_forever()

