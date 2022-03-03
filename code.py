import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) 

GPIO.setup(6, GPIO.OUT)
GPIO.setup(17, GPIO.IN)

while 1:
    a = GPIO.input(17)
    b = not a
    GPIO.output(6,b)