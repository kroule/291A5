GOAL
The goal of this assignment is compare and contrast the suitability of SQL- and NoSQL-based DBMSs depending on data and task. You'll use SQLite for the former and MongoDB for the latter. You'll also be using real open data (courtesy of Airbnb).

PART 1: Building the databases
The CSV files YVR_Airbnb_listings_summary.csv and YVR_Airbnb_reviews.csv (derived from the original dataset) contain summary information and reviews for properties available through Airbnb in the city of Vancouver. Your first tasks are to perform an ETL (extract/transform/load) exercise in order to build the necessary databases from CSV files.

Task 1: Write a Python application (A5T1.py) which will create an SQLite database with two tables, one for the summary listings and one with the reviews. The attribute for the tables should be clear from the headers in the CSV files. The input to the application should be .csv files provided above (they can be hard-coded within your application) and the output should be a SQLite database (A5.db).

Task 2: Write a Python application (A5T2.py) which will use a MongoDB database called A5db (which will be embedded in your own MongoDB data repository) and create within such database a single collection where all the reviews associated to one given listing are to be embedded within that one listing. The input to the application should be .csv files provided above (they can be hard-coded within your applications) but there will be no tangible output. (Note: our lab installations lack mongoexport and mongoimport applications, which could otherwise be used to "dump" and "upload" MongoDB collections, respectively.)

You may want do, but do not need to, use the SQLite database from Task 1 in order to produce the data to build the MongoDB collection.

In order to be sure that your ETL process worked as expected you can use the following queries as a (admittedly very simple) "checksum" verification. 

For the SQLite database:

SELECT MIN(host_id), MAX(host_id), AVG(host_id), COUNT(host_id) FROM listings

should return 

6033, 387534175, 115176061.858295, 4340

SELECT MIN(id), MAX(id), AVG(id), COUNT(id) FROM reviews 

should return 

26444, 730124064, 370354766.849158, 147936

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

Part 2: Using the databases

IMPORTANT: there are 7 tasks below but you need to complete only 5 of them. Tasks 4, 8 and 9 are mandatory and you are free to choose the other two (among Tasks 3, 5, 6 and 7). 

You will write two versions of several Python applications, one connecting to and using the SQLite database (A5TxSQLite.py) and the other one connecting to and using the MongoDB database (A5TxMongoDB.py), where the x in the file name is related to the tasks below. Your applications will provide simple command line-like menu allowing them to execute the following tasks and will output the task result as well as its running time. Note that the basic framework of all applications is very similar, the breaking into one application per task has mainly to do with the submission and marking logistics).

* Task 3 (A5T3SQLite.py and A5T3MongoDB.py): Find how many listings each host own, ordering the output by host_id and only output the top 10.

* **Task 4 (A5T4SQLite.py and A5T4MongoDB.py): Find which listed property(ies) has(have) not received any review, order them by listing_id and output the top 10? 

* Task 5 (A5T5SQLite.py and A5T5MongoDB.py): Given a neighbourhood at run-time (e.g., using command line prompt or via an application parameter) find the average rental cost/night?

* Task 6 (A5T6SQLite.py and A5T6MongoDB.py): Increase the rental cost/night by 10% for all properties in a neighbourhood given at run-time (e.g., using command line prompt or via an application parameter).

* Task7 (A5T7SQLite.py and A5T7MongoDB.py): Add a new attribute called "avgRating” to the table reviews in SQLite and to the documents in the listings collection and insert a random number between 1 and 10 for that new attribute.

* **Task 8 (A5T8SQLite.py and A5T8MongoDB.py): Given a listing_id at run-time (e.g., using command line prompt or via an application parameter) find the host_name, rental_price and the most recent review for that listing.

* **Task 9 (A5T9SQLite.py and A5T9MongoDB.py): Find the top 3 listings which have reviews most similar to a set of keywords given at run-time (e.g., using command line prompt or via an application parameter). Assume those keywords will be given in a comma separated string such as "nice, inexpensive, quiet". 

Important notes wrt Task 9: 

Unlike MongoDB, SQLite (or SQL-based DBMS in general for that matter) does not have a native way to do text-based similarity searches. Fortunately "FTS5 is an SQLite virtual table module that provides full-text search functionality to database applications." Hence, once a virtual table is built using the reviews information (refer to this link for more information) if the user provides a set of keywords as the query terms all one need to do is to issue a query using FTS5's boolean operators (refer to this link for more information). The appendix below has some sample usage of SQLite's FTS5 module.
The ordering of the returned listings may not be identical, and that's OK. This is beyond the scope of the course, but SQLite and MongoDB may use different ways to compare documents, e.s., SQLite's TFS5 uses BM25, and while I couldn't find a reference ("certified" by MongoDB) for how MongoDB does it this document discusses it works well though.
REPORTING / DELIVERABLES
Your submitted applications MUST execute as expected on the lab machines. 
Group composition (at most 3 students) needs to be informed by April 08 (link).
Submissions must be made by the April 13 (link TBD).
What do submit?
TBD
MARKING

TBD


Appendix - Example of SQLite's "FTS5 module" usage:

Try the following on SQLite and observe the results of each query to see how the similarity between the terms in the query and the ranked documents work.

CREATE VIRTUAL TABLE test USING fts5(id, content );

INSERT INTO test VALUES (1, "Coffee and cakes");
INSERT INTO test VALUES (2, "Coffee is overrated");
INSERT INTO test VALUES (3, "coffee, coffee and some tea");
INSERT INTO test VALUES (4, "lots of tea and some coffee");
INSERT INTO test VALUES (5, "only tea");

-- Just making sure everything is where it's supposed to be:
SELECT * FROM test;

-- Finding the rows that have the term coffee
SELECT content FROM test WHERE test MATCH "coffee";

-- Finding the rows that have the term coffee but not the term tea
SELECT content FROM test WHERE test MATCH "coffee NOT tea"; 

-- Finding the rows that have the term coffee and showing more relevant rows (wrt the searched term) first
SELECT content FROM test WHERE test MATCH "coffee" ORDER BY rank;

 -- Finding the rows that have the term coffee or the term tea and showing more relevant rows (wrt the searched terms) first
SELECT content FROM test WHERE test MATCH "coffee OR tea" ORDER BY rank; 
