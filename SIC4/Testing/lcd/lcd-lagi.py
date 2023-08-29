import random
import time
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD

# List of Indonesian names
indonesian_names = ["Adi", "Budi", "Citra", "Dewi", "Endang", "Fitri"]

lcd = LCD()

def safe_exit(signum, frame):
    lcd.clear()
    exit(1)

try:
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)
    
    while True:
        lcd.clear()  # Clear the display
        random_name = random.choice(indonesian_names)
        lcd.text("Halo,", 1)
        lcd.text(random_name, 2)
        time.sleep(2)  # Wait for 2 seconds

except KeyboardInterrupt:
    pass
finally:
    lcd.clear()
