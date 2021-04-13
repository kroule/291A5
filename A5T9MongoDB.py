""" Find the top 3 listings which have reviews most similar to a set of keywords given at run-time (e.g., using command line prompt or via an application parameter). Assume those keywords will be given in a comma separated string such as "nice, inexpensive, quiet".  """

from pymongo import MongoClient
import time

client = MongoClient()
db = client["A5db"]
start_time = time.time()

def runQuery(keywords):
    # Create or open the collection in the db
    listings_collection = db["listings"]

    """ Find the top 3 listings which have reviews most similar to a set of keywords given at run-time (e.g., using command line prompt or via an application parameter). Assume those keywords will be given in a comma separated string such as "nice, inexpensive, quiet".  """
    results = listings_collection.aggregate([
        {
            "$match" : { "reviews.comments" :  { "$search" : keywords } }
        },
    ])
    for row in results:
        print(row)
        

def main():
    # List collection names.
    collist = db.list_collection_names()
    if "listings" in collist:
        print("The collection exists.")
        
    runQuery("great fantastic")

main()
print("Program runtime:  %s seconds" % (time.time() - start_time))