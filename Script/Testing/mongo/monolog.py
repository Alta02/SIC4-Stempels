import pymongo
password = 'Kn5sc2bj7CpSV318'
uri = f"mongodb+srv://altanlanero:{password}@hello.9czit1o.mongodb.net/?retryWrites=true&w=majority"
#uri = f"mongodb+srv://els14029:{password}@sicbatch4.ihzahom.mongodb.net/?retryWrites=true&w=majority"

#Create a new client and connect to the server
client = pymongo.MongoClient(uri)
db = client['TEST'] # ganti sesuai dengan nama database kalian
my_collections = db['KOELS'] # ganti sesuai dengan nama collections kalian
# Data yang ingin dimasukkan
murid_1 = {'nama':'HI','Jurusan':'IPS','Nilai':200}
murid_2 = {'nama':'SYAP', 'Jurusan':'IPA','Nilai':90}
results = my_collections.insert_many([murid_1,murid_2])
print(results.inserted_ids) # akan menghasilkan ID dari data yang kita masukkan