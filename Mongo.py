from pymongo import MongoClient

client = MongoClient("mongodb+srv://Renato:Renato123@cluster0.551n6lo.mongodb.net/?retryWrites=true&w=majority")
db = client.test

systems = db['System']
names = db['Titles']

def insertDiv(l, title, description):
    resp = systems.insert_many(l)
    # Document is a tuple
    document = ("John", 30, "New York")

    # Convert the tuple to a dictionary
    document = {"title": title, "description": description, "ids": resp.inserted_ids}
    names.insert_one(document)
    #names.insert_one(title, description, resp.inserted_ids)

def getNames():
    return names.find()

def getSysem(id_list):
    return list(systems.find({'_id': {'$in': id_list}}))

def listToDict(lis):
    dic = {}
    for l in lis:
        dic[str(l['id'])] = l
    return dic
