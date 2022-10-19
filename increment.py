from sklearn.linear_model import SGDClassifier
from sklearn.datasets import make_classification
import image_processing
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pickle
import base64
import imageio
import numpy as np
from skmultiflow.trees import HoeffdingAdaptiveTreeClassifier
tree = HoeffdingAdaptiveTreeClassifier()

X,Y=make_classification(n_samples=100,n_features=5,random_state=1,n_classes=2)
print(X)
print(Y)
# tree.partial_fit(X,Y)
# tree.partial_fit([[1,0,0,0,1]],[1])
clf = SGDClassifier(alpha=.0001, loss='log_loss', penalty='l2', n_jobs=-1,shuffle=True)
# #clf.partial_fit(X,Y,classes=[0,1,2])


# print(tree.predict([[0]*128]))

X1=image_processing.whirldata_face_encodings(imageio.imread("test/boa1.jpg"))
X=np.array([X1])
print(X)
Y=np.array([0])
print(Y)
print(X.shape)
print(Y.shape)
tree.partial_fit(X,Y)
encoded=base64.b64encode(pickle.dumps(tree))

X1=image_processing.whirldata_face_encodings(imageio.imread("test/boa2.jpg"))
X=np.array([X1])
Y=np.array([0])
tree=pickle.loads(base64.b64decode(encoded))
tree.partial_fit(X,Y)
# clf.partial_fit(X,[Y],classes=2)

X1=image_processing.whirldata_face_encodings(imageio.imread("test/boa3.jpg"))
X=np.array([X1])
Y=np.array([0])
tree.partial_fit(X,Y)
# clf.partial_fit([X],[Y],classes=2)

X1=image_processing.whirldata_face_encodings(imageio.imread("test/chiru1.jpg"))
X=np.array([X1])
Y=np.array([1])
tree.partial_fit(X,Y)
# clf.partial_fit([X],[Y],classes=2)

X1=image_processing.whirldata_face_encodings(imageio.imread("test/chiru2.jpg"))
X=np.array([X1])
Y=np.array([1])
tree.partial_fit(X,Y)

# clf.partial_fit([X],[Y],classes=2)

X1=image_processing.whirldata_face_encodings(imageio.imread("test/chiru3.jpg"))
X=np.array([X1])
Y=np.array([2])
tree.partial_fit(X,Y)
# clf.partial_fit([X],[Y],classes=2)

X1=image_processing.whirldata_face_encodings(imageio.imread("test/t1.jpg"))
X=np.array([X1])
Y=np.array([2])
tree.partial_fit(X,Y)

X1=image_processing.whirldata_face_encodings(imageio.imread("test/t2.jpg"))
X=np.array([X1])
Y=np.array([2])
tree.partial_fit(X,Y)


X1=image_processing.whirldata_face_encodings(imageio.imread("test/t3.jpg"))
X=np.array([X1])
Y=np.array([2])
tree.partial_fit(X,Y)


X1=image_processing.whirldata_face_encodings(imageio.imread("test/m1.jpg"))
X=np.array([X1])
Y=np.array([3])
tree.partial_fit(X,Y)

X1=image_processing.whirldata_face_encodings(imageio.imread("test/m2.jpg"))
X=np.array([X1])
Y=np.array([3])
tree.partial_fit(X,Y)

X1=image_processing.whirldata_face_encodings(imageio.imread("test/m3.jpg"))
X=np.array([X1])
Y=np.array([3])
tree.partial_fit(X,Y)


X1=image_processing.whirldata_face_encodings(imageio.imread("test/ssr1.jpg"))
X=np.array([X1])
Y=np.array([4])
tree.partial_fit(X,Y)

X1=image_processing.whirldata_face_encodings(imageio.imread("test/ssr2.jpg"))
X=np.array([X1])
Y=np.array([4])
tree.partial_fit(X,Y)

X1=image_processing.whirldata_face_encodings(imageio.imread("test/ssr3.jpg"))
X=np.array([X1])
Y=np.array([4])
tree.partial_fit(X,Y)



X1=image_processing.whirldata_face_encodings(imageio.imread("test/m2.jpg"))
X=np.array([X1])
print(X.shape)

print(tree.predict(X)) 


