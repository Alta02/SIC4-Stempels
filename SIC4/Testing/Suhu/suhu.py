from gpiozero import DHT11

# Connect the DHT sensor to the appropriate GPIO pin
dht_sensor = DHT11(17)  # GPIO 17

# Read the sensor data
humidity = dht_sensor.humidity
temperature = dht_sensor.temperature

# Print the sensor data
print(f"Humidity: {humidity}%")
print(f"Temperature: {temperature}°C")
