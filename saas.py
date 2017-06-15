#!/usr/bin/python2

import os
x='''
press 1 to get vlc
press 2 to get firefox
press 3 to get office
press 4 to get screenshot
press 5 to get calculator
press 6 to get webcam
'''
print x
ch=raw_input("enter ur choice : ")
if ch=='1':
	print "wait for a second" 
	execfile('vlc.py')
elif ch=='2':
	print "wait for a second"
	execfile('firefox.py')
elif ch=='3':
	print "wait for a second"
	execfile('office.py')
elif ch=='4':
	print "wait for a second"
	execfile('screenshot.py')
elif ch=='5':
	print "wait for a second"
	execfile('calculator.py')
elif ch=='6':
	print "wait for a second"
	execfile('webcam.py')
else:
	print "wrong input"



