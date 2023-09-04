from Modul.conveyor import *
from Modul.servo import *
from Modul.tele import *
import time

if __name__ == "__main__":
    while (True):
        main_conveyor()
        time.sleep(1)
        main_servo()
        time.sleep(1)
        main_tele()
        time.sleep(1)