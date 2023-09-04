import requests

# API token dari Ubidots
api_token = 'BBFF-kTSkgX5Sa1iYOP1V0WwuMdCdP5UnYo'

# URL endpoint untuk mengakses variabel di Ubidots
device_label = 'sensors'  # Ganti dengan nama perangkat Anda di Ubidots
variable_label = 'gps'

url = f'https://industrial.api.ubidots.com/api/v1.6/devices/{device_label}/{variable_label}'

# Koordinat yang akan dikirim
latitude = -6.2088
longitude = 106.8456

# Format data ke dalam JSON
gps_data = {
    "latitude": latitude,
    "longitude": longitude
}

headers = {
    "X-Auth-Token": api_token,
    "Content-Type": "application/json"
}

try:
    # Kirim data GPS ke Ubidots
    gps_response = requests.post(url, json=gps_data, headers=headers)
    if gps_response.status_code == 201:
        print("Data GPS terkirim ke Ubidots:", gps_response.content)
    else:
        print("Gagal mengirim data GPS:", gps_response.content)

except Exception as e:
    print("Terjadi kesalahan:", e)
