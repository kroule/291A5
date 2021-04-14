""" Find the top 3 listings which have reviews most similar to a set of keywords given at run-time (e.g., using command line prompt or via an application parameter). Assume those keywords will be given in a comma separated string such as "nice, inexpensive, quiet".  """

from pymongo import MongoClient

client = MongoClient()
db = client["A5db"]

def runQuery(keywords):
    # Create or open the collection in the db
    listings_collection = db["listings"]
    """ Find the top 3 listings which have reviews most similar to a set of keywords given at run-time (e.g., using command line prompt or via an application parameter). Assume those keywords will be given in a comma separated string such as "nice, inexpensive, quiet".  """
    index_name = listings_collection.create_index( [("reviews.comments", "text")] )
    results = listings_collection.find( { "$text" : { "$search" : keywords } } , { "score": { "$meta" : "textScore" } } ).sort( [("score", 1)] ).limit(1)
    for row in results:
        print(row)
        print("\n$#############################################\n")


def main():
    # List collection names.
    collist = db.list_collection_names()
    if "listings" in collist:
        print("The collection exists.")
        
    runQuery("great fantastic")

main()
print("Program runtime:  %s seconds" % (time.time() - start_time))
