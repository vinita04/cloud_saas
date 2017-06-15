#!/usr/bin/python2

import os,commands,sys,time,socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",8888))

cdata=s.recvfrom(100)
cdata1=s.recvfrom(100)

if cdata[0]=='test':
	if cdata1[0]=='123':
		s.sendto("Authentication done!!!!!",cdata[1])
	else :
		s.sendto("password invalid",cdata[1])
else:
	s.sendto("user not exist!!!",cdata[1])
	


