""" Task 1: Write a Python application (A5T1.py) which will create an SQLite database with two tables, one for the summary listings and one with the reviews. The attribute for the tables should be clear from the headers in the CSV files. The input to the application should be .csv files provided above (they can be hard-coded within your application) and the output should be a SQLite database (A5.db). """

import sqlite3, csv

cursor = None
connection = None
def main():
	global connection, cursor

	connection = sqlite3.connect('A5.db')
	cursor = connection.cursor()

	cursor.execute("DROP TABLE IF EXISTS Airbnb_reviews;")

	cursor.execute("DROP TABLE IF EXISTS Airbnb_listings_summary;")

	table1 = '''CREATE TABLE Airbnb_reviews(
			listing_id INTEGER,
			id INTEGER PRIMARY KEY,
			date TEXT,
			reviewer_id INTEGER, 
			reviewer_name TEXT,
			comments TEXT
			);'''

	table2 = '''CREATE TABLE Airbnb_listings_summary(
			id INTEGER PRIMARY KEY,
			name TEXT,
			host_id INTEGER,
			host_name TEXT,
			neighbourhood TEXT,
			room_type TEXT,
			price INTEGER
			);'''

	cursor.execute(table1)
	cursor.execute(table2)

	reviewsFile = open("YVR_Airbnb_reviews.csv", "r", encoding='utf8')
	reviewsRows = csv.reader(reviewsFile)
	next(reviewsRows) # jumps to row after the header
	cursor.executemany("INSERT INTO Airbnb_reviews VALUES (?, ?, ?, ?, ?, ?)", reviewsRows)

	listingsFile = open("YVR_Airbnb_listings_summary.csv", "r", encoding='utf8')
	listingsRows = csv.reader(listingsFile)
	next(listingsRows) #jumps to row after the header
	cursor.executemany("INSERT INTO Airbnb_listings_summary VALUES (?, ?, ?, ?, ?, ?, ?)", listingsRows)

	connection.commit()
	connection.close()

main()
