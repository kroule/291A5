""" Task 2: Write a Python application (A5T2.py) which will use a MongoDB database called A5db (which will be embedded in your own MongoDB data repository) and create within such database a single collection where all the reviews associated to one given listing are to be embedded within that one listing. The input to the application should be .csv files provided above (they can be hard-coded within your applications) but there will be no tangible output. (Note: our lab installations lack mongoexport and mongoimport applications, which could otherwise be used to "dump" and "upload" MongoDB collections, respectively.) """
import pymongo
from pymongo import MongoClient
import csv
def main():

	client = MongoClient('localhost', 27008)

	database = client["A5db"]

	collection = database["listings"]

	with open ('YVR_Airbnb_listings_summary.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			listings = collection.insert_one(row)

	'''
	csvlistings = open("YVR_Airbnb_listings_summary.csv", "r", encoding='utf8')
	csvreviews = open("YVR_Airbnb_reviews.csv", "r", encoding='utf8')

	listingsrows = csv.reader(csvlistings)
	next(listingsrows)
	listings = collection.insert_many(listingsrows)
	
	reviewsrows = csv.reader(csvfilereviews)
	next(reviewsrows)
	reviews = collection.insert_many(reviewsrows)

	
	csvfilelistings.close()
	csvfilereviews.close()
	'''
	client.close()
main()
