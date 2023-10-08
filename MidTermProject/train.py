import pandas as pd
import numpy as np
from collections import Counter
import re
import pickle
import json

# plotting 
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

# data preparation and splitting 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import RepeatedStratifiedKFold

# ML models 
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

# metrics and parameters selection
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import roc_auc_score


df = pd.read_csv('data/Leukemia_GSE28497.csv')

print ('number of samples(patients): %s' % df.shape[0])
print ('number of features(gene probes): %s' % str(df.shape[1]-1))
print ('number of classes(tumour types): %s' % str(df.type.nunique()))



# split train/test/val
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=1)

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = df_train.type.values
y_val = df_val.type.values
y_test = df_test.type.values
y_full_train = df_full_train.type.values

del df_train['type']
del df_val['type']
del df_test['type']
del df_full_train['type']

del df_train['samples']
del df_val['samples']
del df_test['samples']
del df_full_train['samples']

X_train = df_train.values
X_test = df_test.values
X_val = df_val.values
X_full_train = df_full_train.values

# save data for testing the model later on a serving stage
data=df_val.iloc[0].T[2:].to_dict()
with open('B-CELL_ALL_MLL.json', 'w') as f:
    json.dump(data, f)

data=df_val.iloc[16].T[2:].to_dict()
with open('B-CELL_ALL_HYPO.json', 'w') as f:
    json.dump(data, f)

data=df_val.iloc[21].T[2:].to_dict()
with open('B-CELL_ALL_HYPERDIP.json', 'w') as f:
    json.dump(data, f)

data=df_val.iloc[25].T[2:].to_dict()
with open('B-CELL_ALL_ETV6-RUNX1.json', 'w') as f:
    json.dump(data, f)

data=df_val.iloc[4].T[2:].to_dict()
with open('B-CELL_ALL_T-ALL.json', 'w') as f:
    json.dump(data, f)

# GridSearch for parameters of multiclass logistic regression
print ('start GridSearchCV for parameters')
std_slc = StandardScaler()
pca = PCA()
logistic_Reg = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=2000)

pipe = Pipeline(steps=[('std_slc', std_slc),
                        ('pca', pca),
                        ('logistic_Reg_Multiclass', logistic_Reg)])

n_components = [40, 50, 70, 90, 100, 105, 120, 130]
C = [0.001,0.005, 0.01, 0.1, 1, 10]
penalty = ['l2']

parameters = dict(pca__n_components=n_components,
                  logistic_Reg_Multiclass__C=C,
                  logistic_Reg_Multiclass__penalty=penalty)


clf_GS = GridSearchCV(pipe, parameters, cv=5, verbose=10, scoring='roc_auc_ovr')  
clf_GS.fit(X_train, y_train)

print('Best C:', clf_GS.best_estimator_.get_params()['logistic_Reg_Multiclass__C'])
print('Best Number Of Components:', clf_GS.best_estimator_.get_params()['pca__n_components'])
print(); print(clf_GS.best_estimator_.get_params()['logistic_Reg_Multiclass'])


# final model: scores of validation
pipe = Pipeline(steps=[('std_slc', std_slc),
                        ('pca', pca),
                        ('logistic_Reg_Multiclass', logistic_Reg)])

print ('roc_auc_ovr score on validation:', pipe.set_params(logistic_Reg_Multiclass__penalty='l2', 
                logistic_Reg_Multiclass__C=clf_GS.best_estimator_.get_params()['logistic_Reg_Multiclass__C'],
                pca__n_components=clf_GS.best_estimator_.get_params()['pca__n_components'],
                logistic_Reg_Multiclass__max_iter=2000).fit(X_train, y_train).score(X_val, y_val))


# use model 
def train(df_train, y_train, C, pca_components, l='l2'):
    '''
    create a pipeline 
    train logistic regression 
    '''
    std_slc = StandardScaler()
    pca = PCA()
    logistic_Reg = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=2000)

    pipe = Pipeline(steps=[('std_slc', std_slc),
                        ('pca', pca),
                        ('logistic_Reg_Multiclass', logistic_Reg)])


    dicts = df_train.to_dict(orient='records')

    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)

    pipe.set_params(logistic_Reg_Multiclass__penalty=l, 
                logistic_Reg_Multiclass__C=C,
                pca__n_components=pca_components,
                logistic_Reg_Multiclass__max_iter=2000).fit(X_train, y_train)

    return dv, pipe


def predict(df, dv, model):
    dicts = df.to_dict(orient='records')

    X = dv.transform(dicts)
    y_pred = model.predict_proba(X)#[:, 1]

    return y_pred


dv, model = train(df_full_train, y_full_train, 
                  C=clf_GS.best_estimator_.get_params()['logistic_Reg_Multiclass__C'],
                  pca_components=clf_GS.best_estimator_.get_params()['pca__n_components'])

y_pred = predict(df_val, dv, model)

micro_roc_auc_ovr = roc_auc_score(
    y_val,
    y_pred,
    multi_class="ovr",
    average="micro",
)

# Save the model
C = str(clf_GS.best_estimator_.get_params()['logistic_Reg_Multiclass__C'])
n = str(clf_GS.best_estimator_.get_params()['pca__n_components'])
output_file = "model.C=%s.n=%s.bin" % (C,n)

print ('model is saved as ' + output_file)

with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)