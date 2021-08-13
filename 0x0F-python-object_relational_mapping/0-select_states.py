 1#!/usr/bin/python3
 2"""
 3return all table values (table 'states')
 4parameters given to script: username, password, database
 5"""
 6
 7import MySQLdb
 8from sys import argv
 9
10if __name__ == "__main__":
11
12    # connect to database
13    db = MySQLdb.connect(host="localhost",
14                         port=3306,
15                         user=argv[1],
16                         passwd=argv[2],
17                         db=argv[3])
18
19    # create cursor to exec queries using SQL
20    cursor = db.cursor()
21    cursor.execute("SELECT * FROM states ORDER BY id ASC")
22    for row in cursor.fetchall():
23        print(row)
24    cursor.close()
25    db.close()
