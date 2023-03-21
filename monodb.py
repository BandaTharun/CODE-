import pymongo

client = pymongo.MongoClient("mongodb+srv://THARUN:Tharun9705@cluster0.mjujmq5.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


