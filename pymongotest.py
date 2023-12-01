from pymongo import MongoClient
import pprint


# Replace 'your_connection_string' with your MongoDB connection string
client = MongoClient('mongodb://localhost:27017/')

# Access a specific database
db = client.rptotorials

# Access a specific collection within the database
collection = db.tutorial

#Define a document


all_documents = collection.find()
for document in all_documents:
    print(document)

    
single_document = collection.find_one()
print(single_document)


tutorial1={"title": "Working with JSON Data in Python","author":"Lucas","contributors":["Aldren","Dan","Khaing"],"url":"khaing@frontiir"}
result=collection.insert_one(tutorial1)

print(result)
# # result = collection.delete_many(tutorial1)
print(f"Inserted document with _id: {result.inserted_id}")

tutorial2 = {"title": "Python's Requests Library (Guide)", "author": "Alex","contributors": ["Aldren","Brad","Joanna"],  "url": "https://realpython.com/python-requests/"}

tutorial3 = {"title": "Object-Oriented Programming (OOP) in Python 3","author": "David","contributors": ["Aldren","Joanna","Jacob"],"url": "https://realpython.com/python3-object-oriented-programming/"}

new_result =collection.insert_many([tutorial2, tutorial3])
print(new_result)

print(f"Multiple tutorials: {new_result.inserted_ids}")
for doc in collection.find():
    pprint.pprint(doc)


jon_tutorial = collection.find_one({"author":"Jon"})
pprint.pprint(jon_tutorial)



# Perform operations on the collection
# For example, insert a document
# document = {"key": "value"}
# collection.insert_one(document)

# Close the connection when done
client.close()
