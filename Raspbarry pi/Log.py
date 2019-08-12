 # -*- coding: utf-8 -*-
from time import strftime

def eventadd(msg):
    data = strftime("%b %d %Y %H:%M:%S: ")

    try:
        syslog = open("syslog2.log", "a")
        syslog.write(data + msg + "\n")
        syslog.close()
        print(data + msg)

    except Exception as erro:
        print(str('Syslog Problem: {}'.format(erro)))
