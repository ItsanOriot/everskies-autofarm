import mouse
import keyboard
import win32api
import random
import time
keyboard.wait('esc')
while True:
    state = win32api.GetKeyState(0x02)
    if state < 0:
        quit()
    else:
        x = random.randint(415, 1190)
        y = random.randint(223, 1060)
        print(str(x) + " " + str(y))
        mouse.move(x, y, duration = 0.002)
        mouse.click()
