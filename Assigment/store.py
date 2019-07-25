from bottle import route, run, template, static_file, get, post, delete, request
from sys import argv
import json
import pymysql

connection =pymysql.connect(host='localhost',
                            user='root',
                            password='root',
                            db='bookshoop',
                            cursorclass=pymysql.cursors.DictCursor)




@get("/admin")
def admin_portal():
	return template("pages/admin.html")

@get("/")
def index():
    return template("index.html")

@get("/categories")
def categories():
    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM  categories"
            cursor.execute(query)
        return json.dumps({'CATEGORIES':cursor.fetchall()})
    except:
         return json.dumps({'ERROR':'internal error'})
     

@get('/category/<id>/products')
def loadProducts(id):
   try:
        with connection.cursor() as cursor:
                
                query= f'SELECT * FROM product WHERE category="{id}"'
                cursor.execute(query)
        return json.dumps({'PRODUCTS':cursor.fetchall()})
   except:
         return json.dumps({'error':'internal error'})     
     
     
@get("/products")
def products():
    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM  product"
            cursor.execute(query)
        return json.dumps({'PRODUCTS':cursor.fetchall()})
    except:
         return json.dumps({'ERROR':'internal error'})     
     
     
@get('/product/<id>')
def getProdcut(id):
   try:
        with connection.cursor() as cursor:
                
                query= f'SELECT * FROM product WHERE id="{id}"'
                cursor.execute(query)
                # print(json.dumps(cursor.fetchall()))
                # if json.dumps(cursor.fetchall()) !=0:
                    # print(json.dumps(cursor.fetchall()))
                return json.dumps(cursor.fetchall())
                # else:
                    # return json.dumps({'error':'Product not found'})
   except:
           return json.dumps({'error':'DB problem'})     
       
       
@post("/category")
def add_category():
    name =request.forms.get("name")
    print(name)
    try:
        with connection.cursor() as cursor:
            query = f"insert into categories (name) values ('{name}')"
            cursor.execute(query)
            connection.commit()
            return json.dumps({'CAT_ID': cursor.lastrowid, "CODE": 201})
    except:
            return json.dumps({'ERROR':'error entering new category'})
     

@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='js')


@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='css')


@get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='images')


run(host='localhost', port=5000,debug=True,reloader=True)
