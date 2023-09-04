import pymongo # meng-import library pymongo yang sudah kita install

password = '8lpz9drmblL8ylKI'
uri = f"mongodb+srv://dismtzking:{password}@cluster0.9vjmeo5.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(uri)
db = client['test_database'] # ganti sesuai dengan nama database kalian
my_collections = db['test_collection'] # ganti sesuai dengan nama collections kalian
# Data yang ingin dimasukkan
murid_1 = {'nama':'John Doe','Jurusan':'IPS','Nilai':90}
murid_2 = {'nama':'Jane Doe', 'Jurusan':'IPA','Nilai':85}
results = my_collections.insert_many([murid_1,murid_2])
print(results.inserted_ids) # akan menghasilkan ID dari data yang kita masukkan