import pymysql

connection =pymysql.connect(host='localhost',
                            user='root',
                            password='root',
                            db='imdb',
                            cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        cursor.execute("alter table actors add column num_of_movies int")
        cursor.execute("UPDATE actors AS t1 INNER JOIN cast AS t2 ON t1.id = t2.actor_id SET t1.num_of_movies = t2.movie_id")
        connection.commit()
finally:            
    connection.close()        