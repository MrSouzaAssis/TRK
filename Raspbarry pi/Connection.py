# -*- coding: utf-8 -*-
import socket
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
import Log

broker_url = 'postman.cloudmqtt.com'
broker_port = 12018
broker_user = 'xevwfqdz'
broker_pass = 'qqFxDSf1Fi5Y'
topic = '001'

def test(broker_url, broker_port):
	status = False
	try:
		s = socket.socket()
		s.connect((broker_url, broker_port))
		Log.eventadd('Connection:Has been established with host {} under port {}.' .format(broker_url, str(broker_port)))
		status = True
		return status

	except ConnectionRefusedError:
		Log.eventadd('Connection:Refused by host {} under port {}.' .format(broker_url, str(broker_port)))
		return status

	except socket.gaierror:
		Log.eventadd('Connection:Hostname problem: Connection to {}.' .format(broker_url))
		return status

	except Exception as erro:
		Log.eventadd('Connection:Problem with network: Connection to {}.\n           {}' .format(broker_url, erro))
		return status


def publisher(payload):
	if test(broker_url, broker_port) == True:
		publish.single(topic, payload, hostname=broker_url, port=broker_port, qos=1, auth={'username': broker_user, 'password': broker_pass})
		return print('transmitido')
	else:
		return Log.eventadd('Publish:Connection failure with broker.')


def subscriber(topic):
		msg = subscribe.simple(topic, hostname=broker_url, port=broker_port, auth={'username': broker_user, 'password': broker_pass})
		print(msg)
		time.sleep(1.5)
		