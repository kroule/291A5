#Application 5 Task 3 
#Find how many listings each host own, ordering the output by host_id and only output the top 10.

import sqlite3
import time
connection = None
cursor = None

A5 = []


############################ START OF QUERY #########################
def runQuery():
        global connection, cursor
        
         # might be the correct way
        #SQL STATEMENT: select the number of times the host id appears as well as the host id and then group it by the host id and limit the results to 10.
        Query = """SELECT count(id), host_id FROM listings GROUP BY host_id LIMIT 10 """
        Query = """ SELECT host_id, count(id) FROM listings GROUP BY host_id ORDER BY count(id) DESC LIMIT 10; """
        connection = sqlite3.connect('A5.db')
        cursor = connection.cursor()
        #execute the query with no runtime input as no input is required
        start_time = time.time()
        cursor.execute(Query)
        end_time = time.time()
        #fetch all of the results from the query and assign them to myresult
        myresult = cursor.fetchall()
        #for all results in myresult print each element of said results
        for x in myresult:
                print(x)
                
        print("T3 SQLite runtime:  %s seconds" % (end_time - start_time))   
        #commit the connection
        connection.commit()
        #close the connection
        connection.close()

############################## END OF QUERY ################################


#main function will run function query and return results
def main():
        global connection, cursor
        runQuery()       
        
main()