import pymysql

conn = pymysql.connect(host='127.0.0.1', user='ubuntu', password='rmaWhrdlemf', db='library', charset='utf8')

cur = conn.cursor()

sql = "select * from USERS"
cur.execute(sql)

while(1):
    row = cur.fetchone()
    if row==None:
        break

    print(row[0], row[1], row[2], row[3])

conn.close()