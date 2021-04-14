""" Task 2: Write a Python application (A5T2.py) which will use a MongoDB database called A5db (which will be embedded in your own MongoDB data repository) and create within such database a single collection where all the reviews associated to one given listing are to be embedded within that one listing. The input to the application should be .csv files provided above (they can be hard-coded within your applications) but there will be no tangible output. (Note: our lab installations lack mongoexport and mongoimport applications, which could otherwise be used to "dump" and "upload" MongoDB collections, respectively.) """
import pymongo
from pymongo import MongoClient
import csv
def main():
	client = MongoClient()

	database = client["A5db"]
	
	collection = database["listings"]

	collection.delete_many({})


	listingsfile = open('YVR_Airbnb_listings_summary.csv', 'r', encoding= 'utf8')
	reviewsfile = open('YVR_Airbnb_reviews.csv', 'r', encoding = 'utf8')


	### Create an object that operates like a regular reader but maps the information in each row to a dict whose keys are given by the optional fieldnames parameter.
	### The fieldnames parameter is a sequence. If fieldnames is omitted, the values in the first row of file f will be used as the fieldnames. 
	### Regardless of how the fieldnames are determined, the dictionary preserves their original ordering.

	listingsrows = csv.DictReader(listingsfile)
	reviewsrows = csv.DictReader(reviewsfile)

	### Didn't know a better way to do this - if a given field name needs to be an 'int' it's set to true
	header_listings = {"id":True, "name":False, "host_id":True, "host_name":False, "neighbourhood":False, "room_type":False, "price":True, "minimum_nights":True, "availability_365":True}
	header_reviews = {'listing_id':True,'id':True,'date':False,'reviewer_id':True,'reviewer_name':False,'comments':False}
	
	### Step 1: Initialize a dictionary for every listings 'reviews' field (this will be a list of the reviews)
	group_reviews = {}
	for rows in listingsrows:
		for i, v in header_listings.items():
			### Check if field should be casted to int
			if(v == True):
				rows[i] = int(rows[i])
		group_reviews[str(rows['id'])] = []
		
	### Step 2: Add the reviews to the list that belong to the proper listings
	### rows['listing_id'] = this is a row in the 'reviews' table with the 'listing_id' = to the 'id' within the table listings
	for rows in reviewsrows:
		for i, v in header_reviews.items():
			### Check if field should be casted to int
			if(v == True):
				rows[i] = int(rows[i])
				
		group_reviews[str(rows['listing_id'])].append(rows)
		
	### Set the file reader file pointer back to the start
	reviewsfile.seek(0)
	listingsfile.seek(0)
	### Skip the first row to ignore the header
	next(listingsrows)
	next(reviewsrows)
		
	### Iterate over every listing
	for rows in listingsrows:
		
		### Add the appropriate fields into the dictionary
		row = {}
		for field in listingsrows.fieldnames:
			### Check if the field should be casted to int
			if(header_listings[field]):
				row[field] = int(rows[field])
			else:
				row[field] = rows[field]
			
	
		### Add our new 'reviews' column/field to the listing
		row['reviews'] = group_reviews[str(rows['id'])]
				
		### Add our new entry into the listings dict
		collection.insert_one(row)
		
	### All done!
	client.close()
	
	### This builds the following structure
	#listings 
	#[ 
	  #{
	  #_id: ObjectId("6072b8569c7e8809eedc60d8"),
	  #id: 18589,
	  #name: 'Commercial Drive B&B',
	  #host_id: 71508,
	  #host_name: 'Sylvain & Alexis',
	  #neighbourhood: 'Grandview-Woodland',
	  #room_type: 'Private room',
	  #price: 79,
	  #minimum_nights: 1,
	  #availability_365: 194,
	  #reviews: [ {listing_id: 18589,
	              #id: 300387,
	              #date: '2011-06-06',
	              #reviewer_id: 578644,
	              #reviewer_name: 'Bonita',
	              #comments: 'Sylvain is a charming host and an extremely talented and creative cook! Our stay in Vancouver was made 100% better because of our choice of this quiet, beautifully decorated home, combined with the truly gracious and generous nature of Sylvain and his partner. We will return to stay with them in the future when Vancouver beckons again.'
	              #},
	             #{listing_id: 18589,
	              #id: 308845,
	              #date: '2011-06-11',
	              #reviewer_id: 667825,
	              #reviewer_name: 'Kim',
	              #comments: 'What a wonderful experience staying with this lovely couple! And wow, what great breakfasts they provided for us! They even bought special cereal for our two small children:) Very comfortable and cozy accommodations. \n' +
	              #'I highly recommend this bnb!' }
	             #]
	  #}
	#]

main()
