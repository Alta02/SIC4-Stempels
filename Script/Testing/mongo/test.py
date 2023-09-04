import pymongo

# Membuat koneksi dengan MongoDB
client = pymongo.MongoClient("mongodb://103.247.12.11:27017/")

# Mengakses database dan koleksi yang sesuai
db = client["test"]
collection = db["mydata"]

# Membaca data dari sensor ultrasonik
distance = "lutfie"

# Membuat objek data
data = {
    "distance": distance
}

# Mengirim data ke MongoDB
collection.insert_one(data)

# Menutup koneksi
client.close()
