""" Given a neighbourhood at run-time (e.g., using command line prompt or via an application parameter) find the average rental cost/night? """

from pymongo import MongoClient
import time

client = MongoClient('localhost', 27017)
db = client["A5db"]

def runQuery():
    # Create or open the collection in the db
    listings_collection = db["listings"]
    print("Enter a neighbourhood to find average rental cost")
    user = str(input('enter neighbourhood: '))

    """ Given a neighbourhood at run-time (e.g., using command line prompt or via an application parameter) find the average rental cost/night? """
    start_time = time.time()
    results = listings_collection.aggregate([ 
        {
            # Find listings with neighborhood
            "$group" : { "_id" : "$neighbourhood", "average" : {"$avg": "$price"} }
        },
        {
            "$match" : {"_id" : user}
        }
    ])
    end_time = time.time()
    for row in results:
        print(row)
        
    print("T5 MongoDB runtime:  %s seconds" % (end_time - start_time)) 

def main():
    runQuery() 

main()