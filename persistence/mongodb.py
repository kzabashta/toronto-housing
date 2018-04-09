from pymongo import MongoClient
cl = MongoClient()
coll = cl["local"]["solds"]

def insert_listing(listing):
    coll.update({'_id':listing['_id']}, listing, True)