#!/usr/bin/python3
'''Connection to database'''
if __name__ == "__main__":

    import sys
    import MySQLdb

    localhost = "localhost"
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]
    db = MySQLdb.connect(
        host="localhost", user=username, passwd=password, db=database)
    c = db.cursor()
    query = "SELECT * "
    query += "FROM states "
    query += "WHERE name = '{}' "
    query += "ORDER BY 1;"
    c.execute(query.format(state))
    registers = c.fetchall()
    for i in registers:
        print(i)
