""" Find which listed property(ies) has(have) not received any review, order them by listing_id and output the top 10? """

from pymongo import MongoClient
import time 

client = MongoClient('localhost', 27017)
db = client["A5db"]

def runQuery():
    # Create or open the collection in the db
    listings_collection = db["listings"]
    print("Listings with no reviews")
    """ Find which listed property(ies) has(have) not received any review, order them by listing_id and output the top 10? """
    start_time = time.time()
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
    end_time = time.time()
    for row in results:
        print(row)
        
    print("T4 MongoDB runtime:  %s seconds" % (end_time - start_time))  

def main():
    runQuery()

main()