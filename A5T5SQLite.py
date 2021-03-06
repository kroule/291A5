#Assignment 5 task 5
#Given a neighbourhood at run-time (e.g., using command line prompt or via an application parameter) find the average rental cost/night?

import sqlite3
import time
connection = None
cursor = None

#################################### START QUERY ########################
def runQuery():
        global connection, cursor
        
        #SQL STATEMENT: select the avg price of listings from a neighbourhood provided at runtime
        Query = """SELECT AVG(price) FROM listings WHERE neighbourhood=? """
        connection = sqlite3.connect('A5.db')
        cursor = connection.cursor()
        print("Enter a neighbourhood to find average rental cost")
        #x will a user inputed string of the neighbourhood to be queried
        x = str(input("enter neighbourhood: "))
        #execute the query with a user runtime input of a specific neighbourhood
        start_time = time.time()
        cursor.execute(Query, (x,))
        end_time = time.time()
        #fetch all of the results from the query and assign them to myresult
        myresult = cursor.fetchall()
        # for every element in myresult, print it
        for x in myresult:
                print(x)
                
        print("T5 SQLite runtime:  %s seconds" % (end_time - start_time)) 
        #commit 
        connection.commit()
        #close connection
        connection.close()
################################ END QUERY #################################

# main function will query with the user inputed neighbourhood and return the avg price
def main():
        global connection, cursor
        runQuery()
        
main()