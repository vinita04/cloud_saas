#!/usr/bin/python2

import os,socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s_ip="192.168.122.1"
s_port=8888


os.system('sshpass -p 123 ssh -X test@'+s_ip+' firefox ')


execfile("saas.py")
