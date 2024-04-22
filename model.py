# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R0amnDckD1MX3tZKJpjnBqdhTk8UCjpJ
"""

import pandas as pd
import numpy as np
np.set_printoptions(suppress=True)

df = pd.read_csv('/content/survey.csv')
df.head()

df.shape

df.info()

df.isnull().sum()

df['state'].fillna(df['state'].mode()[0],inplace=True)
df['self_employed'].fillna(df['self_employed'].mode()[0],inplace=True)
df['work_interfere'].fillna("N/A",inplace=True)
df['comments'].fillna(df['comments'].mode()[0],inplace=True)

df.Age.value_counts()

df.index[df['Age'] == 99999999999 ]

df1 = df
df1.drop(391,inplace=True)

df1.index[df['Age'] == -1 ]

df1.drop(1127,inplace=True)

df1.index[df['Age'] == -29 ]



df1.index[df['Age'] == -1726 ]

df1.drop(715 ,inplace=True)

df1.Age.value_counts()

df1.no_employees.value_counts()

age_median = df1['Age'].median()
age_median

df.shape

df.describe()

df.Gender.nunique()

df.Country.nunique()

df.state.nunique()

df.self_employed.nunique()

df.family_history.nunique()

df.work_interfere.nunique()

df.work_interfere.value_counts()

df.leave.nunique()

df.no_employees.nunique()

df.mental_health_consequence.nunique()

df.phys_health_consequence.nunique()

df.supervisor.nunique()

df.mental_health_interview.nunique()

df.phys_health_interview.nunique()

df.mental_vs_physical.nunique()

df.obs_consequence.nunique()

df.comments.nunique()

df.coworkers.nunique()

df.remote_work.nunique()

df.benefits.nunique()

df.care_options.nunique()

df.wellness_program.nunique()

df.anonymity.nunique()

df.seek_help.nunique()

df.corr()

import seaborn as sns

sns.boxplot(df.Age)

q1 = df.Age.quantile(0.25)
q3 = df.Age.quantile(0.75)
print(q1)
print(q3)

IQR =q3-q1

upper_limit = q3+1.5*IQR
upper_limit

lower_limit = q1-1.5*IQR
lower_limit

df.median()

df['Age'] = np.where(df['Age']>upper_limit,31,df['Age'])

sns.boxplot(df.Age)

df['Age'] = np.where(df['Age']<lower_limit,31,df['Age'])

sns.boxplot(df.Age)

df['Gender'].replace(['Male','male','M','m','Male ','Cis Male','Man','cis male','Mail','Male-ish','Male (CIS)','Cis Man','msle','Malr','Mal','maile','Make',],'Male',inplace =True)

df['Gender'].replace(['Female ','female', 'F','f','Woman','Female','femail','Cis female','cis-female/femme','Femake','Female (cis)','woman','Cis Female',],'Female',inplace =True)

df['Gender'].replace(['Female (trans)','queer/she/they','non-binary','fluid','queer','Androgyne','Trans-female','male leaning androgynous','Agender','A little about you','Nah','All','ostensibly male, unsure what that really means','Genderqueer','Enby','p','Neuter','something kinda male?','Guy (-ish) ^_^','Trans woman',],'Non-Binary',inplace = True)



df.head()

df.Gender.nunique()

df.Gender.value_counts()

import matplotlib.pyplot as plt
sns.displot(df["Age"])
plt.title("Distribution - Age")
plt.xlabel("Age")

#bivariate analysis
#employment and treatment
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.subplot(1, 1, 1)  # Adjust the subplot as needed
sns.countplot(data=df, x='self_employed', hue='treatment')
plt.title("Employment type and Treatment")
plt.show()

#family history and treatment
plt.figure(figsize=(10,40))
plt.subplot(9,2,2)
sns.countplot(data=df , x='family_history' , hue = 'treatment')
plt.title('family history and treatment')
plt.show

#work interference and treatment
plt.figure(figsize=(10,40))
plt.subplot(9,2,3)
sns.countplot(data=df , x='work_interfere',hue = 'treatment' )
plt.title('work interfereance ')
plt.show()

#worktype and treatment
plt.figure(figsize=(10,40))
plt.subplot(9,2,4)
sns.countplot(data=df , x='remote_work',hue = 'treatment' )
plt.title('work type ')
plt.show()

#company and treatment
plt.figure(figsize=(10,40))
plt.subplot(9,2,5)
sns.countplot(data=df , x='tech_company',hue = 'treatment' )
plt.title('company' )
plt.show()

#benfits and treatment
plt.figure(figsize=(10,40))
plt.subplot(9,2,6)
sns.countplot(data=df , x='benefits',hue = 'treatment' )
plt.title('benefits')
plt.show()

#care options and treatment
plt.figure(figsize=(10,40))
plt.subplot(9,2,7)
sns.countplot(data=df , x='care_options',hue = 'treatment' )
plt.title('care options')
plt.show()

#mental vs physical health
plt.figure(figsize=(10,40))
plt.subplot(9,2,8)
sns.countplot(data=df , x='mental_vs_physical',hue = 'treatment' )
plt.title('Equal importance to mental and physical health')
plt.show()

#wellness program and treatment
plt.figure(figsize=(10,40))
plt.subplot(9,2,9)
sns.countplot(data=df , x='wellness_program',hue = 'treatment' )
plt.title('wellness program')
plt.show()

#anonymity and treatment
plt.figure(figsize=(10,40))
plt.subplot(9,2,10)
sns.countplot(data=df , x='anonymity',hue = 'treatment' )
plt.title('anonymity ')
plt.show()

#leave and treatment
plt.figure(figsize=(10,40))
plt.subplot(9,2,11)
sns.countplot(data=df , x='leave',hue = 'treatment' )
plt.title('leave ')
plt.show()

#mental_health_consequence and treatment
plt.figure(figsize=(10,40))
plt.subplot(9,2,12)
sns.countplot(data=df , x='mental_health_consequence',hue = 'treatment' )
plt.title('mental health consequence ')
plt.show()

#phys_health_consequence
plt.figure(figsize=(10,40))
plt.subplot(9,2,13)
sns.countplot(data=df , x='phys_health_consequence',hue = 'treatment' )
plt.title('physical health consequences')
plt.show()

#coworkers and treatment
plt.figure(figsize=(10,40))
plt.subplot(9,2,3)
sns.countplot(data=df , x='coworkers',hue = 'treatment' )
plt.title('Discussion with coworkers')
plt.show()

#supervisor and treatment
plt.figure(figsize=(10,40))
plt.subplot(9,2,14)
sns.countplot(data=df , x='supervisor',hue = 'treatment' )
plt.title('Discussion with supervisor')
plt.show()

#mental_health_interview and treatment
plt.figure(figsize=(10,40))
plt.subplot(9,2,15)
sns.countplot(data=df , x='mental_health_interview',hue = 'treatment' )
plt.title('Discussion with interviewer(mental)')
plt.show()

#phys_health_interview and treatment
plt.figure(figsize=(10,40))
plt.subplot(9,2,16)
sns.countplot(data=df , x='phys_health_interview',hue = 'treatment' )
plt.title('Discussion with interviewer(Physical)')
plt.show()

#obs_consequence and treatment
plt.figure(figsize=(10,40))
plt.subplot(9,2,17)
sns.countplot(data=df , x='obs_consequence',hue = 'treatment' )
plt.title('consequence after Disclosure ')
plt.show()

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

df.Gender=le.fit_transform(df.Gender)
df.head()
df.Country=le.fit_transform(df.Country)
df.state=le.fit_transform(df.state)
df.self_employed=le.fit_transform(df.self_employed)
df.family_history=le.fit_transform(df.family_history)
df.work_interfere=le.fit_transform(df.work_interfere)
df.no_employees=le.fit_transform(df.no_employees)
df.leave=le.fit_transform(df.leave)
df.mental_health_consequence=le.fit_transform(df.mental_health_consequence)
df.phys_health_consequence=le.fit_transform(df.phys_health_consequence)
df.coworkers=le.fit_transform(df.coworkers)
df.supervisor=le.fit_transform(df.supervisor)
df.mental_health_interview=le.fit_transform(df.mental_health_interview)
df.phys_health_interview=le.fit_transform(df.phys_health_interview)
df.obs_consequence=le.fit_transform(df.obs_consequence)
df.mental_vs_physical=le.fit_transform(df.mental_vs_physical)
df.mental_vs_physical=le.fit_transform(df.mental_vs_physical)
df.remote_work=le.fit_transform(df.remote_work)
df.benefits=le.fit_transform(df.benefits)
df.care_options=le.fit_transform(df.care_options)
df.wellness_program=le.fit_transform(df.wellness_program)
df.seek_help=le.fit_transform(df.seek_help)
df.anonymity=le.fit_transform(df.anonymity)
df.tech_company=le.fit_transform(df.tech_company)

df.head()

df.comments=le.fit_transform(df.comments)
df.head()

df.treatment=le.fit_transform(df.treatment)
y=df['treatment']
y

x=df.drop(columns = ['treatment'],axis=1)



x.head()

x_new=x.drop(columns = ['Timestamp'],axis=1)

x_new = x_new.drop(columns= ['state'],axis =1)
x_new = x_new.drop(columns= ['Country'],axis =1)
x_new = x_new.drop(columns= ['comments'],axis =1)

x_new.head()

from sklearn.preprocessing import MinMaxScaler
scale = MinMaxScaler()

x_scaled = pd.DataFrame(scale.fit_transform(x_new),columns=x_new.columns)
x_scaled.head()

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x_scaled,y,test_size=0.3,random_state=0)

from sklearn.tree import DecisionTreeClassifier
model1 = DecisionTreeClassifier()
model1.fit(x_train,y_train)
d_y_predict = model1.predict(x_test)
d_y_predict

from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

print('Testing accuracy = ', accuracy_score(y_test,d_y_predict))

d_y_predict_train = model1.predict(x_train)

print('Training accuracy = ', accuracy_score(y_train,d_y_predict_train))

from sklearn.ensemble import RandomForestClassifier ,AdaBoostClassifier ,GradientBoostingClassifier
model2 = RandomForestClassifier(random_state=99)
model2.fit(x_train,y_train)
l_y_predict = model2.predict(x_test)

l_y_predict_train = model2.predict(x_train)

print('Testing accuracy = ', accuracy_score(y_test,l_y_predict))
print('Training accuracy = ', accuracy_score(y_train,l_y_predict_train))

from sklearn.linear_model import LogisticRegression
model3 = LogisticRegression()
model3.fit(x_train,y_train)
lr_y_predict = model3.predict(x_test)

lr_y_predict_train = model3.predict(x_train)

print('Testing accuracy = ', accuracy_score(y_test,lr_y_predict))
print('Training accuracy = ', accuracy_score(y_train,lr_y_predict_train))

model4 = AdaBoostClassifier()
model4.fit(x_train,y_train)
a_y_predict = model4.predict(x_test)
a_y_predict_train = model4.predict(x_train)
print('Testing accuracy = ', accuracy_score(y_test,a_y_predict))
print('Training accuracy = ',accuracy_score(y_train,a_y_predict_train))

model5 = GradientBoostingClassifier()
model5.fit(x_train,y_train)
g_y_predict = model5.predict(x_test)
g_y_predict_train = model5.predict(x_train)
print('Testing accuracy = ', accuracy_score(y_test,g_y_predict))
print('Training accuracy = ',accuracy_score(y_train,g_y_predict_train))

from sklearn.svm import SVC



model6 = SVC()
model6.fit(x_train,y_train)
s_y_predict = model6.predict(x_test)
print('Testing accuracy = ', accuracy_score(y_test,s_y_predict))

"""RandomForest has best accuracy

"""

abc = AdaBoostClassifier(random_state=99)
abc.fit(x_train,y_train)
pred_abc = abc.predict(x_test)
print("accuracy of adaboost = ",accuracy_score(y_test,pred_abc))



import pickle
pickle.dump(abc,open('model.pkl','wb'))

# import joblib

# # Assuming your model is named 'model'
# joblib.dump(abc, 'model.pkl')

from google.colab import files

files.download('model.pkl')

model2.predict([[1,1,1,1,1 ,1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1]])