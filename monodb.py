import pymongo


""""
db = client.test
collection = db["my_collection"]

# insert a document
result = collection.insert_one({"name": "John Doe", "age": 30})
print(result.inserted_id)

# query the database
result = collection.find_one({"name": "John Doe"})
print(result)"""




# to connect to the mongodb database
client = pymongo.MongoClient("mongodb+srv://THARUN:Tharun9705@cluster0.mjujmq5.mongodb.net/?retryWrites=true&w=majority")

# to create database
#db=client.tharun

# or you also create database like this also
db=client["test"]

# to create a table
table=db["my_collection"]

# to insert  one document(dictionary) into table use insert one
#result = table.insert_one({"SUBJECTS":["meachinelerning"],"CREDITS":[6,12,12,9,6,6]})

# to insert multiple documents use insert_many store the dictionary inside list
"""result = table.insert_many([
{"SUBJECTS":["meachinelerning","database","operatingsystem","webprogramming","devise_and_curicts","system_syscurity"],"CREDITS":[6,12,12,9,6,6]},
{"SUBJECTS":["meachinelerning","database","operatingsystem","webprogramming","devise_and_curicts","system_syscurity"],"CREDITS":[6,12,12,9,6,6]},
{"SUBJECTS":["meachinelerning","database","operatingsystem","webprogramming","devise_and_curicts","system_syscurity"],"CREDITS":[6,12,12,9,6,6]}
])"""





#print(result.inserted_id)




# query to get a paticular insatance from the data table
#result = table.find_one({"SUBJECTS":["meachinelerning","database","operatingsystem","webprogramming","devise_and_curicts","system_syscurity"]})
#print(result)

#query to get all the data from the table

result=table.find()

# to get condiction releated data use this

#result =table.find({"SUBJECTS":["meachinelerning"]})

# query to extract data with the condiction use $in , in mongobd or is reffered as $in

#result=table.find({"CREDITS":{'$in':[[6,12,12,9,6,6],[6]]}})

# in mongodb the >,>=,<,<=,==, symbols are not used insted ,we use $gt,$ge,$lt,$le

#result=table.find({"CREDITS": {'$in':[[6,12,12,9,6,6],[6]]} ,"SUBJECTS":"meachinelerning"})

# to update the data ,use  update_one (this will update a single record the one which it  finds frist  with the matching condition)
# or update_all( this will update all the records with the matching condition )
# USE $set to update to the new one

#result=table.update_one({"SUBJECTS":"meachinelerning"},{"$set":{"SUBJECTS":"MEACHINELEARNING"} })
#result=table.update_many({"SUBJECTS":"meachinelerning"},{"$set":{"SUBJECTS":"MEACHINELEARNING"} })


# delete one single reacord with the matching condition use delete_one
#result=table.delete_one({"SUBJECTS":"MEACHINELEARNING"})

# delete many records with the condition use delete_many
#result=table.delete_many({"SUBJECTS":"MEACHINELEARNING"})

result=table.find()
for i in result:
    print(i)



