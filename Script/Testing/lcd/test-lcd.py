import smbus2
import time

# Define I2C address of the LCD module (use the address you detected)
lcd_address = 0x27

# Define registers for data and control
lcd_data_register = 0x40
lcd_control_register = 0x00

# Create an I2C bus instance
bus = smbus2.SMBus(1)  # Use 0 on older Raspberry Pi boards

# Initialize LCD
def lcd_init():
    # Initialize your LCD based on your library's initialization code
    # Example: You might need to send specific initialization commands here
    pass

# Send command to LCD
def lcd_command(cmd):
    bus.write_byte_data(lcd_address, lcd_control_register, cmd)
    time.sleep(0.005)  # Delay after sending a command

# Send data to LCD
def lcd_data(data):
    for char in data:
        bus.write_byte_data(lcd_address, lcd_data_register, ord(char))
        time.sleep(0.005)  # Delay after sending each character

# Main program
try:
    lcd_init()
    lcd_command(0x01)  # Clear the screen
    lcd_command(0x80)  # Set cursor to the first line
    lcd_data("Hello,")
    lcd_command(0xC0)  # Set cursor to the second line
    lcd_data("Raspberry Pi!")

except KeyboardInterrupt:
    pass
finally:
    bus.close()
