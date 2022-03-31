import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
res = [0, 0, 0, 0, 0, 0, 0, 0]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup (dac, GPIO.OUT)
GPIO.setup (leds, GPIO.OUT)
GPIO.setup (troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup (comp, GPIO.IN)

def dec2bin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]

def adc2 ():
    while (True):
        for i in [0, 1, 2, 3, 4, 5, 6, 7]:
            GPIO.output(dac[i], 1)
            time.sleep (0.01)
            if GPIO.input(comp) == 0:
                GPIO.output(dac[i], 1)
                res[i] = 1
            else:
                GPIO.output(dac[i], 0)
                res[i] = 0
        return GPIO.input(troyka)

def bin2dec(res):
    for i in range (8):
        num = res[i]*2^(i-1)
    return num

num = bin2dec(res)
# print (num)

def adc1 (n):
    while (True):
        for i in range(num):
            GPIO.output(leds, dec2bin(num))
            
            if GPIO.input(comp) == 0:
                return i


try:
    while(True):
        n = adc2 ()
        ans = adc1 (n)

        print ('Цифровое = ', res, 'An = ', n)
        GPIO.output(dac, 0)


finally: 
    GPIO.output(dac, 0)
    GPIO.cleanup()
