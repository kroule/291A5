#Application 5 task 4
#Find which listed property(ies) has(have) not received any review, order them by listing_id and output the top 10? 


import sqlite3

connection = None
cursor = None

A5 = []


######################### START OF QUERY ############################
def runQuery():
        global connection, cursor
        
        #SQL STATEMENTS: select the id from listings where the id is not found in the listing_id from reviews and limit results to 10
        Query = """SELECT id FROM listings WHERE id NOT IN (SELECT listing_id FROM reviews) GROUP BY id LIMIT 10 """
        connection = sqlite3.connect('A5.db')
        cursor = connection.cursor()
        #execute the query with no runtime input as no input is required
        cursor.execute(Query)
        #fetch all of the results from the query and assign them to myresult
        myresult = cursor.fetchall()
        #for all results in myresult print each element of said results
        for x in myresult:
                print(x)
        #commit the connection
        connection.commit()
        #close the connection
        connection.close()

############################## END QUERY ###########################

#main() will run the query and print the results
def main():
        global connection, cursor
        runQuery()
main()