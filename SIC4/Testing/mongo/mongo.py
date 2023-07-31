from pymongo.mongo_client import MongoClient

password = "08b0Qt32zhbwArYG"
uri = f"mongodb+srv://els14029:{password}@sicbatch4.ihzahom.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)