import pymysql
from bottle import run, route, get, post, delete, put,request,template
import json

connection =pymysql.connect(host='localhost',
                            user='root',
                            password='root',
                            db='bootcamp_2019',
                            cursorclass=pymysql.cursors.DictCursor)

@get('/')
def getAll():
  try:
    with connection.cursor() as cursor:
        query = "SELECT * FROM student"
        cursor.execute(query)
        return  json.dumps(cursor.fetchall())
  except:
         return json.dumps({'error':'something is wrong with the DB'})
                       

@get('/student/<name>')
def get(name):
   try:
        with connection.cursor() as cursor:
                query = f'SELECT * FROM student WHERE firstName ="{name}"'
                cursor.execute(query)
        return json.dumps(cursor.fetchall())
   except  Exception as e:
         return json.dumps({'error':'something is wrong with the DB'+repr(e)})
 
 
 
@post('/add_student')
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
                student_query = "SELECT * FROM student"
                cursor.execute(student_query)
                return json.dumps(cursor.fetchone())
    except Exception as e:    
        return json.dumps({'error':'something is wrong with the DB'+repr(e)})

@put('/update/')
def update():
        myIdid = request.json.get("id")
        fnewname = request.json.get("newName")
        try:
         with connection.cursor() as cursor:
                
                query = f"update student set firstName = '{fnewname}' where id = {myIdid}"
                print(query)
                cursor.execute(query)
                connection.commit()
                students_query = f"SELECT * FROM student where id = {myIdid}"
                cursor.execute(students_query)
                return json.dumps(cursor.fetchone())
        except Exception as e:    
         return json.dumps({'error':'something is wrong with the DB'+repr(e)})       
               
                
@delete('/delete_student')
def dell_student():
    myIdid = request.json.get("id")
    try:
        with connection.cursor() as cursor:
            query=f'DELETE FROM student WHERE id="{myIdid}"'
            cursor.execute(query)
            connection.commit()
            answer="item with id:" + myIdid +" removed from DB"
            return answer
    except Exception as e:    
         return json.dumps({'error':'something is wrong with the DB'+repr(e)})    
 
@route('/cohort/<year>')
def get_cohort(year):
        print(year)
        print(type(year))
        try:
                with connection.cursor() as cursor:
                        query = f'SELECT * FROM cohort WHERE cohort_year ="{year}"'
                        cursor.execute(query)
                return json.dumps(cursor.fetchall())
        except  Exception as e:
                return json.dumps({'error':'something is wrong with the DB'+repr(e)})

run(host='localhost', port=7000, debug=True,reloader=True)