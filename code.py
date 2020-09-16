from adafruit_circuitplayground import cp
import time
import random

def displaypoints(points):
    """displays points in blue"""
    cp.pixels[0:points] = [(0, 255, 0)] * points
    time.sleep(2)
    cp.pixels.fill((0, 0, 0))

def displaylives(lives):
    """displays lives in red"""
    cp.pixels[0:lives] = [(255, 0, 0)] * lives
    time.sleep(2)
    cp.pixels.fill((0, 0, 0))

def blinkpixel(num, color):
    """blinks a selected pixel defined by num, with color in RGB format"""
    for i in range(3):
        cp.pixels[num] = color
        time.sleep(0.2)
        cp.pixels[num] = (0, 0, 0)
        time.sleep(0.2)

cp.red_led = True
time.sleep(1)
cp.red_led = False

cp.pixels.brightness = 0.02
delaystart = 0.06

while True:
    points = 0
    lives = 3
    inc = 0
    delay = delaystart
    winflag = 0

    displaylives(lives)

    while True:
        print("Delay: ", delay)
        while True:
            """
            pixels lighting up in circles
            """
            cp.pixels[inc % 10] = ((0, 0, 255))
            if cp.button_a:
                break
            time.sleep(delay)
            if cp.button_a:
                break
            cp.pixels[inc % 10] = ((0, 0, 0))
            inc += 1

        if inc % 10 == 2:
            blinkpixel(inc % 10, (0, 255, 0))
            points += 1
            displaypoints(points)
            delay *= 0.93
            if points == 10:
                winflag = 1
                break
        else:
            blinkpixel(inc % 10, (255, 0, 0))
            lives -= 1
            if lives == 0:
                cp.pixels.fill((255, 0, 0))
                time.sleep(2)
                break
            displaylives(lives)

    cp.pixels.fill((0, 0, 0))
    time.sleep(2)
    if winflag == 1:
        delaystart *= 0.9