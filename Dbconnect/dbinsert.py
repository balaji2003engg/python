import pymysql as p
ENDPOINT = 'dbtraining.cluster-ccyhzxfto390.us-east-1.rds.amazonaws.com'
PORT ='3306'
USER= 'admin'
PASSWORD = 'Ch683212'
DBNAME= 'trainingdb'

db = p.connect(host=ENDPOINT,user=USER,password=PASSWORD,db=DBNAME)
cur = db.cursor()
cur.execute("select @@version")
cur.execute("select * from student")
cur.execute("insert into student values('104','Dhan','dhan@gmail.com','11th','Female')")
output =cur.fetchall()
print(output)
print(cur.rowcount,"records effected")
cur.close()
db.close
