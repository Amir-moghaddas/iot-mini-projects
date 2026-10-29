from machine import Pin, PWM
from time import sleep, sleep_us
import time

trig_pin = Pin(16, Pin.OUT)
echo_pin = Pin(4, Pin.IN)

buzzer_pin = Pin(13, Pin.OUT)
buzzer = PWM(buzzer_pin)

def measure_distance():

    trig_pin.value(0)
    sleep_us(2)
    trig_pin.value(1)
    sleep_us(10)
    trig_pin.value(0)

    while echo_pin.value() == 0:
        pass
    start_time = time.ticks_us()

    while echo_pin.value() == 1:
        pass
    end_time = time.ticks_us()

    duration = end_time - start_time

    if duration > 0:
        res = (duration * 0.0343) / 2
        return res
    return None

def bugh():
    buzzer.freq(500)
    buzzer.duty_u16(3000)

def bugh_off():
    buzzer.duty_u16(0)

while True:
    distance = measure_distance()
    print(distance)                      
    if distance is not None and distance <= 200:
        bugh()
    else:
        bugh_off()
    sleep(0.1)
