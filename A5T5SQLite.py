import sqlite3

connection = None
cursor = None

A5 = []

def runQuery():
        global connection, cursor
        
        Query = """SELECT AVG(price) FROM listings WHERE neighbourhood=? """
        connection = sqlite3.connect('A5.db')
        cursor = connection.cursor()
        x = str(input("enter neighbourhood: "))
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