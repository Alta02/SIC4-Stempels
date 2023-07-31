import pymongo # meng-import library pymongo yang sudah kita install

password = "08b0Qt32zhbwArYG"
uri = f"mongodb+srv://els14029:{password}@sicbatch4.ihzahom.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)

db = client['mentor-rusdiansyah'] # ganti sesuai dengan nama database kalian
#my_collections = db['mentor'] # ganti sesuai dengan nama collections kalian
# my_collections = db['183'] # ganti sesuai dengan nama collections kalian
my_collections = db['arjuna'] # ganti sesuai dengan nama collections kalian
# my_collections = db['asteria'] # ganti sesuai dengan nama collections kalian
# my_collections = db['jayamahe'] # ganti sesuai dengan nama collections kalian
# my_collections = db['quantumania'] # ganti sesuai dengan nama collections kalian
# my_collections = db['stemga'] # ganti sesuai dengan nama collections kalian
# my_collections = db['tothreetwo'] # ganti sesuai dengan nama collections kalian

# Data yang ingin dimasukkan
murid_1 = {'nama':'Lutfie','Jurusan':'TKJ','Nilai':90}
murid_2 = {'nama':'Nero', 'Jurusan':'RPL','Nilai':85}

results = my_collections.insert_many([murid_1,murid_2])
print(results.inserted_ids) # akan menghasilkan ID dari data yang kita masukkan