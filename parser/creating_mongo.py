from pymongo import MongoClient

CLIENT = MongoClient('localhost', 27017)
DB = CLIENT['db_link']
COLLECTION = DB['links']

def mongo_connection (link):
    # insert values into collection
    col = COLLECTION.insert_one(link)
    # keep id for saving html file
    
    return col.inserted_id


def find_link(path):
    #  get all values with these path
    cursor = COLLECTION.count_documents({'path': path}) 
    
    return cursor


def getting_ids ():
    # return list of all ids
    values = COLLECTION.find ().distinct('_id')
    
    return values

def get_path (id):
    # list path for that id
    path = COLLECTION.find({'_id': id}).distinct('path')
  
    return path[0]




