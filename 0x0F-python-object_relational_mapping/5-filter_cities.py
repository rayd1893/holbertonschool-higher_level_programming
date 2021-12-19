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
    query = "SELECT a.id, a.name "
    query += "FROM cities a "
    query += "JOIN states b "
    query += "ON a.state_id = b.id "
    query += "WHERE b.name COLLATE utf8mb4_bin = %s "
    query += "ORDER BY 1;"
    filters = (state, )
    c.execute(query, filters)
    registers = c.fetchall()
    cities = []
    for i in registers:
        cities.append(i[1])
    print(", ".join(cities))
