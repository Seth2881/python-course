from pynput import keyboard
import pyautogui
import threading
import time as t

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

running = False

def click_loop():
    n = 0
    while running:
        n += 1
        pyautogui.click()  # plus rapide que doubleClick
        if n%10==0:
            t.sleep(0.001)


def on_press(key):
    global running
    if key == keyboard.Key.f6:
        running = not running
        if running:
            threading.Thread(target=click_loop, daemon=True).start()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
