
import sys
import time
import RPi.GPIO as GPIO

mode= GPIO.getmode()

#GPIO.cleanup()

Forward=26
Backward=21
sleeptime=1

fwd = 17
bck = 18    


GPIO.setmode(GPIO.BCM)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)

GPIO.setup(fwd, GPIO.OUT)
GPIO.setup(bck, GPIO.OUT)


GPIO.setwarnings(False)

def forward(x):
	GPIO.output(Forward, GPIO.HIGH) 
	GPIO.output(fwd, GPIO.HIGH) 
	
	print("Moving Forward")
	time.sleep(x)
	GPIO.output(Forward, GPIO.LOW)
	GPIO.output(fwd, GPIO.LOW)


def reverse(x):
	GPIO.output(Backward, GPIO.HIGH)
	GPIO.output(bck, GPIO.HIGH)
	
	print("Moving Backward")
	time.sleep(x)
	GPIO.output(Backward, GPIO.LOW)
	GPIO.output(bck, GPIO.LOW)


def left(x):
	#GPIO.output(fwd, GPIO.HIGH)
	
	GPIO.output(Forward, GPIO.HIGH)
	print('left')
	time.sleep(x)
	#GPIO.output(fwd, GPIO.LOW)
	GPIO.output(Forward, GPIO.LOW)  # bck is left wheel
	
def right(x):
	
	GPIO.output(fwd, GPIO.HIGH)
	#GPIO.output(Backward, GPIO.HIGH)
	print('right')
	time.sleep(x)
	
	GPIO.output(fwd , GPIO.LOW)
	#GPIO.output(Backward, GPIO.LOW)

while (1):

	#forward(5)

	reverse(5)
	#left(5)
	#right(5)
	GPIO.cleanup()


