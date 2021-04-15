#Application 5 task 8 
#Given a listing_id at run-time (e.g., using command line prompt or via an application parameter) find the host_name, rental_price and the most recent review for that listing.
import sqlite3
import time
connection = None
cursor = None

############################ START QUERY ##############################
def runQuery():
        global connection, cursor
        #SQL STATEMENT: find the host name, the price and comments from a user selected listing_id and order by the most recent date and limit results to 1 
        Query = """SELECT host_name, price, comments FROM listings, reviews WHERE listing_id=? ORDER BY date DESC LIMIT 1"""
        connection = sqlite3.connect('A5.db')
        cursor = connection.cursor()
        #user will input a integer listing_id for the query
        x = int(input("enter listing id: "))
        #execute the query with the user inputed integer (listing_id)
        start_time = time.time()
        cursor.execute(Query, (x,))
        end_time = time.time()
        # fetchall results of the query and assign it to myresult
        myresult = cursor.fetchall()
        #for every element in myresult print it off
        for x in myresult:
                print(x)
                
        print("T8 SQLite runtime:  %s seconds" % (end_time - start_time))         
        #commit
        connection.commit()
        #close connection
        connection.close()
############################### CLOSE QUERY ###################################


# main will prompt user for the inputed integer listing id and then run the query with said input and print result
def main():
        global connection, cursor
        print("Input listing id to find, host name, rental price and the most recent review")
        runQuery()
        
main()
