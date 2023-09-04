import serial
import pynmea2

# Konfigurasi modul GPS
serial_port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1.0)

try:
    while True:
        # Baca data dari modul GPS
        line = serial_port.readline().decode("utf-8")
        if line.startswith("$GPGGA"):
            msg = pynmea2.parse(line)
            latitude = msg.latitude
            longitude = msg.longitude
            altitude = msg.altitude

            print("Latitude:", latitude)
            print("Longitude:", longitude)
            print("Altitude:", altitude)
            print("===================")

except KeyboardInterrupt:
    print("Program dihentikan melalui keyboard interrupt")
finally:
    # Menutup port serial GPS
    serial_port.close()
