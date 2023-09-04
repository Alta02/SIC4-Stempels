import requests
import adafruit_dht
import board
import time

def send_to_telegram(message):
    apiToken = '6138535917:AAHzvm8z4VgoTCczWCDXMJaX_b8HdV9oGus'
    # chatID = '5214657416'
    chatID = '1988436146'

    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

dht_pin = board.D17
dht_sensor = adafruit_dht.DHT11(dht_pin)

putaran = 0

try:
    while True:
        try:
            temperature = dht_sensor.temperature
            humidity = dht_sensor.humidity
            if temperature is not None and humidity is not None:
                print('Temperature: {:.1f}°C, Humidity: {:.1f}%'.format(temperature, humidity))
                if temperature > 27:  # Adjust the threshold temperature as needed
                    pesan = f"⚠️ Waktunya Menggoreng ! temperature saat ini: {temperature:.2f}°C"
                    send_to_telegram(pesan)
                    putaran += 1
                    print(f"Telah mengirim pesan sebanyak {putaran} kali")
                    print("========================================================")
                    
            else:
                print('Data not available.')
        except RuntimeError as e:
            print('Error reading from sensor:', e)

        time.sleep(1)

except KeyboardInterrupt:
    pass
