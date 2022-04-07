import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
cad_reverse = [10, 9, 11, 5, 6, 13 , 19, 26]
array = [0, 0 ,0 ,0 ,0 ,0 ,0 ,0]
comp = 4
troyka = 17

GPIO.setup (dac, GPIO.OUT)
GPIO.setup (troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup (comp, GPIO.IN)
def dec2bin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]


def adc():
    for i in 7, 6, 5, 4, 3, 2, 1, 0:
        GPIO.output (cad_reverse[i], 1)
        array[7 - i] = 1
        time.sleep(0.007)

        if (GPIO.input(comp) == 0):
            GPIO.output (cad_reverse[i], 0)
            array[7 - i] = 0

    return i

try:
    while (1):
        v = 0
        array = [0, 0 ,0 ,0 ,0 ,0 ,0 ,0]
        GPIO.output(dac, array)
        adc()
        for j in range(8):
            v += array[j]*(2**(7-j))
            volt = v * 3.3 / 256
        print(dec2bin(v), v, " ", volt)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
