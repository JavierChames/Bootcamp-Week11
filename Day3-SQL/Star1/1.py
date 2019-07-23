import pymysql

actors=["Andrew Adamson","Actor1","Dicaprio","Jennifer Jaffe","Robert Ozasky"]

connection =pymysql.connect(host='localhost',
                            user='root',
                            password='root',
                            db='imdb',
                            cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql="select  full_name from actors"
        cursor.execute(sql)
        result=cursor.fetchall()
        for x in actors:
            sum=0
            for row in result:
               if x == row["full_name"]:
                   print("Actor:"+ x +" Exists in your list")
                   break
               else:
                   sum+=1              
            if sum==len(result):
                print("Actor:"+ x +" doesnt Exists in your list")
finally:            
    connection.close()        