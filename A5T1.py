""" Task 1: Write a Python application (A5T1.py) which will create an SQLite database with two tables, one for the summary listings and one with the reviews. The attribute for the tables should be clear from the headers in the CSV files. The input to the application should be .csv files provided above (they can be hard-coded within your application) and the output should be a SQLite database (A5.db). """

import sqlite3, csv
import time

cursor = None
connection = None
def main():
	global connection, cursor

	connection = sqlite3.connect('A5.db')
	cursor = connection.cursor()

	start_time = time.time()
	cursor.execute("DROP TABLE IF EXISTS reviews;")

	cursor.execute("DROP TABLE IF EXISTS listings;")

	table1 = '''CREATE TABLE reviews(
			listing_id INTEGER,
			id INTEGER PRIMARY KEY,
			date TEXT,
			reviewer_id INTEGER, 
			reviewer_name TEXT,
			comments TEXT
			);'''

	table2 = '''CREATE TABLE listings(
			id INTEGER PRIMARY KEY,
			name TEXT,
			host_id INTEGER,
			host_name TEXT,
			neighbourhood TEXT,
			room_type TEXT,
			price INTEGER,
			minimum_nights INTEGER,
			availability_365 INTEGER
			);'''

	cursor.execute(table1)
	cursor.execute(table2)

	reviewsFile = open("YVR_Airbnb_reviews.csv", "r", encoding='utf8')
	reviewsRows = csv.reader(reviewsFile)
	next(reviewsRows) # jumps to row after the header
	cursor.executemany("INSERT INTO reviews VALUES (?, ?, ?, ?, ?, ?)", reviewsRows)

	listingsFile = open("YVR_Airbnb_listings_summary.csv", "r", encoding='utf8')
	listingsRows = csv.reader(listingsFile)
	next(listingsRows) #jumps to row after the header
	cursor.executemany("INSERT INTO listings VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", listingsRows)
	
	print("T1 SQLite runtime:  %s seconds" % (time.time() - start_time)) 
	connection.commit()
	connection.close()

main()
