import time
import threading
from pynput.mouse import Button, Controller, Listener as mouseListener
from pynput.keyboard import Listener, KeyCode
import random



button = Button.left
start_stop_key = KeyCode(char='b')
exit_key = KeyCode(char='z')

print('Start Stop Key:' + str(start_stop_key))
print('Exit Key:' + str(exit_key))




class ClickMouse(threading.Thread):
    def __init__(self, button):
        super(ClickMouse, self).__init__()
        self.button = button
        self.running = False
        self.program_running = True
        self.flag = False

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.press(self.button)
                generateNumber = random.uniform(0.032473, 0.0410444)
                time.sleep(float(generateNumber))
                mouse.release(self.button)
                generateNumber = random.uniform(0.03855655, 0.04294455)
                time.sleep(float(generateNumber))


mouse = Controller()
click_thread = ClickMouse(button)
click_thread.start()



#Old script to use keyboard input to start and stop.
def on_press(key):
    if key == start_stop_key:
        if not click_thread.running:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()

def on_release(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    
"""

def on_press(key):
    if key == start_stop_key:
        if click_thread.flag:
            click_thread.flag = False
        else:
            click_thread.flag = True
    elif key == exit_key:
        click_thread.exit()
        listener.stop()

def on_click(x, y, button, pressed):
    if click_thread.flag == True:
        if pressed:
            if not click_thread.running:
                click_thread.start_clicking()
        else:
            if click_thread.running:
                click_thread.stop_clicking()

with mouseListener(on_click=on_click) as mouseListener:
    mouseListener.join()

"""

with Listener(on_press=on_press) as listener:
    listener.join()


