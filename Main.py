from pynput import keyboard
import time
from gpiozero import CamJamKitRobot

robot = CamJamKitRobot()

def on_press(key):
    try:
        Pressed = key.char
    except AttributeError:
        Pressed = key

    if Pressed == "w":
        print("Robot forward")
        robot.forward()
        time.sleep(0.1)

    if Pressed == "s":
        print("Robot back")
        robot.reverse()
        time.sleep(0.1)

    if Pressed == "a":
        print("Robot left")
        robot.left()
        time.sleep(0.1)

    if Pressed == "d":
        print("Robot Right")
        robot.right()
        time.sleep(0.1)

def on_release(key)
    print(format(key))
    if key == keyboard.Key.esc:
        robot.stop()
        return False

# Collect events until released
#with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
#    listener.join()

with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
