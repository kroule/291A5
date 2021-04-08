""" Task 2: Write a Python application (A5T2.py) which will use a MongoDB database called A5db (which will be embedded in your own MongoDB data repository) and create within such database a single collection where all the reviews associated to one given listing are to be embedded within that one listing. The input to the application should be .csv files provided above (they can be hard-coded within your applications) but there will be no tangible output. (Note: our lab installations lack mongoexport and mongoimport applications, which could otherwise be used to "dump" and "upload" MongoDB collections, respectively.) """
import pymongo
from pymongo import MongoClient 
import pandas as pd
import json, csv,sys, getopt, pprint

def main():
	'''
	client = MongoClient('localhost', 27017)

	database = client["A5db"]

	collection = database["listings"]

	collection.delete_many({})
	
	csvfile = open("YVR_Airbnb_listings_summary.csv", "r")
	reader = csv.DictReader(csvfile)

	header = ["id", "name", "host_id", "host_name", "neighbourhood", "room_type", "price", "minimum_nights", "availability_365"]
	'''
	with open('YVR_Airbnb_listings_summary.csv', 'r', encoding='utf8') as file:
		data = file.read()
		client = MongoClient()
		database = client["A5db"]
		database.segment.drop()
		header = ["id", "name", "host_id", "host_name", "neighbourhood", "room_type", "price"    , "minimum_nights", "availability_365"]

		for each in data:
			row = {}
			for field in header:
				row[field]=each[field]
			db.segment.insert(row)

	database.eval("db.shutdownServer()")
		
main()
