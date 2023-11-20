import machine
from machine import Pin
import utime


class Button:
    def __init__(self, button_id, label, callback):
        def interrupt_handler(pin):
            time = utime.ticks_ms()
            if (time - self.last_pressed_time) > 200:  # 200ms debounce
                self.last_pressed_time = time
                callback(button_id, label)

        self.pin = Pin(button_id, Pin.IN)
        self.pin.irq(trigger=Pin.IRQ_RISING,
                     handler=interrupt_handler)
        self.last_pressed_time = utime.ticks_ms()
        self.id = button_id
        self.label = label


class Keyboard:
    def __init__(self, button_ids, button_labels):
        def cb(button_id, label):
            self.notify_observers(button_id, label)

        self.observers = []
        self.buttons = []
        for i in range(len(button_ids)):
            self.buttons.append(Button(button_ids[i], button_labels[i], cb))

    def connect(self, observer):
        self.observers.append(observer)

    def notify_observers(self, button_id, label):
        for obs in self.observers:
            obs.callback(button_id, label)

    def disconnect(self, observer):
        self.observers.remove(observer)


class KeyboardObserver:
    def __init__(self, callback):
        self.callback = callback

    def callback(self, button_id, label):
        self.callback(button_id, label)
