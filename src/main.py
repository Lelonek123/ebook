import machine
from machine import Pin, Timer
from lib.keyboard import Keyboard, KeyboardObserver


def obs_cb(button_id, label):
    print("ID: ", button_id, " Label: ", label)


class State:
    MAIN_MENU = 1
    READER = 2


def blink(_timer):
    led.value(not led.value())


led = Pin(25, Pin.OUT)
timer = Timer(-1)
timer.init(period=1000, mode=Timer.PERIODIC, callback=blink)


keyboard = Keyboard([21, 22, 26, 27, 28], ["OK", "UP", "DOWN", "LEFT", "RIGHT"])
obs = KeyboardObserver(obs_cb)
keyboard.connect(obs)




# TODO:
#  - import nanogui library and run tests
#  - implement keyboard using observer pattern
#  - implement reader
#  - implement menu view
#  - button debounce with timer


# global state
#
# while True:
#     switch state
#         case s1:
#             init_s1() # registered callbacks that can change state
#
#             while state == s1:
#                 sleep(60Hz)
#                 pass
#
#             clear_state_s1()
#
#         case s2:
#             init_s2() # registered callbacks that can change state
#
#             while state == s1:
#                 sleep(60Hz)
#                 pass
#
#             clear_state_s2()

from lib.color_setup import ssd

print("Draw")
ssd.line(20, 20, 100, 100, 0xff)
ssd.text("test", 0, 0, 0xff)
ssd.show()
