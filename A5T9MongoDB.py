""" Find the top 3 listings which have reviews most similar to a set of keywords given at run-time (e.g., using command line prompt or via an application parameter). Assume those keywords will be given in a comma separated string such as "nice, inexpensive, quiet".  """

from pymongo import MongoClient
import time 

client = MongoClient()
db = client["A5db"]
start_time = time.time()

def runQuery():
    # Create or open the collection in the db
    listings_collection = db["listings"]
    user = str(input('enter keywords: '))
    """ Find the top 3 listings which have reviews most similar to a set of keywords given at run-time (e.g., using command line prompt or via an application parameter). Assume those keywords will be given in a comma separated string such as "nice, inexpensive, quiet".  """
    index_name = listings_collection.create_index( [("reviews.comments", "text")] )
    results = listings_collection.find( { "$text" : { "$search" : user } } , { "score": { "$meta" : "textScore" } } ).sort( [("score", 1)] ).limit(3)
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