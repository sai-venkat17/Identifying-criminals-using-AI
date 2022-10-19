from flask import Flask,request,redirect
import connect_database
import base64
import image_processing
import imageio.v2 as imageio
import pickle

def insert_criminal(request):
    #id,name,age,timestamp,3photos,crime

    id=request.form['id']
    name=request.form['name']
    age=request.form['age']
    crime=request.form['crime']

    photo1=base64.b64encode(request.files['photo1'].read())
    photo2=base64.b64encode(request.files['photo2'].read())
    photo3=base64.b64encode(request.files['photo3'].read())
    print("2. Encoded Photos of criminals")

    # aug_images=[]
    # for i in image_processing.aug_images(imageio.imread(request.files['photo1'])):
    #     aug_images.append(i)
    
    # for i in image_processing.aug_images(imageio.imread(request.files['photo2'])):
    #     aug_images.append(i)
    
    # for i in image_processing.aug_images(imageio.imread(request.files['photo3'])):
    #     aug_images.append(i)
    
    # aug_images_encoded=base64.b64encode(pickle.dumps(aug_images))
    flags=0
    try:
        db=connect_database.connect_sql()
        print("3. Connected to database")
    except Exception as thrown:
        print("Cannot connect to database: ")
        print(thrown)
        flags=1

    try:
        connect_database.insert_criminal(name,id,age,crime,photo1,photo2,photo3,db)
        print("4. Inserted data to criminal database")
        image_processing.main(request,db)
        print("14. Successfully completed all tasks")
    except Exception as thrown:
        print("Cannot insert to database: ")
        print(thrown)
        flags=1
    if(flags==0):
        print("Inserted successful")
        return redirect("http://localhost:4999/insert_criminal")

    else:
        return "Insertion failed"
    
    


    


