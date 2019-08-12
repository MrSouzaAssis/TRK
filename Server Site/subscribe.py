 # -*- coding: utf-8 -*-
import socket, log, time, mysql.connector
import paho.mqtt.subscribe as subscribe

broker_url = 'soldier.cloudmqtt.com'
broker_port = 18002
broker_user = 'anvbaiiw'
broker_pass = 'mLg9v9rNYvKo'


def subscriber(topic):
		msg = subscribe.simple(topic, hostname=broker_url, port=broker_port, auth={'username': broker_user, 'password': broker_pass})
		print(msg.topic,msg.payload)
		time.sleep(1.5)

while True:
	subscriber('#')