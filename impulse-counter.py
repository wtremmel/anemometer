import time
from machine import Pin

hall = Pin(0,Pin.IN,Pin.PULL_UP)
led = Pin(25,Pin.OUT)

topic = "/Chattenweg5/2OG-Loggia/wind"
prev = 0
count = 0
interval = 60

lastRead = time.time()

while True:
    v = hall.value()
    if v != prev:
        if v == 0:
            count += 1
            led.high()
            # print(count)
        else:
            led.low()
        prev = v
    if (time.time() >= lastRead + interval):
        print(topic,count)
        lastRead = time.time()
        count = 0