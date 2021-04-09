""" Task 2: Write a Python application (A5T2.py) which will use a MongoDB database called A5db (which will be embedded in your own MongoDB data repository) and create within such database a single collection where all the reviews associated to one given listing are to be embedded within that one listing. The input to the application should be .csv files provided above (they can be hard-coded within your applications) but there will be no tangible output. (Note: our lab installations lack mongoexport and mongoimport applications, which could otherwise be used to "dump" and "upload" MongoDB collections, respectively.) """
import pymongo
from pymongo import MongoClient
import csv
def main():

	client = MongoClient('localhost', 27008)

	database = client["A5db"]


	collection = database["listings"]

	collection.delete_many({})

	with open('YVR_Airbnb_listings_summary.csv', 'r', encoding= 'utf8') as csvfile:
		header = ["id", "name", "host_id", "host_name", "neighbourhood", "room_type", "price", "minimum_nights", "availability_365"]
		reader = csv.reader(csvfile)
		for row in reader:
			doc={}
			for n in range(0, len(header)):
				doc[header[n]] = row[n]
			collection.insert_one(doc)

	client.close()
main()
