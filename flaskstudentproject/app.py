from flask import Flask,render_template,request,redirect
import pymysql as p
ENDPOINT = 'dbtraining.cluster-ccyhzxfto390.us-east-1.rds.amazonaws.com'
PORT ='3306'
USER= 'admin'
PASSWORD = 'Ch683212'
DBNAME= 'trainingdb'
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    if request.method =="POST":
        studendetails=request.form
        Name = studendetails['name']
        Rollno = studendetails['rollno']
        Email = studendetails['email']
        Grade = studendetails['grade']
        Gender = studendetails['gender']
        
        db = p.connect(host=ENDPOINT,user=USER,password=PASSWORD,db=DBNAME)
        cur = db.cursor()
       # sql = "insert into student(rollno,name,email,grade,gender) values(Rollno,Name,Email,Grade,Gender)"
        cur.execute("insert into student(rollno,name,email,grade,gender) values(%s,%s,%s,%s,%s)",(Rollno,Name,Email,Grade,Gender))
        db.commit()
        output = cur.fetchall()
        print(output)
        cur.close()
        db.close()
        return redirect('/studentdetails')
    return render_template('index.html')

@app.route('/studentdetails')
def studentlist():
    db = p.connect(host=ENDPOINT,user=USER,password=PASSWORD,db=DBNAME)
    cur = db.cursor()
    result = cur.execute("select * from student")
    if result >0:
        sdetails = cur.fetchall()
        cur.close()
        db.close()
        return render_template('studentdetails.html',sdetails=sdetails)



if  __name__ =="__main__":
    app.run(debug=True)
