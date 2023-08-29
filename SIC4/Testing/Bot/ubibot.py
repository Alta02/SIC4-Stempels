import board
import adafruit_dht
import time
import requests

# Set up the DHT11 sensor
dht_pin = board.D17  # Set the pin where the DHT11 data pin is connected to GPIO 17
dht_sensor = adafruit_dht.DHT11(dht_pin)

# Ubidots configuration
UBIDOTS_TOKEN = "BBFF-xNOFNDrbkUqOhvwOEz4qQ1qrQ45wXJ"
DEVICE_LABEL = "sensors"
TEMP_VARIABLE_LABEL = "temperature"  # Variable label for temperature
HUMIDITY_VARIABLE_LABEL = "Kelembapan"  # Variable label for humidity

def send_to_telegram(message):
    apiToken = '6138535917:AAHzvm8z4VgoTCczWCDXMJaX_b8HdV9oGus'
    chatID = '1988436146'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

def send_data_to_ubidots(variable_label, value):
    url = f"https://industrial.api.ubidots.com/api/v1.6/devices/{DEVICE_LABEL}/{variable_label}/values"
    headers = {"Content-Type": "application/json", "X-Auth-Token": UBIDOTS_TOKEN}
    payload = {"value": value}

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        print(f"Data for {variable_label} sent to Ubidots successfully!")
    else:
        print(f"Failed to send data for {variable_label} to Ubidots")

def main():
    try:
        while True:
            try:
                # Read temperature and humidity from the DHT11 sensor
                temperature = dht_sensor.temperature
                Kelembapan = dht_sensor.humidity
                print('Temperature: {:.1f}°C, Humidity: {:.1f}%'.format(temperature, Kelembapan))

                # Send temperature and humidity data to Ubidots
                send_data_to_ubidots(TEMP_VARIABLE_LABEL, temperature)
                send_data_to_ubidots(HUMIDITY_VARIABLE_LABEL, Kelembapan)
                print("==========================================================")

                # Send temperature data to Telegram
                if temperature > 27:  # Adjust the threshold temperature as needed
                    pesan = f"⚠️ Waktunya Menggoreng ! temperature saat ini: {temperature:.2f}°C"
                    send_to_telegram(pesan)

            except RuntimeError as e:
                print('Error reading from sensor:', e)

            time.sleep(1)  

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
