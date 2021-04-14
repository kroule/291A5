""" Given a neighbourhood at run-time (e.g., using command line prompt or via an application parameter) find the average rental cost/night? """

from pymongo import MongoClient
import time

client = MongoClient()
db = client["A5db"]
start_time = time.time()

def runQuery():
    # Create or open the collection in the db
    listings_collection = db["listings"]
    user = str(input('enter neighbourhood: '))

    """ Given a neighbourhood at run-time (e.g., using command line prompt or via an application parameter) find the average rental cost/night? """
    results = listings_collection.aggregate([ 
        {
            # Find listings with neighborhood
            "$group" : { "_id" : "$neighbourhood", "average" : {"$avg": "$price"} }
        },
        {
            "$match" : {"_id" : user}
        }
    ])
    for row in results:
        print(row)
        

def main():
    # List collection names.
    collist = db.list_collection_names()
    if "listings" in collist:
        print("The collection exists.")
        
    runQuery()

main()
print("Program runtime:  %s seconds" % (time.time() - start_time))