""" Given a neighbourhood at run-time (e.g., using command line prompt or via an application parameter) find the average rental cost/night? """

from pymongo import MongoClient

client = MongoClient()
db = client["A5db"]

def runQuery(hood):
    # Create or open the collection in the db
    listings_collection = db["listings"]

    """ Given a neighbourhood at run-time (e.g., using command line prompt or via an application parameter) find the average rental cost/night? """
    results = listings_collection.aggregate([ 
        {
            # Find listings with neighborhood
            "$group" : { "_id" : "$neighbourhood", "average" : {"$avg": "$price"} }
        },
        {
            "$match" : {"_id" : hood}
        }
    ])
    for row in results:
        print(row)
        

def main():
    # List collection names.
    collist = db.list_collection_names()
    if "listings" in collist:
        print("The collection exists.")
        
    runQuery("Downtown")

main()