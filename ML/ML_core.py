import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from collections import Counter

data = pd.read_csv('mypay2.csv')

data = data.dropna()

arr = [i for i in range(len(set(data['was'])))]
# encode = {list(set(data['was']))[i] : arr[i] for i in range(len(set(data['was'])))}
encode = dict(zip(list(set(data['was'])), arr))
# encode = dict(enumerate(list(set(data['was']))))

data['was'] = [encode[i] for i in data['was']]

X = data.iloc[:, 1:2]
y = data.iloc[:, 0:1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=20, random_state=23)

# Fitting
tdc = DecisionTreeClassifier()
tdc.fit(X_train, y_train)

y_pred = tdc.predict(X_test)

print(accuracy_score(y_test, y_pred))


def pred(value):
    predicted = int(tdc.predict([[value]]))
    for name, p in encode.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
        if p == predicted:
            return name
