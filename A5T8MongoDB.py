""" Given a listing_id at run-time (e.g., using command line prompt or via an application parameter) find the host_name, rental_price and the most recent review for that listing. """

from pymongo import MongoClient
import time

client = MongoClient()
db = client["A5db"]
start_time = time.time()

def runQuery(listing_id):
    # Create or open the collection in the db
    listings_collection = db["listings"]

    """ Given a listing_id at run-time (e.g., using command line prompt or via an application parameter) find the host_name, rental_price and the most recent review for that listing. """
    results = listings_collection.aggregate([
        {
            "$match" : { "id": listing_id}
        },
        {
            "$unwind" : "$reviews"
        }, 
        {
            "$sort" : {"reviews.date" : -1 }
        },
        {
            "$limit" : 1
        },
        {
            "$project" : { "host_name" : 1, "price" : 1, "reviews.comments" : 1 }
        }
    ])
    for row in results:
        print(row)
        

def main():
    # List collection names.
    collist = db.list_collection_names()
    if "listings" in collist:
        print("The collection exists.")
        
    runQuery(10080)

main()
print("Program runtime:  %s seconds" % (time.time() - start_time))