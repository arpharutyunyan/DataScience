from pymongo import MongoClient


CLIENT = MongoClient('localhost', 27017)
DB = CLIENT['db_link']
COLLECTION_PAGES = DB['links']
COLLECTION_WORDS = DB['words']

def insert_pages (link):
    # insert values into collection
    col = COLLECTION_PAGES.insert_one(link)
    # keep id for saving html file
    
    return col.inserted_id

def insert_words (data):
    COLLECTION_WORDS.insert_one(data)

def find_link(path):
    #  get count of given path
    cursor = COLLECTION_PAGES.count_documents({'path': path}) 
    
    return cursor


def getting_ids ():
    # return list of all ids
    values = COLLECTION_PAGES.find ().distinct('_id')
    
    return values

def get_path (id):
    # list path for that id
    path = COLLECTION_PAGES.find({'_id': id}).distinct('path')
  
    return path[0]




