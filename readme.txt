## Remove after ##
A single .tgz file containing a README.txt file, and all necessary (and commented) source code in Python necessary to execute the necessary applications (the naming of all files must be as described above). The README file should have the name(s) of student(s), their ccid(s), the usual collaboration statement, a list of all included files, plus a brief instructions on how to run the applications. The README file should also include a section with a simple "how to” guide for executing the applications for each task. The .tgz file (containing at least 12 files, README.txt plus 11 .py files and other files with common functions you have defined) should be submitted using this submission page. 
##################

Name: Jacob Nguyen, Keaton Roulette, Liam Gyori
ccid: jvnguyen, roulette, lgyori
collaboration statement: The above members worked on the project together
Included files: 
	- README.txt
	- A5T1.py
	- A5T2.py
	- A5T3MongoDB.py
	- A5T3SQLite.py
	- A5T4MongoDB.py
	- A5T4SQLite.py
	- A5T5MongoDB.py
	- A5T5SQLite.py
	- A5T8SQLite.py
	- A5T8MongoDB.py
	- A5T9MongoDB.py

Instructions:
	1). Make sure to have the "YVR_Airbnb_listings_summary.csv" and "YVR_Airbnb_reviews.csv" data in the same directory as the python files.
	2). Run A5T1.py and A5T2.py. This will create the databases
	3). Run the remaining python files as needed in any order.
		3a). For Tasks 5 - Input a neighborhood to see average price (e.g: "Sunset" or "Downtown")
		3b). For Task 8 - Input a single listing_id (e.g: 10080) Assuming input is known to exist - no error for non-existant printed out.
		3c). For Task 9 - input a set of keywords separated by commas and once space. (e.g: "great, fantastic, horrible" )

Notes: Our python code for MongoClient uses port 27017