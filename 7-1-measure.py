import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as ptl

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17
data = []

GPIO.setmode(GPIO.BCM)

GPIO.setup (dac, GPIO.OUT)
GPIO.setup (leds, GPIO.OUT)
GPIO.setup (troyka, GPIO.OUT)
GPIO.setup (comp, GPIO.IN)


def dec2bin(n):
    return [int(i) for i in bin(int(n))[2:].zfill(8)]

def bin2dec(list):
    w = 128
    val = 0
    for i in range(0, 8):
        val += w * list[i]
        w /= 2
    return val


def adc():
    list = [0] * 8
    for i in range(0,8):
        list[i] = 1
        GPIO.output (dac, list)
        time.sleep (0.005)

        if (GPIO.input(comp) == 0):
            list[i] = 0

    return bin2dec(list)

try:

    while (1):
        rem_time_strt = time.time()
        GPIO.output(17, 1)

        val = 0

        while (val <= 255*0.6):
            val = adc()
            data.append(val)

            print ("volt = {:.2f} V".format(val * 3.3 / 256))

            GPIO.output (leds, dec2bin(val))
            
        rem_time_end = time.time ()
        time_ism = rem_time_end - rem_time_strt

        val = 255
        GPIO.output(17, 0)

        while(val >= 255*0.05):  
            val = adc()
            data.append(val)

            print ("volt = {:.2f} V".format(val * 3.3 / 256))

            GPIO.output (leds, dec2bin(val))
            
        time_end = time.time ()
        time_all = time_end - rem_time_strt
        break


finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()

ptl.plot(data)
ptl.show()

str_data = [str(item) for item in data]

with open("7-1-data.txt", "w") as outfile:
    outfile.write("\n".join(str_data))

with open("7-1-settings.txt", "w") as settfile:
    settfile.write("discr = s\n".format(time_ism / len(data)))
    settfile.write("q step = {:.5f} V\n".format(3.3/256))
    settfile.write("all  time = {:.5f} sec\n".format(time_all))

