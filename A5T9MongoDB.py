""" Find the top 3 listings which have reviews most similar to a set of keywords given at run-time (e.g., using command line prompt or via an application parameter). Assume those keywords will be given in a comma separated string such as "nice, inexpensive, quiet".  """

from pymongo import MongoClient
import time 

client = MongoClient()
db = client["A5db"]

def runQuery():
    # Create or open the collection in the db
    listings_collection = db["listings"]
    user = str(input('enter keywords: '))
    """ Find the top 3 listings which have reviews most similar to a set of keywords given at run-time (e.g., using command line prompt or via an application parameter). Assume those keywords will be given in a comma separated string such as "nice, inexpensive, quiet".  """
    index_name = listings_collection.create_index( [("reviews.comments", "text")] )
    results = listings_collection.aggregate( [
        { "$match" : { "$text" : { "$search" : user } } },
        { "$sort" : { "score" : { "$meta" : "textScore" } } },
        { "$project" : { "id" : 1, "_id" : 0, "score" : { "$meta" : "textScore" } } },         #Uncomment this to just see 'listing_id' + text score
        { "$limit" : 3 }
    ])
    for row in results:
        print(row)


def main():
    # List collection names.
    collist = db.list_collection_names()
    if "listings" in collist:
        print("The collection exists.")
        
    start_time = time.time()    
    runQuery()
    print("A5 Task 9 runtime:  %s seconds" % (time.time() - start_time))

main()