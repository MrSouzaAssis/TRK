# -*- coding: utf-8 -*-
import Adafruit_DHT, Connection, time
DHT_SENSOR = Adafruit_DHT.DHT22


def temperature_read():	
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, 4)

    if(humidity is not None and temperature is not None):
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
        Connection.publisher('{0.1f}'.format(humidity))
        Connection.publisher('{0.1f}'.format(temperature))