""" Task 2: Write a Python application (A5T2.py) which will use a MongoDB database called A5db (which will be embedded in your own MongoDB data repository) and create within such database a single collection where all the reviews associated to one given listing are to be embedded within that one listing. The input to the application should be .csv files provided above (they can be hard-coded within your applications) but there will be no tangible output. (Note: our lab installations lack mongoexport and mongoimport applications, which could otherwise be used to "dump" and "upload" MongoDB collections, respectively.) """

""" 
In order to be sure that your ETL process worked as expected you can use the following queries as a (admittedly very simple) "checksum" verification. 

For the MongoDB database:

db.listings.aggregate([ 

    {$group: {_id: null, min: {$min: "$host_id"}, max: {$max: "$host_id"}, avg: {$avg: "$host_id"}, count: {$sum: 1}}} 

])

should return 

{ "_id" : null, "min" : 6033, "max" : 387534175, "avg" : 115176061.85829493, "count" : 4340 }

and

db.listings.aggregate([

    {$unwind: "$reviews"}, 

    {$group: {_id: null, min: {$min: "$reviews.id"}, max: {$max: "$reviews.id"}, avg: {$avg: "$reviews.id"}, count: {$sum: 1}}}

])

should return 

{ "_id" : null, "min" : 26444, "max" : 730124064, "avg" : 370354766.84915775, "count" : 147936 }
"""

from pymongo import MongoClient 

client = MongoClient()
database = client["A5db"]
collist = database.list_collection_names()

