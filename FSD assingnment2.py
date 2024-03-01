import sqlite3
try:
    conn = sqlite3.connect("records.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE user2 (id INTEGER, name TEXT, cell BIGINT, email TEXT)")
    cur.execute("""INSERT INTO user2 VALUES (1, 'Prajwal', 8951260930, 'prcm21ec@cmrit.ac.in')""")
    cur.execute("""INSERT INTO user2 VALUES (2, 'vekat', 8088709381, 'yve21ec@cmrit.ac.in')""")
    cur.execute("""INSERT INTO user2 VALUES (3, 'Chetana',8317349115, 'chp21ee@cmrit.ac.in')""")
    cur.execute("""INSERT INTO user2 VALUES (4, 'kusuma',8660760072, 'kutv21ee@cmrit.ac.in')""")
    cur.execute("""INSERT INTO user2 VALUES (5, 'Kushal', 9932592523, 'kum21ee@cmrit.ac.in')""")
    conn.commit()
    print("Insert operation done")

    data=cur.execute("""SELECT * FROM user2""") 
    for row in data: 
        print(row)

except sqlite3.Error as e:
    print("Error while inserting Data", e)

finally:
    if(conn):
        conn.close()
        print("Connection closed")