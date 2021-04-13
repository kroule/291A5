""" Find how many listings each host own, ordering the output by host_id and only output the top 10. """

from pymongo import MongoClient

client = MongoClient()
db = client["A5db"]



### See: https://www.analyticsvidhya.com/blog/2020/08/query-a-mongodb-database-using-pymongo/
def runQuery():
    # Create or open the collection in the db
    listings_collection = db["listings"]
    
    ### Finds the listings with the 'id' 10080
    results = listings_collection.find({"id": 10080})
    for row in results:
        print(row)
        
    print("###############################################################")
    print("###############################################################")
    print("###############################################################")
        
    ### Sorts collection by price descending  .limit(field, -1) takes first listing (finds min priced entry)
    results = listings_collection.find({}).sort("price", -1).limit(1)
    ### Sorts collection by price ascending   .limit(field, 1) takes first listing (finds max priced entry)
    results = listings_collection.find({}).sort("price", 1).limit(1)
    
    ### Finds the number of results for host_name = Paola
    result_count = listings_collection.find({"host_name": 'Paola'}).count()
    
    ### Finds host_id=48621877 and how many
    result_count = listings_collection.find( {"host_id" : 48621877} ).count()
    
    ### Search within the aggregate data (reviews 'sub table' within listings
    results = listings_collection.find( 
        { "reviews": {"$elemMatch": {"reviewer_name": "Elizabeth"}} } )
    
    ### Finds the number of listings each host owns...
    ### SELECT COUNT(id) FROM listings GROUP BY host_id LIMIT 10;
    ### listings_collection.find({})
    
    ### The _id field is included in the returned documents by default unless you explicitly specify _id: 0 in the projection to suppress the field.

    ### stage 1
    #{
        #"$match" : 
                 #{"center_id" : {"$eq" : 11 } }
    #},
    ### stage 2
    #{
        #"$group" : { "_id" : 0 ,
                     #"average_num_orders": { "$avg" : "$num_orders"},
                     #"unique_meal_id" : {"$addToSet" : "$meal_id"}} 
                     
    # db.mycol.aggregate([ {$group : {_id: {user : "$by_user"}, num_tutorial : {$sum : 1} } } ])
    # SELECT by_user AS user, count(*) AS num_tutorial FROM mycol GROUP BY by_user;

    ### You use $field-name format, when you want to reference a field from the original or intermediary document. Here you are summing up all the page views grouping them by author.

    ### This is like doing SELECT host_id, COUNT(*) FROM listings GROUP BY host_id LIMIT 10
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