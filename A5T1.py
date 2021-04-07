""" Task 1: Write a Python application (A5T1.py) which will create an SQLite database with two tables, one for the summary listings and one with the reviews. The attribute for the tables should be clear from the headers in the CSV files. The input to the application should be .csv files provided above (they can be hard-coded within your application) and the output should be a SQLite database (A5.db). """

"""
In order to be sure that your ETL process worked as expected you can use the following queries as a (admittedly very simple) "checksum" verification. 

For the SQLite database:

SELECT MIN(host_id), MAX(host_id), AVG(host_id), COUNT(host_id) FROM listings

should return 

6033, 387534175, 115176061.858295, 4340

SELECT MIN(id), MAX(id), AVG(id), COUNT(id) FROM reviews 

should return 

26444, 730124064, 370354766.849158, 147936

"""

files = ['A5T3SQLite.py' , 'A5T3MongoDB.py',
'A5T4SQLite.py' , 'A5T4MongoDB.py',
'A5T5SQLite.py' , 'A5T5MongoDB.py',
'A5T6SQLite.py' , 'A5T6MongoDB.py',
'A5T7SQLite.py' , 'A5T7MongoDB.py',
'A5T8SQLite.py' , 'A5T8MongoDB.py',
'A5T9SQLite.py' , 'A5T9MongoDB.py']

instructions = ['#Find how many listings each host own, ordering the output by host_id and only output the top 10.',
                '#Find which listed property(ies) has(have) not received any review, order them by listing_id and output the top 10?',
                '#Given a neighbourhood at run-time (e.g., using command line prompt or via an application parameter) find the average rental cost/night?'
                '#Increase the rental cost/night by 10% for all properties in a neighbourhood given at run-time (e.g., using command line prompt or via an application parameter).',
                '#Add a new attribute called "avgRating” to the table reviews in SQLite and to the documents in the listings collection and insert a random number between 1 and 10 for that new attribute.',
                '#Given a listing_id at run-time (e.g., using command line prompt or via an application parameter) find the host_name, rental_price and the most recent review for that listing.',
                '#Find the top 3 listings which have reviews most similar to a set of keywords given at run-time (e.g., using command line prompt or via an application parameter). Assume those keywords will be given in a comma separated string such as "nice, inexpensive, quiet".']

dependancy = ['import sqlite3', 
              'from pymongo import MongoClient']

for i in range(len(files)):
    file = open(files[i], 'x')
    file.write(instructions[i//2])
    file.write(dependancy[i%2])
    file.close()