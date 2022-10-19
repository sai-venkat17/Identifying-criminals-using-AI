import imageio.v2 as imageio
import imgaug as ia
import imgaug.augmenters as iaa
import ipyplot
import dlib
import numpy as np
import base64
import pickle
import connect_database
from skmultiflow.trees import HoeffdingAdaptiveTreeClassifier

def augment(input_img):
    #Horizontal Flip
    hflip= iaa.Fliplr(p=1.0)
    input_hf= hflip.augment_image(input_img)

    #Adding noise
    noise=iaa.AdditiveGaussianNoise(10,40)
    input_noise=noise.augment_image(input_img)

    #Changing contrast
    contrast=iaa.GammaContrast((0.5, 2.0))
    contrast_sig = iaa.SigmoidContrast(gain=(5, 10), cutoff=(0.4, 0.6))
    contrast_lin = iaa.LinearContrast((0.6, 0.4))
    input_contrast = contrast.augment_image(input_img)
    sigmoid_contrast = contrast_sig.augment_image(input_img)
    linear_contrast = contrast_lin.augment_image(input_img)
    
    aug_images=[input_img,input_hf,input_noise,input_contrast,sigmoid_contrast,linear_contrast]
    return aug_images

face_detector = dlib.get_frontal_face_detector()
pose_predictor_68_point = dlib.shape_predictor('./shape_predictor_68_face_landmarks.dat')
face_encoder = dlib.face_recognition_model_v1('./dlib_face_recognition_resnet_model_v1.dat')

def whirldata_face_detectors(img, number_of_times_to_upsample=1):
 #print("Whirl data face detectors called")
 return face_detector(img, number_of_times_to_upsample)

def whirldata_face_encodings(face_image,num_jitters=1):
 #print("Whilrdata face encodings called")
 face_locations = whirldata_face_detectors(face_image)
 #gives 68 points which indicates boundary of face
 #print("Detection complete")
 pose_predictor = pose_predictor_68_point
 #The pose will be predicted here
 predictors = [pose_predictor(face_image, face_location) for face_location in face_locations]
 #print("Predictors found "+str(len(predictors)))
 if(len(predictors)==0):
    return []
#Pose and image is passed to face encoder which will convert the face to 128 attribute value
 return [np.array(face_encoder.compute_face_descriptor(face_image, predictor, num_jitters)) for predictor in predictors][0]


def distance(enc1,enc2):
    if(len(enc1)!=len(enc2)):
        print("Error")
        return -1
    else:
        ans=0
        for i in range(len(enc1)):
            ans+=(enc1[i]-enc2[i])**2
        return ans**(1/2)

def centroid(encodings):
    ans=[]
    for i in range(len(encodings[0])):
        cur=0
        for j in range(len(encodings)):
            cur+=encodings[j][i]
        ans.append(cur/len(encodings))
    return ans
        


def find_encodings(aug_images):
    #print("Face encoding function called")
    face_encodings=[]
    for i in aug_images:
        temp=whirldata_face_encodings(i)
        face_encodings.append(temp)
    return face_encodings


def display(aug_images):
    labels=["Original","Horizontal","Added Noise","Gamma","Sigmoid","Linear"]
    for i in range(len(labels)):
        imageio.imwrite("aug_images/"+labels[i]+".png",aug_images[i])

def main(request,db):
    print("5. Image processing started")
    id=request.form['id']
    
    photo1=base64.b64encode(request.files['photo1'].read())
    photo2=base64.b64encode(request.files['photo2'].read())
    photo3=base64.b64encode(request.files['photo3'].read())

    aug_images=[]
    for i in augment(imageio.imread(request.files['photo1'])):
        aug_images.append(i)
    
    for i in augment(imageio.imread(request.files['photo2'])):
        aug_images.append(i)
    
    for i in augment(imageio.imread(request.files['photo3'])):
        aug_images.append(i)
    
    print("6. Augmented images length="+str(len(aug_images)))
    
    face_encodings=find_encodings(aug_images)
    for i in face_encodings:
        if(len(i)!=0):
            non_zero_encoding=i
            break
    for i in range(len(face_encodings)):
        if(len(face_encodings[i])==0):
            face_encodings[i]=non_zero_encoding
    
            
            
    #print("Found face encodings")
    centroid_encoding=centroid(face_encodings)

    print("7. Found centroid encoding length="+str(len(centroid_encoding)))

    aug_images_encoded=base64.b64encode(pickle.dumps(aug_images))
    
    centroid_encoding_encoded=base64.b64encode(pickle.dumps(centroid_encoding))

    try:
        connect_database.insert_derived(db,id,aug_images_encoded,centroid_encoding_encoded)
        print("8. Inserted centroid encoding values to derived database")
    except:
        print("Failed to insert into derived database")
    
    train_model(face_encodings,db,id)

def train_model(face_encodings,db,id):

    print("9. Starting training model")
    model_name="HoeffdingTree"

    try:
        retrived_model=connect_database.retrive_model(model_name,db)
        print("10. Reterived model from database")
    except Exception as thrown:
        print("Retriving model failed")
        print(thrown)
    #print(retrived_model)
    tree=None
    if(len(retrived_model)==0):
        tree=HoeffdingAdaptiveTreeClassifier()
        #tree=HoeffdingTree(nominal_attributes=['0','4','8','12','16'],grace_period=5)
        print("11. First time training")
    else:
        tree=pickle.loads(base64.b64decode(retrived_model[-1][0]))
        print("11. Training an already existing model in database")
    
    try:
        #print("***FACE_ENCODING***")
        # print(face_encodings)
        for i in face_encodings:
            #print(np.array([i]))
            #print(np.array([int(id)]))
            X=np.array([i])
            Y=np.array([int(id)])
            #print(X.shape)
            #print(Y.shape)
            #print(X)
            tree.partial_fit(X,Y)
            #print("PREDICTEX")
            #print(tree.predict(X))
        
        print("12. Fitted current data to the model")
    except Exception as thrown:
        print("Fitting failed")
        print(thrown)
    
    try:
        connect_database.insert_model(model_name,base64.b64encode(pickle.dumps(tree)),db)
        print("13. Reinserted model to database again")
    except Exception as thrown:
        print("Reinsertion into model database failed")
        print(thrown)


    





    

# aug_images=augment(imageio.imread("passport.jpg"))
# display(aug_images)
#print(centroid(find_encodings(aug_images)))
