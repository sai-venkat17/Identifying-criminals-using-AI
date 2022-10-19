import mysql.connector
from flask import Flask
#from flaskext.mysql import MySQL
def connect_sql():
    # app = Flask(__name__)
    # mysql = MySQL()
    # app.config['MYSQL_DATABASE_USER'] = 'root'
    # app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
    # app.config['MYSQL_DATABASE_DB'] = 'IDBJ'
    # app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    # mysql.init_app(app)
    # return mysql.connect()
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="IDBJ",
    auth_plugin='mysql_native_password'
    )
    return mydb

def insert_model(name,b64_model,db):
    my_cursor=db.cursor()
    #query="delete from models"
    #db.commit()
    query='insert into models (name,model) values(%s,%s)'
    args=(name,b64_model)
    my_cursor.execute(query,args)
    db.commit()

def retrive_model(name,db):
    my_cursor=db.cursor()
    query="select model from models where name='"+name+"'"
    my_cursor.execute(query)
    x=my_cursor.fetchall()
    return x

def insert_criminal(name,id,age,crime,photo1,photo2,photo3,db):
    my_cursor=db.cursor()
    id=int(id)
    age=int(age)
    query="insert into criminals (name,id,age,crime,photo1,photo2,photo3) values(%s,%s,%s,%s,%s,%s,%s)"
    args=(name,id,age,crime,photo1,photo2,photo3)
    my_cursor.execute(query,args)
    db.commit()

def insert_derived(db,id,aug_images_encoded,centroid_encoding_encoded):
    my_cursor=db.cursor()
    id=int(id)
    query="insert into derived (id,all_photos,centroid_encoding) values(%s,%s,%s)"
    args=(id,aug_images_encoded,centroid_encoding_encoded)
    my_cursor.execute(query,args)
    db.commit()

def insert_suspect(db,identified_id,location,crime,photo_uploaded):
    my_cursor=db.cursor()
    identified_id=int(identified_id)
    query="insert into complaint (identified_id,location,crime,photo_uploaded) values(%s,%s,%s,%s)"
    args=(identified_id,location,crime,photo_uploaded)
    my_cursor.execute(query,args)
    db.commit()

def delete_all(db):
    #db=connect_sql()
    my_cursor=db.cursor()
    query1="delete from complaint"
    query2="delete from criminals"
    query3="delete from derived"
    query4="delete from models"
    my_cursor.execute(query1)
    my_cursor.execute(query2)
    my_cursor.execute(query3)
    my_cursor.execute(query4)
    db.commit()
def get_name(db,id):
    my_cursor=db.cursor()
    query="select name from criminals where id='"+id+"'"
    my_cursor.execute(query)
    x=my_cursor.fetchall()
    return x



    



    

    



