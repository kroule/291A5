import sqlite3

connection = None
cursor = None

A5 = []

def runQuery():
        global connection, cursor
        
        Query = """SELECT count(host_id), host_id FROM listings GROUP BY host_id LIMIT 10 """
        connection = sqlite3.connect('A5.db')
        cursor = connection.cursor()
        cursor.execute(Query)
        myresult = cursor.fetchall()
        for x in myresult:
                print(x)
        connection.commit()
        connection.close()



def main():
        global connection, cursor
        runQuery()
main()