#Assignment 5 task 5
#Given a neighbourhood at run-time (e.g., using command line prompt or via an application parameter) find the average rental cost/night?

import sqlite3

connection = None
cursor = None

A5 = []

#################################### START QUERY ########################
def runQuery():
        global connection, cursor
        
        #SQL STATEMENT: select the avg price of listings from a neighbourhood provided at runtime
        Query = """SELECT AVG(price) FROM listings WHERE neighbourhood=? """
        connection = sqlite3.connect('A5.db')
        cursor = connection.cursor()
        #x will a user inputed string of the neighbourhood to be queried
        x = str(input("enter neighbourhood: "))
        #execute the query with a user runtime input of a specific neighbourhood
        cursor.execute(Query, (x,))
        #fetch all of the results from the query and assign them to myresult
        myresult = cursor.fetchall()
        # for every element in myresult, print it
        for x in myresult:
                print(x)
        #commit 
        connection.commit()
        #close connection
        connection.close()
################################ END QUERY #################################

# main function will query with the user inputed neighbourhood and return the avg price
def main():
        global connection, cursor
        print("Input listing id to find, host name, rental price and the most recent review")
        runQuery()
main()