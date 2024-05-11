import pymysql

conn = pymysql.connect(host='127.0.0.1', user='ubuntu', password='rmaWhrdlemf', db='library', charset='utf8')

cur = conn.cursor()

studentNumber = "20213516"
password = "cnduswlsqkqh"
name = "추연진"

sql = f"INSERT INTO USERS (Id, Passwd, name, created_at) VALUES ({studentNumber}, SHA2('{password}', 256), '{name}', CURDATE())"
print(sql)
cur.execute(sql)
conn.commit()
conn.close()