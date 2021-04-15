""" Find how many listings each host own, ordering the output by host_id and only output the top 10. """

from pymongo import MongoClient
import time

client = MongoClient('localhost', 27017)
db = client["A5db"]

def runQuery():
    # Create or open the collection in the db
    listings_collection = db["listings"]
    
    start_time = time.time()
    ### This is like doing SELECT host_id, COUNT(id) FROM listings GROUP BY host_id ORDER BY count(id) LIMIT 10
    results = listings_collection.aggregate([ 
        {
            # SELECT document, groups them by host_id, then counts the # of occurances
            "$group": { "_id" : "$host_id",  "count" : {"$sum":1} }
        },
        {
            # Step 2: sort them in descending
            "$sort": { "count" : -1 }
        },
        {
            # Step 3: limit 10
            "$limit": 10
        }        
    ])
    end_time = time.time()  
    for row in results:
        print(row)
    
    print("T3 MongoDB runtime:  %s seconds" % (end_time - start_time)) 

def main():
    runQuery()

main()