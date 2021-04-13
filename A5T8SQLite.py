import sqlite3

connection = None
cursor = None

A5 = []

def runQuery():
        global connection, cursor
        
        Query = """SELECT host_name, price, comments FROM listings, reviews WHERE listing_id=? ORDER BY date DESC LIMIT 1"""
        connection = sqlite3.connect('A5.db')
        cursor = connection.cursor()
        x = int(input("enter listing id: "))
        cursor.execute(Query, (x,))
        myresult = cursor.fetchall()
        for x in myresult:
                print(x)
        connection.commit()
        connection.close()



def main():
        global connection, cursor
        print("Input listing id to find, host name, rental price and the most recent review")
        runQuery()
main()