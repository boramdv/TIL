# K-Digital Training 멀티캠퍼스 데이터 사이언스/엔지니어링
## 데이터 사이언스 과정
- 주교재 : 파이썬 머신러닝 완벽 가이드(권철민 지음, 위키북스)

### 210721 강의 요약

- data : fish length and weight data 
- kNN(k-Nearest Neighbors)  
`from sklearn.neighbors import KNeighborsClassifier`
- Hold-out Train data & Test data  
`from sklearn.model_selection import train_test_split`

- data : iris dataset  
`from sklearn.datasets import load_iris`
- Decision Tree  
`from sklearn.Tree import DecisionTreeClassifier`  
`from sklearn.metrics import accuracy_score`

### 210722 강의 요약

- data : iris dataset  
`from sklearn.datasets import load_iris`
- K-Fold Cross Validation  
`from sklearn.medel_selection import KFlod`  
- Stratified K-Fold Cross Validation  
`from sklearn.model_selection import StratifiedKFold`  
`from sklearn.model_selection import cross_val_score, cross_validate`
- GridSearch Cross Validation  
`from sklearn.model_selection import GridSearchCV`  

- Encoding  
`from sklearn.preprocessing import OneHotEncoder, LabelEncoder`  

- Normalization & Standardization  
`from sklearn.preprocessing import MinMaxScaler, StandardScaler`  

### 210723 강의 요약

- data : titanic.csv, MNIST dataset  
`from sklearn.datasets import load_digits`  

- Confusion Matrix  
`from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix`  
`from sklearn.metrics import precision_recall_curve`  

- ROC Curve, AUC score  
`from sklearn.metrics import roc_curve, roc_auc_score`  

- etc.  
`from sklearn.preprocessing import Binarizer`  
`from sklearn.base import BaseEstimator`  

### 210728 강의 요약

- data : iris dataset, Human Activity Recognition, breast cancer wisconsin dataset  
`from sklearn.datasets import load_iris`  
`from sklearn.datasets import load_breast_cancer`

- Decision Tree  
`sklearn.tree import DecisionTreeClassifier`  
- Decision Tree Visualization  
`from sklearn.tree import export_graphviz`  
`import graphviz`  
`from subprocess import call`  
`from IPython.display import Image`  

- Classification Sample  
`from sklearn.datasets import make_classification`

- Ensemble: Voting  
`from sklearn.ensemble import VotingClassifier`  

- Ensemble: Random Forest  
`from sklearn.ensemble import RandomForestClassifier`  

- Ensemble: Gradient Boosting  
`from sklearn.ensemble import GradientBoostingClassifier`

- etc.  
`import warnings  
warnings.filterwarnings('ignore')`  
`import time`

---

### 210805 강의 요약  
- DNN Classification & Regression  
  - Overfitting Issue  
    - L2 Regularization
    - Dropout
    - Batch Normalization
  - Early Stopping
- Data : MNIST, Boston Housing Price
