  
""" Find how many listings each host own, ordering the output by host_id and only output the top 10. """

from pymongo import MongoClient
import time

client = MongoClient()
db = client["A5db"]
start_time = time.time()

def runQuery():
    # Create or open the collection in the db
    listings_collection = db["listings"]
    
    ### This is like doing SELECT host_id, COUNT(id) FROM listings GROUP BY host_id ORDER BY count(id) LIMIT 10
    results = listings_collection.aggregate([ 
        {
            # SELECT document, groups them by host_id, then counts the # of occurances  https://stackoverflow.com/questions/23116330/mongodb-select-count-group-by
            "$group": { "_id" : "$host_id",  "count" : {"$sum":1} }
        },
        {
            # Step 2: sort them in descending
            "$sort": { "count" : -1 }
        },
        {
            # Step 3: 
            "$limit": 10
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