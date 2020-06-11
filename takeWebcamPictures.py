import os
from datetime import datetime
import time

run = input("Start? y/n > ")
minBetweenImages = float(input("Photo every x min: x = "))

try:
    while True:
        if run == "y":
            currenttime = str(datetime.now())
            currenttimeshort = currenttime[0:19]
            currenttimeshort = currenttimeshort.replace(" ", "_")
            os.system('fswebcam -r 1280x720 --no-banner ./images/image_' + currenttimeshort + '.jpg')
            time.sleep(minBetweenImages*60)
except KeyboardInterrupt:
    pass