#!/usr/bin/python2

import os,time,sys,commands,getpass,socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s_ip="192.168.122.1"
s_port=8888
print "loading cloud services enter authentication details!!!"
time.sleep(2)

suser=raw_input("enter username : ")
spass=getpass.getpass("enter password : ")

sdata=s.sendto(suser,(s_ip,s_port))
sdata1=s.sendto(spass,(s_ip,s_port))

sdata=s.recvfrom(100)[0]
print sdata
if sdata=="Authentication done!!!!!" :
	
	print "wait for services"
	time.sleep(2)
	execfile("saas.py")
elif sdata=="password invalid":
	 	exit()
	
else:
	exit()
