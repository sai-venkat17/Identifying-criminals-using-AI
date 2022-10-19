from xml.dom.minidom import Identified
import image_processing
import imageio
import connect_database
import predict_criminal
import pickle
import base64
from flask import redirect
def report_criminal(request):
    db=connect_database.connect_sql()
    crime=request.form["crime"]
    location=request.form["location"]
    suspect=base64.b64encode(pickle.dumps(request.files['suspect']))
    identified_id=predict_criminal.predict_criminal(request,db)
    try:
        connect_database.insert_suspect(db,identified_id,location,crime,suspect)
        
    except Exception as thrown:
        print("Cannot insert suspect reported details")
        print(thrown)
    print("Reported Successfully and identified id is "+str(identified_id))
    print(connect_database.get_name(db,str(identified_id))[0][0])
    return redirect("http://localhost:4999/report_criminal")


    




    