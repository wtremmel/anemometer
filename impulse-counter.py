import time
from machine import Pin, ADC

hall = Pin(0,Pin.IN,Pin.PULL_UP)

prev = 0
count = 0

lastRead = time.time()

while True:
    v = hall.value()
    if v != prev:
        if v == 0:
            count += 1
            print(count)
        prev = v
    if (time.time() >= lastRead+60):
        print("Impulses per minute: ",count)
        lastRead = time.time()
        count = 0