import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup (dac, GPIO.OUT)
GPIO.setup (troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup (comp, GPIO.IN)

def dec2bin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]

def adc ():
    while (True):
        for i in range(256):
            GPIO.output(dac, dec2bin(i))
            time.sleep (0.01)
            
            if GPIO.input(comp) == 0:
                return i

try:
    while(True):
        n = adc()
        cifr = dec2bin(n)
        print ('Цифровое = ', cifr, 'Аналоговое = ', n)


finally: 
    GPIO.output(dac, 0)
    GPIO.cleanup()
