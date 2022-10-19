import image_processing
import imageio
import connect_database
import base64
import pickle
import numpy as np

def predict_criminal(request,db):
    model_name="HoeffdingTree"
    suspect=request.files['suspect']
    suspect_encoding=image_processing.whirldata_face_encodings(imageio.imread(suspect))
    #print(suspect_encoding)
    try:
        encoded_model=connect_database.retrive_model(model_name,db)[-1][0]
        serialized_model=base64.b64decode(encoded_model)
        retrived_model=pickle.loads(serialized_model)
        
        
    except Exception as thrown:
        print(thrown)
    
    sus_encoding=np.array([suspect_encoding])
    ans=retrived_model.predict(sus_encoding)
    return ans[0]
    


    


    