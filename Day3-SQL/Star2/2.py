import pymysql

actors=[
    {"id":933,
     "full_name":"Lewis Abernathy",
     "gender":"M"},
    {"id":2547,
     "full_name":"Andrew Adamson",
     "gender":"M"},
    {"id":999997,
     "full_name":"Moshe Cohen",
     "gender":"M"},
    {"id":999998,
     "full_name":"Madona Dona",
     "gender":"F"},
    {"id":999999,
     "full_name":"Eli Bum",
     "gender":"M"}
   ]

connection =pymysql.connect(host='localhost',
                            user='root',
                            password='root',
                            db='imdb',
                            cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql="select  * from actors"
        cursor.execute(sql)
        result=cursor.fetchall()
        for actor in actors:
            sum=0
            for currentResult in result:
               if currentResult["id"] != actor["id"]:
                  sum+=1
            if sum==len(result):
                print("We are going to insert to DB:" + str(actor))     
                sql="insert into actors  values (%s,%s,%s)"
                val=(actor["id"],actor["full_name"],actor["gender"]) 
                cursor.execute(sql,val)
                connection.commit()
finally:            
    connection.close()        