# -*- coding: utf-8 -*-
import door_sensor as door 
import Connection as connection
import Log as log
import dht_sensor as dht
import time


broker_url = 'postman.cloudmqtt.com'
broker_port = 12018
timer = 10

while True:
	if connection.test(broker_url, broker_port) == True:
		try:
			door.door_read()
			time.sleep(timer)
			dht.temperature_read()
			time.sleep(timer)

	    except Exception as erro:
        	log.eventadd(erro)

	else:
		time.sleep(1000)
