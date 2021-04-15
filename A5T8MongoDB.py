""" Given a listing_id at run-time (e.g., using command line prompt or via an application parameter) find the host_name, rental_price and the most recent review for that listing. """

from pymongo import MongoClient
import time

client = MongoClient('localhost', 27017)
db = client["A5db"]

def runQuery():
    # Create or open the collection in the db
    listings_collection = db["listings"]
    print("Get host name, price and most recent listing...")
    user_input = int(input('enter listing_id: '))

    start_time = time.time()
    """ Given a listing_id at run-time (e.g., using command line prompt or via an application parameter) find the host_name, rental_price and the most recent review for that listing. """
    
    # Match id to a given user input, pair all reviews to the matched document, sort by date of review, limit 1 to get most recent, the project the host name price and comment of review.
    results = listings_collection.aggregate([
        {
            "$match" : { "id": user_input}
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
    end_time = time.time()
    for row in results:
        print(row)
        
    print("T8 MongoDB runtime:  %s seconds" % (end_time - start_time)) 
        

def main():
    runQuery()

main()