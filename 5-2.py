import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
res = [0, 0, 0, 0, 0, 0, 0, 0]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup (dac, GPIO.OUT)
GPIO.setup (troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup (comp, GPIO.IN)

def dec2bin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]

def bin2dec(res):
    for i in range (8):
        num = res[i-1]*2^(i-1)
    return num


def adc ():
    while (True):
        for i in [0, 1, 2, 3, 4, 5, 6, 7]:
            GPIO.output(dac[i], 1)
            time.sleep (0.01)
            if GPIO.input(comp) == 0:
                GPIO.output(dac[i], 1)
                res[i] = 1
            else:
                res[i] = 0
        return bin2dec(res)



try:
    while(True):
        n = adc()
        print ('Цифровое = ', res, 'An = ', n)
        GPIO.output(dac, 0)


finally: 
    GPIO.output(dac, 0)
    GPIO.cleanup()
