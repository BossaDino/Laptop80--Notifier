import psutil
from win11toast import toast
import pystray
from PIL import Image
import time
import sys

battery = psutil.sensors_battery()
percentage = battery.percent
state = 1
antiSpam = 0


# Windows tray icon on-click
def trayClick(icon, query):
    if str(query) == "Exit":
        icon.stop()


# Windows tray icon configuration
image = Image.open("battery.ico")
icon = pystray.Icon("battery", image, "Battery Reader", menu=pystray.Menu(
    pystray.MenuItem("Exit", trayClick)
))
icon.run_detached()


while state == 1:
    print(1)
    # Check to see if it is charging
    while battery.power_plugged == 1 and state == 1:
        # Check if battery is > 80%
        if percentage >= 80:
            antiSpam = antiSpam + 1
            toast("Assistant", "Battery is at or above 80%!", scenario='incomingCall')
            print("waiting1")
            state = 0
        else:
            time.sleep(30)
            percentage = battery.percent
        break

    battery = psutil.sensors_battery()
    # Prevent getting stuck when plugged out
    if battery.power_plugged == 0:
        state = 0

    # Wait after notifying / Wait before monitoring again
    while state == 0:
        # Get updated information
        tempPower = psutil.sensors_battery()
        tempPower = tempPower.power_plugged

        if tempPower == 1:
            state = 1
            time.sleep(60)
            break
        else:
            print("waiting")
            time.sleep(60)

    # Exit if notif has been received twice to avoid spam
    if antiSpam >= 2:
        sys.exit()


# If this runs, you somehow broke it
toast("Assistant", "Battery checker turned off")
