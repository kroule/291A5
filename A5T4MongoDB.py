""" Find which listed property(ies) has(have) not received any review, order them by listing_id and output the top 10? """

from pymongo import MongoClient
import time 

client = MongoClient()
db = client["A5db"]
start_time = time.time()

def runQuery():
    # Create or open the collection in the db
    listings_collection = db["listings"]

    """ Find which listed property(ies) has(have) not received any review, order them by listing_id and output the top 10? """
    results = listings_collection.aggregate([ 
        {
            # Find reviews with empty listings
            "$match" : { "reviews" : { "$eq" : [] } }
        },
        {
            # Step 2: sort them in descending
            "$sort": { "id" : 1 }
        },
        {
            # Step 3: limit to 10
            "$limit": 10
        },
        {
            # Only show the 'id' in the output
            "$project" : { "_id" : 0, "id" : 1 }
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