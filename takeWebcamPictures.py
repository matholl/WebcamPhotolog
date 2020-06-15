import os
from datetime import datetime
import time


def time_to_min(hour, minute):
    return hour*60+minute

run = input("Start? y/n > ")
minBetweenImagesDay = float(input("Photo every x min during daytime: x = "))
minBetweenImagesNight = float(input("Photo every y min during nighttime: y = "))

try:
    while True:
        if run == "y":
            

            timenow = time.localtime()

            start_daytime = time_to_min(7, 30)
            end_daytime = time_to_min(22, 00)
            current_time = time_to_min(timenow.tm_hour, timenow.tm_min)

            currenttime = str(datetime.now())
            currenttimeshort = currenttime[0:19]
            currenttimeshort = currenttimeshort.replace(" ", "_")

            if current_time >= start_daytime and current_time <= end_daytime:
                os.system('fswebcam -D 2 -S 20 --set brightness=30% -r 1280x720 --no-banner ./images/image_' + currenttimeshort + '.jpg')
                time.sleep(minBetweenImagesDay*60)
            else:
                os.system('fswebcam -D 2 -S 20 --set brightness=30% -r 1280x720 --no-banner ./images/image_' + currenttimeshort + '.jpg')
                if ((start_daytime - current_time) < minBetweenImagesNight*60):
                    time.sleep((start_daytime - current_time)*60)
                else:
                    time.sleep(minBetweenImagesNight*60)
            
            
except KeyboardInterrupt:
    pass