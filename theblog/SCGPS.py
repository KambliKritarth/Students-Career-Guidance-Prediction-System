import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score

dataset = pd.read_csv('CSEsubjects0.csv')
#Replace zeroes
'''zero_not_accepted = ['Database Fundamentals','Software Development', 'Programming Skills']

for column in zero_not_accepted:
    dataset[column] = dataset[column].replace(0,np.NaN)
    mean = int(dataset[column].mean(skipna=True))
    dataset[column] = dataset[column].replace(np.NaN,mean)'''

# split dataset
X = dataset.iloc[:, 0:11]
y = dataset.iloc[:, 12]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.2)

#feature scaling
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

len(y)

import math
math.sqrt(462)

# Define the model: Init K-NN
classifier = KNeighborsClassifier(n_neighbors=316, p=11,metric='euclidean')

# Fit Model
classifier.fit(X_train, y_train)

# Predict the test set results
y_pred = classifier.predict(X_test)
y_pred

# Evaluate Model
cm = confusion_matrix(y_test, y_pred)
print (cm)
print(f1_score(y_test, y_pred, average='micro'))

print(accuracy_score(y_test, y_pred))
#saving model as a pickle
import pickle
pickle.dump(classifier,open("student_career_guidance_system_ml_model.sav", "wb"))
pickle.dump(sc_X, open("scaler.sav", "wb"))