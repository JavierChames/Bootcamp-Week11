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
        return json.dumps(cursor.fetchall())
   except:
         return json.dumps({'error':'Product not found'})     
     
     


@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='js')


@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='css')


@get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='images')


run(host='0.0.0.0', port=argv[1],debug=True,reloader=True)
