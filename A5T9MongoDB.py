""" Find the top 3 listings which have reviews most similar to a set of keywords given at run-time (e.g., using command line prompt or via an application parameter). Assume those keywords will be given in a comma separated string such as "nice, inexpensive, quiet".  """

from pymongo import MongoClient
import time 

client = MongoClient('localhost', 27017)
db = client["A5db"]

def runQuery():
    print("Find top 3 listings with reviews most similar to keywords... [comma separated]")
    # Create or open the collection in the db
    listings_collection = db["listings"]
    user_input = str(input('enter keywords: '))
    # Input with commas, we don't need them so just replace them with empty string
    user_input = user_input.replace(',', '')
    """ Find the top 3 listings which have reviews most similar to a set of keywords given at run-time (e.g., using command line prompt or via an application parameter). Assume those keywords will be given in a comma separated string such as "nice, inexpensive, quiet".  """
    index_name = listings_collection.create_index( [("reviews.comments", "text")] )
    start_time = time.time()
    results = listings_collection.aggregate( [
        { "$match" : { "$text" : { "$search" : user_input } } },
        { "$sort" : { "score" : { "$meta" : "textScore" } } },
        { "$project" : { "id" : 1, "_id" : 0, "score" : { "$meta" : "textScore" } } },         #Uncomment this to just see 'listing_id' + text score
        { "$limit" : 3 }
    ])
    end_time = time.time()
    for row in results:
        print(row)
        
    print("T9 MongoDB runtime:  %s seconds" % (end_time - start_time)) 

def main():
    runQuery()

main()