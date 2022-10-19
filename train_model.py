from sklearn.linear_model import SGDClassifier
from sklearn.datasets import make_classification
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import connect_database
import pickle
import base64

db=connect_database.connect_sql()

X,Y=make_classification(n_samples=200,n_features=4,random_state=1,n_classes=2)
clf = SGDClassifier(alpha=.0001, loss='log_loss', penalty='l2', n_jobs=-1, shuffle=True)

X=pd.DataFrame(X,columns=['col1','col2','col3','col4'])
Y=pd.Series(Y)

X1,X2,Y1,Y2=train_test_split(X,Y,test_size=0.6)
X2_train,X2_test,Y2_train,Y2_test=train_test_split(X2,Y2,test_size=0.2)

clf.partial_fit(X1, Y1, classes=[0,5])
print(accuracy_score(Y2_test,clf.predict(X2_test)))
model_obj=pickle.dumps(clf)
model_obj_b64=base64.b64encode(model_obj)
connect_database.insert_model("SGDClassifier",model_obj_b64,db)

retrived_obj_b64=connect_database.retrive_model("SGDClassifier",db)[0][0]
retrived_obj=base64.b64decode(retrived_obj_b64)
retrived_model=pickle.loads(retrived_obj)

retrived_model.partial_fit(X2_train,Y2_train,classes=[0,5])
print(accuracy_score(Y2_test,retrived_model.predict(X2_test)))



