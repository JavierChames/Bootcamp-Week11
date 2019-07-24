import pymysql
from bottle import run, route, get, post, delete, put,request
import json

connection =pymysql.connect(host='localhost',
                            user='root',
                            password='root',
                            db='bootcamp_2019',
                            cursorclass=pymysql.cursors.DictCursor)

@get('/students')
def getAll():
  try:
    with connection.cursor() as cursor:
        query = "SELECT * FROM student"
        cursor.execute(query)
        return json.dumps(cursor.fetchall())
  except:
         return json.dumps({'error':'something is wrong with the DB'})
                       

@get('/student/<name>')
def get(name):
   try:
        with connection.cursor() as cursor:
                query = f'SELECT * FROM student WHERE firstName ="{name}"'
                cursor.execute(query)
        return json.dumps(cursor.fetchall())
   except:
         return json.dumps({'error':'something is wrong with the DB'})
 
 
 
@post('/add')
def add():
    try:
        with connection.cursor() as cursor:
                fname = request.json.get("firstName")
                lname = request.json.get("lastName")
                course = request.json.get("course")
                start= request.json.get("start_study_year")
                end= request.json.get("end_study_year")

                query = "INSERT into student (firstName, lastName,course,start_study_year,end_study_year)values('{}', '{}','{}','{}','{}')".format(fname, lname,course,start,end)
                cursor.execute(query)
                connection.commit()
                
                cursor.execute(query)
                connection.commit()
                student_query = "SELECT * FROM student"
                cursor.execute(student_query)
                return json.dumps(cursor.fetchall())
    except:    
        return json.dumps({'error':'something is wrong with the DB'})



@put('/update/<name>')
def update(name):
        try:
         with connection.cursor() as cursor:
                # fname = request.json.get("firstName")
                query = f'update  student set firstName  ="test" where firstname ="{name}"'
                cursor.execute(query)
                connection.commit()
        except:    
         return json.dumps({'error':'something is wrong with the DB'})       

run(host='localhost', port=7000, debug=True,reloader=True)