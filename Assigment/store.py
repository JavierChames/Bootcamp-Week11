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

@post("/category")
def add_category():
    name =request.forms.get("name")
    
    try:
        with connection.cursor() as cursor:
        #     Check if new category allready exits in DB(no check of lower or upper case)
            prequery=f'SELECT * FROM  categories where name="{name}"'
            cursor.execute(prequery)
            rc=cursor.rowcount
            print(rc)   
            if rc == 0:     
                query = f"insert into categories (name) values ;('{name}')"
                cursor.execute(query)
                connection.commit()
                return json.dumps({'CAT_ID': cursor.lastrowid, "CODE": 201,'ERROR':'​The category was created successfully','STATUS':'SUCCESS'})
            else:
                 return json.dumps({"CODE": 200,'ERROR':'The category was not created due to an error',"STATUS":"​ERROR",'MSG':"Category already exists"})
    except Exception as e:
            return json.dumps({'ERROR':'error entering new category:'+repr(e)})

@get("/categories")
def categories():
    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM  categories"
            cursor.execute(query)
            return json.dumps({'CATEGORIES':cursor.fetchall(),"CODE": 200})
    except:
         return json.dumps({'ERROR':'internal error',"CODE": 500})
     
     
@get('/product/<id>')
def getProdcut(id):
   try:
        with connection.cursor() as cursor:
                
                query= f'SELECT * FROM product WHERE id="{id}"'
                cursor.execute(query)
                return json.dumps(cursor.fetchall())
   except:
           return json.dumps({'error':'DB problem'})     
       
     
@delete("/category/<id>")
def dell_category(id):
    try:
        with connection.cursor() as cursor:
            query=f'DELETE FROM categories WHERE id="{id}"'
            cursor.execute(query)
            connection.commit()
            return json.dumps({'CAT_ID': cursor.lastrowid, "CODE": 201})
    except:
            return json.dumps({'ERROR':'category not found, "CODE": 404'})   
     
     
@post("/product")
def product():
    cat=request.forms.get("category")
    name =request.forms.get("title")
    description =request.forms.get("desc")
    favorite =request.forms.get("favorite")
    price=int(request.forms.get("price"))
    img_url=request.forms.get("img_url")
    if favorite =="on":
         favorite = 1
    else:
         favorite = 0
    try:
        with connection.cursor() as cursor:
            check_product_exists= f"select * from product where title ='{name}'"
            cursor.execute(check_product_exists)
            prod_id=json.dumps(cursor.fetchone()["id"])
            rc=cursor.rowcount
            prequery= f"select name from categories where id ='{cat}'"
            cursor.execute(prequery)
            cat_name=cursor.fetchone()['name']
            cursor.execute(prequery)
            if rc ==0 :
                query = f"insert into product (title,description,price,img_url,category,favorite) values ('{name}','{cat_name}','{price}','{img_url}','{cat}','{favorite}')"
            else:
                query = f"update product set title = '{name}', description = '{cat_name}',price = '{price}',img_url='{img_url}',category='{cat}',favorite='{favorite}'where id = '{prod_id}'"
                print(query)
            cursor.execute(query)
            connection.commit()
            return json.dumps({'CAT_ID': cursor.lastrowid, "SUCCESS":"The product was added successfully"})
    except Exception as e:
            return json.dumps({'ERROR':'​The product was not create due to an error:'+repr(e)})   
    
@delete('/product/<id>')
def getProdcut(id):
   try:
        with connection.cursor() as cursor:
                query= f'delete  FROM product WHERE id="{id}"'
                cursor.execute(query)
                connection.commit()
                return json.dumps(cursor.fetchone(),{'SUCCESS':'​​The product was deleted successfully',"CODE": 201})
   except:
           return json.dumps({'error':'​The product was not deleted due to an error',"CODE": 404})     
       
    
@delete('/category/<id>')
def getProdcut(id):
   try:
        with connection.cursor() as cursor:
                query= f'select *  FROM categories WHERE id="{id}"'
                cursor.execute(query)
                if cursor.rowcount == 0:
                  return json.dumps({'ERROR':"product not found","CODE": 404})
                else:        
                        query= f'delete  FROM categories WHERE id="{id}"'
                        cursor.execute(query)
                        connection.commit()
                        return json.dumps({'SUCCESS':'​​​The category was deleted successfully',"CODE": 201})
   except Exception as e:
           return json.dumps({'ERROR':'​The category was not deleted due to an error:'+repr(e),"CODE": 404,"MSG":"Category not found"})     

@get("/products")
def products():
    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM  product"
            cursor.execute(query)
        return json.dumps({'PRODUCTS':cursor.fetchall(),'SUCCESS':"Products fetched","CODE": 200})
    except:
         return json.dumps({'ERROR':"​internal error",'CODE': 500})        
       
@get('/category/<id>/products')
def loadProducts(id):
   try:
        with connection.cursor() as cursor:
                query= f'SELECT * FROM product WHERE category="{id}"'
                cursor.execute(query)
                if cursor.rowcount == 0:
                  return json.dumps({'ERROR':"category not found","CODE": 404})
                return json.dumps({'PRODUCTS':cursor.fetchall(),'SUCCESS':"Products fetched","CODE": 200})
   except:
         return json.dumps({'ERROR':"​internal error",'CODE': 500}) 

@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='js')

@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='css')


@get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='images')

run(host='localhost',port=argv[1],debug=True,reloader=True)
