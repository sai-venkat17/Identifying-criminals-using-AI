from time import sleep
import requests
import os

# def insert_criminal():
#     url = "http://localhost:4999/insert_criminal"

#     payload={'name': 'manikanta',
#     'id': '1',
#     'age': '25',
#     'crime': 'theft'}
#     files=[
#     ('photo1',('khan.jpg',open('/Users/venkatramadugula/Desktop/INTELLIGENT DATABASE/IDBJ/khan.jpg','rb'),'image/jpeg')),
#     ('photo2',('mahesh1.jpg',open('/Users/venkatramadugula/Desktop/INTELLIGENT DATABASE/IDBJ/mahesh1.jpg','rb'),'image/jpeg')),
#     ('photo3',('mani2.jpg',open('/Users/venkatramadugula/Desktop/INTELLIGENT DATABASE/IDBJ/mani2.jpg','rb'),'image/jpeg'))
#     ]


#     response = requests.request("POST", url,  data=payload, files=files)

#     return response.text

def insert_data():
    files=os.listdir("./test")
    files.sort()
    print(files)
    for i in range(0,len(files),4):
        name=files[i].split(".")[0]
        id=i
        crime="theft"
        files=[
        ('photo1',("/Users/venkatramadugula/Desktop/INTELLIGENT DATABASE/IDBJ/identifying-criminals-using-AI/test/"+files[i],open(files[i],'rb'),'image/jpeg')),
        ('photo2',("/Users/venkatramadugula/Desktop/INTELLIGENT DATABASE/IDBJ/identifying-criminals-using-AI/test/"+files[i+1],open(files[i+1],'rb'),'image/jpeg')),
        ('photo3',("/Users/venkatramadugula/Desktop/INTELLIGENT DATABASE/IDBJ/identifying-criminals-using-AI/test/"+files[i+2],open(files[i+2],'rb'),'image/jpeg'))
        ]
        payload={
            'name':name,
            'id':str(id),
            'age':'18',
            'crime':crime
        }
        requests.request("POST","http://localhost:4999/insert_criminal",data=payload,files=files)
    

insert_data()
