# -*- coding: utf-8 -*-
"""Data Science Assignment

Automatically generated by Colaboratory.

Original file is located at https://colab.research.google.com/drive/1QRKdxP86RUu9xHFVWAZNXFOiH_-kwB_I

# WQD7001 Assignment 1

**Import Library**
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder


"""**Declare Data Path**"""

# Declare Data Path

cardio_data_csv = "cardio_data_processed.csv"
cardiao_data_path = cardio_data_csv
print(f"Data Path: {cardiao_data_path}")

"""**Load CSV**"""

# Load CSV
df = pd.read_csv(cardiao_data_path)
df_bp = pd.get_dummies(df, columns=['bp_category'], drop_first=True)
print(df)

"""**DF Info**"""

df.info()

"""**Describe DF**"""

df.describe()

"""**Check Missing Data**"""

#check missing values
df.isnull().sum()

"""**Describe Gender**"""

# Gender of the patient. Categorical variable (1: Female, 2: Male).
# Female
gender_female = df['gender'].value_counts()[1]
print(f"Female: {gender_female}")
print("Female Percentage: {:.2f}%".format((len(df[df.gender == 1]) / (len(df.gender))*100)))
# Male
gender_male = df['gender'].value_counts()[2]
print(f"Male: {gender_male}")
print("Male Percentage: {:.2f}%".format((len(df[df.gender == 2]) / (len(df.gender))*100)))

#plotting a pie chart of Genderwise disribution
plt.figure(figsize=(10,6))
df['gender'].value_counts().plot(kind='pie',autopct='%2.2f%%')
#plt.pie(df['gender'].value_counts(),autopct='%1.1f%%')
plt.title("Genderwise Distribution")
plt.xlabel('1: Female,2: Male')
plt.ylabel('')

"""**Gender vs Cardio**"""

ax = pd.crosstab(df.gender,df.cardio).plot(kind="bar",figsize=(10,6))
plt.title('Cardiovascular Diseases by Gender')
plt.xlabel('Gender (1 = Female, 2 = Male)')
plt.xticks(rotation=0)
plt.legend(["Absence", "Presence"])
plt.ylabel('Value Counts')
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 5), textcoords='offset points')
plt.show()

plt.figure(figsize=(10, 6))
sns.violinplot(x=df.gender,y=df.cardio,data=df)
plt.xlabel("Gender (1 = Female, 2 = Male)")
plt.show()

"""**Describe Age**"""

age_describe = df['age_years'].describe()
print(age_describe)
age_count = df['age_years'].value_counts()
print(f"Age   Value")
print(age_count)
pd.crosstab(df.age_years,df.gender).plot(kind="bar",figsize=(10,6))
# pd.crosstab(df['age_years'],df['gender']).plot.bar()

"""**Age vs Cardio**"""

pd.crosstab(df.age_years,df.cardio).plot(kind="bar",figsize=(10,6))
plt.title('Cardiovascular Diseases by Age')
plt.xlabel('age_years')
plt.ylabel('ratio')
plt.legend(["Absence", "Presence"])
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='cardio', y='age_years')
plt.title('Box Plot of Cardiovascular Diseases by Age')
plt.xlabel('Cardiovascular Disease (0: Absence, 1: Presence)')
plt.ylabel('Age')
plt.show()

"""**BP Categories**"""

#plotting a countplot of No of people in each B.P Categories
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='bp_category')
plt.xlabel("Blood Pressure Category")
plt.ylabel("Value Counts")
plt.title("No of people in each B.P Category")
plt.show()
df['bp_category'].value_counts().plot(kind='pie',autopct='%1.1f%%')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(x=df.age_years[df.cardio==0], y=df.bp_category[(df.cardio==0)], c="#32CD32")
plt.scatter(x=df.age_years[df.cardio==1], y=df.bp_category[(df.cardio==1)], c="#D2042D")
plt.legend(["Absence", "Presence"])
plt.xlabel("age_years")
plt.ylabel("Blood Pressure Category")
plt.show()
# violinplot
plt.figure(figsize=(10, 6))
sns.violinplot(y=df.cardio,x=df.bp_category,data=df)
plt.show()

plt.figure(figsize=(10, 6))
ax = pd.crosstab(df.bp_category,df.cardio).plot(kind="bar",figsize=(25,8))
plt.title('Cardiovascular diseases by BP_Category')
plt.xlabel('BP_Category')
plt.xticks(rotation=0)
plt.ylabel('Counts')
plt.legend(["Absence", "Presence"])
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 5), textcoords='offset points')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='bp_category', y='cardio')
plt.title('Box Plot of BP Category vs. Cardiovascular Disease')
plt.ylabel('Cardiovascular Disease (0: Absence, 1: Presence)')
plt.xlabel('BP Category')
plt.show()

# sns.swarmplot(x='cardio',y='ap_hi',hue='bp_category', data=df, size=6)
# plt.xlabel('Cardiovascular Disease (0: Absence, 1: Presence)')
# plt.ylabel('Systolic blood pressure')
# plt.show()

"""**Describe Smoking Status**"""

#plotting a pie chart of No of people with smoking status
df['smoke'].value_counts().plot(kind='pie',autopct='%1.1f%%')
plt.title("No of people with smoking status")
plt.xlabel('0: Non-smoker,1: Smoker')

plt.scatter(x=df.age_years[df.cardio==0], y=df.smoke[(df.cardio==0)], c="#32CD32")
plt.scatter(x=df.age_years[df.cardio==1], y=df.smoke[(df.cardio==1)], c="#D2042D")
plt.legend(["Absence", "Presence"])
plt.xlabel("age_years")
plt.ylabel("Smoke (0: Non-Smoker, 1:Smoker)")
plt.show()
# violinplot
sns.violinplot(x=df.cardio,y=df.smoke,data=df)
plt.title('Violin Plot of Cardiovascular Diseases by Smoking Status')
plt.ylabel('Cardiovascular Disease (0: Absence, 1: Presence)')
plt.xlabel('Smoking status (0: Non-Smoker, 1:Smoker)')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='smoke', y='cardio')
plt.title('Box Plot of Smoking vs. Cardiovascular Disease')
plt.ylabel('Cardiovascular Disease (0: Absence, 1: Presence)')
plt.xlabel('Smoke (0: Non-Smoker, 1:Smoker)')
plt.show()

"""**Describe Alcohol Drink Status**"""

#plotting a pie chart of No of people with drinking status
df['alco'].value_counts().plot(kind='pie',autopct='%1.1f%%')
plt.title("No of people with alcohol drinking status")
plt.xlabel('0: Does not consume alcohol, 1: Consumes alcohol')

plt.scatter(x=df.age_years[df.cardio==0], y=df.alco[(df.cardio==0)], c="#32CD32")
plt.scatter(x=df.age_years[df.cardio==1], y=df.alco[(df.cardio==1)], c="#D2042D")
plt.legend(["Absence", "Presence"])
plt.xlabel("age_years")
plt.ylabel("Alcohol (0: Non-Alcoholic, 1:Alcoholoc)")
plt.show()
# violinplot
sns.violinplot(x=df.cardio,y=df.alco,data=df)
plt.title('Violin Plot of Cardiovascular Diseases by Alcohol Intake')
plt.ylabel('Cardiovascular Disease (0: Absence, 1: Presence)')
plt.xlabel('Alcohol intake(0: Does not consume alcohol, 1:Consumes alcohol)')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='alco', y='cardio')
plt.title('Box Plot of Alcohol vs. Cardiovascular Disease')
plt.ylabel('Cardiovascular Disease (0: Absence, 1: Presence)')
plt.xlabel('Alcohol (0: Non-Alcoholic, 1:Alcoholoc)')
plt.show()

"""**Desribe Cholesterol Levels**"""

#plotting a countplot of No of people with Cholesterol Levels
sns.countplot(data=df, x='cholesterol')
plt.title("No of people in each Cholesterol Levels")
plt.xlabel('Cholesterol Levels(1:Normal, 2:Above Normal, 3:Well Above Normal)')

plt.scatter(x=df.age_years[df.cardio==0], y=df.cholesterol[(df.cardio==0)], c="#32CD32")
plt.scatter(x=df.age_years[df.cardio==1], y=df.cholesterol[(df.cardio==1)], c="#D2042D")
plt.legend(["Absence", "Presence"])
plt.xlabel("age_years")
plt.ylabel("Cholesterol Levels(1:Normal, 2:Above Normal, 3:Well Above Normal)")
plt.show()
# violinplot
sns.violinplot(x=df.cardio,y=df.cholesterol,data=df)
plt.title('Violin Plot of Cardiovascular Disease by Cholesterol')
plt.xlabel('Cardiovascular Disease (0: Absence, 1: Presence)')
plt.ylabel('Cholesterol Levels(1:Normal, 2:Above Normal, 3:Well Above Normal)')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, y='cholesterol', x='cardio')
plt.title('Box Plot of Cholesterol vs. Cardiovascular Disease')
plt.xlabel('Cardiovascular Disease (0: Absence, 1: Presence)')
plt.ylabel('Cholesterol Levels(1:Normal, 2:Above Normal, 3:Well Above Normal)')
plt.show()

"""**Describe Glucose Levels**"""

#plotting a countplot of No of people with Glucose Levels
sns.countplot(data=df, x='gluc')
plt.title("No of people with Glucose Levels")
plt.xlabel('Glucose Levels(1:Normal, 2:Above Normal, 3:Well Above Normal)')

plt.scatter(x=df.age_years[df.cardio==0], y=df.gluc[(df.cardio==0)], c="#32CD32")
plt.scatter(x=df.age_years[df.cardio==1], y=df.gluc[(df.cardio==1)], c="#D2042D")
plt.legend(["Absence", "Presence"])
plt.xlabel("age_years")
plt.ylabel("Glucose Levels(1:Normal, 2:Above Normal, 3:Well Above Normal)")
plt.show()
# violinplot
sns.violinplot(x=df.cardio,y=df.gluc,data=df)
plt.title('Violin Plot of Cardiovascular Disease by Glucose')
plt.xlabel('Cardiovascular Disease (0: Absence, 1: Presence)')
plt.ylabel('Glucose Levels(1:Normal, 2:Above Normal, 3:Well Above Normal)')
plt.show()

# plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='cardio', y='gluc')
plt.title('Box Plot of Glucose vs. Cardiovascular Disease')
plt.xlabel('Cardiovascular Disease (0: Absence, 1: Presence)')
plt.ylabel('Glucose Levels(1:Normal, 2:Above Normal, 3:Well Above Normal)')
plt.show()

"""**Describe physical activites**"""

#plotting a pie chart of No of people with active physical activities
df['active'].value_counts().plot(kind='pie',autopct='%1.1f%%')
plt.title("No of people with active physical activities")
plt.xlabel('0: Not physically active, 1: Physically active')

plt.scatter(x=df.age_years[df.cardio==0], y=df.active[(df.cardio==0)], c="#32CD32")
plt.scatter(x=df.age_years[df.cardio==1], y=df.active[(df.cardio==1)], c="#D2042D")
plt.legend(["Absence", "Presence"])
plt.xlabel("age_years")
plt.ylabel("0: Not physically active, 1: Physically active")
plt.show()
# violinplot
sns.violinplot(x=df.cardio,y=df.active,data=df)
plt.title('Violin Plot of Cardiovascular Disease by Physical Activity')
plt.xlabel('Cardiovascular Disease (0: Absence, 1: Presence)')
plt.ylabel('0: Not physically active, 1: Physically active')
plt.show()

# plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='cardio', y='active')
plt.title('Box Plot of Activity vs. Cardiovascular Disease')
plt.xlabel('Cardiovascular Disease (0: Absence, 1: Presence)')
plt.ylabel('0: Not physically active, 1: Physically active')
plt.show()

"""**Describe Cardiovascular Diseases**"""

# Gender of the patient. Categorical variable (0: Absence, 1: Presence).
# absence
cardio_absence = df['cardio'].value_counts()[0]
print(f"Absence: {cardio_absence}")
print("Absence Percentage: {:.2f}%".format((len(df[df.cardio == 0]) / (len(df.cardio))*100)))
# presence
cardio_presence = df['cardio'].value_counts()[1]
print(f"Presence: {cardio_presence}")
print("Presence Percentage: {:.2f}%".format((len(df[df.cardio == 1]) / (len(df.cardio))*100)))

#plotting a pie chart of No of people with persense or absense of cardiovascular diseases
df['cardio'].value_counts().plot(kind='pie',autopct='%2.2f%%')
plt.title("Presence or Absence of Cardiovascular Diseases")
plt.xlabel('0: Absence, 1: Presence')
plt.ylabel('')

"""**Describe Age vs Cardiovascular Disease**"""

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='cardio', y='age_years', hue='cardio')
plt.title('Scatter Plot of Age vs. Cardiovascular Disease')
plt.xlabel('Cardiovascular Disease (0: Absence, 1: Presence)')
plt.ylabel('Age (Years)')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='cardio', y='age_years')
plt.title('Box Plot of Cardiovascular Disease vs. Age')
plt.xlabel('Cardiovascular Disease (0: Absence, 1: Presence)')
plt.ylabel('Age (Years)')
plt.show()

"""**Cardio vs Age vs ap_lo**"""

plt.figure(figsize=(10, 6))
plt.scatter(x=df.age_years[df.cardio==0], y=df.ap_lo[(df.cardio==0)], c="#32CD32")
plt.scatter(x=df.age_years[df.cardio==1], y=df.ap_lo[(df.cardio==1)], c="#D2042D")
plt.legend(["Absence", "Presence"])
plt.title('Scatter Plot of Cardiovascular Disease by Diastolic blood pressure')
plt.xlabel("age_years")
plt.ylabel("Diastolic blood pressure")
plt.show()
# violinplot
sns.violinplot(x=df.cardio,y=df.ap_lo,data=df)
plt.title('Violin Plot of Cardiovascular Disease by Diastolic blood pressure')
plt.xlabel('Cardiovascular Disease (0: Absence, 1: Presence)')
plt.ylabel('Diastolic blood pressure')
plt.show()

"""**Cardio vs age vs ap_hi**"""

plt.figure(figsize=(10, 6))
plt.scatter(x=df.age_years[df.cardio==0], y=df.ap_hi[(df.cardio==0)], c="#32CD32")
plt.scatter(x=df.age_years[df.cardio==1], y=df.ap_hi[(df.cardio==1)], c="#D2042D")
plt.legend(["Absence", "Presence"])
plt.title('Scatter Plot of Cardiovascular Disease by Systolic blood pressure')
plt.xlabel("age_years")
plt.ylabel("ap_hi")
plt.show()
# violinplot
sns.violinplot(x=df.cardio,y=df.ap_hi,data=df)
plt.title('Violin Plot of Cardiovascular Disease by Systolic blood pressure')
plt.xlabel('Cardiovascular Disease (0: Absence, 1: Presence)')
plt.ylabel('Systolic blood pressure')
plt.show()

"""**Describe Diastolic Blood Pressure vs Cardiovascular Disease**"""

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='cardio', y='ap_lo', hue='cardio')
plt.title('Scatter Plot of Diastolic Blood Pressure vs. Cardiovascular Disease')
plt.xlabel('Cardiovascular Disease (0: Absence, 1: Presence)')
plt.ylabel('Diastolic Blood Pressure (ap_lo)')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='cardio', y='ap_lo')
plt.title('Box Plot of Cardiovascular Disease by Diastolic Blood Pressure ')
plt.xlabel('Cardiovascular Disease (0: Absence, 1: Presence)')
plt.ylabel('Diastolic Blood Pressure (ap_lo)')
plt.show()

"""**Describe Systolic Blood Pressure vs Cardiovascular Disease**"""

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='cardio', y='ap_hi', hue='cardio')
plt.title('Scatter Plot of Systolic Blood Pressure vs. Cardiovascular Disease')
plt.xlabel('Cardiovascular Disease (0: Absence, 1: Presence)')
plt.ylabel('Systolic Blood Pressure (ap_lo)')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='cardio', y='ap_hi')
plt.title('Box Plot of Cardiovascular Disease by Systolic Blood Pressure')
plt.xlabel('Cardiovascular Disease (0: Absence, 1: Presence)')
plt.ylabel('Systolic Blood Pressure (ap_lo)')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='cardio', y='bmi', hue='cardio')
plt.title('Scatter Plot of BMI vs. Cardiovascular Disease')
plt.xlabel('Cardiovascular Disease (0: Absence, 1: Presence)')
plt.ylabel('BMI')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='cardio', y='bmi')
plt.title('Scatter Plot of BMI vs. Cardiovascular Disease')
plt.xlabel('Cardiovascular Disease (0: Absence, 1: Presence)')
plt.ylabel('BMI')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='weight', y='bmi', hue='cardio', palette={0: 'blue', 1: 'red'})
plt.title('Scatter Plot of Age vs. Diastolic Blood Pressure')
plt.xlabel('Diastolic Blood Pressure (ap_lo)')
plt.ylabel('Diastolic Blood Pressure (ap_hi))')
plt.show()

# Correlation Analysis
data_corr = df_bp.copy()

for column in data_corr.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    data_corr[column] = le.fit_transform(data_corr[column])

correlation_matrix = data_corr.corr()
plt.figure(figsize=(14,10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Feature Correlation Matrix')
plt.show()

"""**Assignment 2**"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, OrdinalEncoder
from sklearn.preprocessing import MaxAbsScaler
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense,InputLayer
from tensorflow.keras.utils import plot_model
import keras
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay,classification_report,accuracy_score,average_precision_score
import os


# Load CSV
df = pd.read_csv(cardiao_data_path)

tf.__version__
keras.__version__

"""**Data Preprocessing 1**"""

df = df.drop('bp_category',axis=1)
df = df.drop('id',axis=1)

#To drop bp_category(output)

bp_categories = ['Normal','Elevated','Hypertension Stage 1','Hypertension Stage 2']
enc = OrdinalEncoder()
df['bp_category_encoded']=enc.fit_transform(df[['bp_category_encoded']])
df['bp_category_encoded']=df['bp_category_encoded'].apply(lambda x: int(x))

# 0 1 2 3 (maybe, for easily observe)

X = df.drop('bp_category_encoded',axis=1)
y = df['bp_category_encoded']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=101)
X_train.shape,X_test.shape,y_train.shape,y_test.shape
print(X_train)
print(X_train.iloc[0])
print(type(X_train.iloc[0]))
print(X_train.shape,y_train.shape)

scaler = MinMaxScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)
print(X_train[0])

"""**Simple ANN Model 1**"""

#create model
model = Sequential([
    InputLayer(input_shape=14), #input layer
    Dense(14,activation='relu'), #hidden layer
    Dense(14,activation='relu'), #hidden layer
    Dense(4, activation='softmax'), #output layer
])

#compile the model
model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), #can try other learning rate if need to prove this the better/best learning rate to use
              metrics=['accuracy'])

history = model.fit(X_train,y_train,
                   epochs=25, #Can try other epoch as well if necessary
                   validation_data=[X_test,y_test])

model.save('cardio_model')
model.summary()
plot_model(model,show_shapes=True)

new_model = tf.keras.models.load_model('cardio_model')
new_model.summary()
y_probs = new_model.predict(X_train[0])
y_preds = tf.argmax(y_probs)
print(y_preds)

#checking model training loss history
loss=history.history['loss']
val_loss=history.history['val_loss']
losses = pd.DataFrame({'loss':loss,'val_loss':val_loss})

#checking model training accuracy history
accuracy=history.history['accuracy']
val_accuracy=history.history['val_accuracy']
acc = pd.DataFrame({'accuracy':accuracy,'val_accuracy':val_accuracy})


losses.plot(title='Loss curve')
acc.plot(title='Accuracy curve')

#Evaluating using model.evaluate (Can consider as training conclusion result)
loss,acc = model.evaluate(X_test,y_test)
print(f"Model loss: {loss:.3f}")
print(f"Model accuracy: {acc*100:.2f}%")

y_probs = model.predict(X_test)
print(y_probs)
y_preds = tf.argmax(y_probs,axis=1)
print(y_preds)

sacc_score=accuracy_score(y_test,y_preds) #another way to conclude and prove the result

print(classification_report(y_test,y_preds))
print(f'Accuracy is {acc_score*100:.2f}%')

#Making Confusion Matrix
cm = confusion_matrix(y_test,y_preds)

#using ConfusionMatrixDisplay to output a good confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=bp_categories)
disp.plot()
plt.title("Confusion Matrix")
plt.xticks(rotation=90)

"""**Simple ANN Model 2**"""

#create model
model = Sequential([
    InputLayer(input_shape=14),
    Dense(14,activation='relu'),
    Dense(28,activation='relu'),
    Dense(14,activation='relu'),
    Dense(4, activation='softmax'),
])

#compile the model
model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              metrics=['accuracy'])

history = model.fit(X_train,y_train,
                   epochs=25,
                   validation_data=[X_test,y_test])

model.summary()
plot_model(model,show_shapes=True)
#checking model training loss history
loss=history.history['loss']
val_loss=history.history['val_loss']
losses = pd.DataFrame({'loss':loss,'val_loss':val_loss})

#checking model training accuracy history
accuracy=history.history['accuracy']
val_accuracy=history.history['val_accuracy']
acc = pd.DataFrame({'accuracy':accuracy,'val_accuracy':val_accuracy})


losses.plot(title='Loss curve')
acc.plot(title='Accuracy curve')
loss,acc = model.evaluate(X_test,y_test)
print(f"Model loss: {loss:.3f}")
print(f"Model accuracy: {acc*100:.2f}%")
y_probs = model.predict(X_test)
y_preds = tf.argmax(y_probs,axis=1)
acc_score=accuracy_score(y_test,y_preds)

print(classification_report(y_test,y_preds))
print(f'Accuracy is {acc_score*100:.2f}%')

#Making Confusion Matrix
cm = confusion_matrix(y_test,y_preds)

#using ConfusionMatrixDisplay to output a good confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=bp_categories)
disp.plot()
plt.title("Confusion Matrix")
plt.xticks(rotation=90)

"""**Simple ANN Model 3**"""

#create model
model = Sequential([
    InputLayer(input_shape=14),
    Dense(14,activation='relu'),
    Dense(14,activation='relu'),
    Dense(14,activation='relu'),
    Dense(4, activation='softmax'),
])

#compile the model
model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              metrics=['accuracy'])

history = model.fit(X_train,y_train,
                   epochs=25,
                   validation_data=[X_test,y_test])

model.summary()
plot_model(model,show_shapes=True)
#checking model training loss history
loss=history.history['loss']
val_loss=history.history['val_loss']
losses = pd.DataFrame({'loss':loss,'val_loss':val_loss})

#checking model training accuracy history
accuracy=history.history['accuracy']
val_accuracy=history.history['val_accuracy']
acc = pd.DataFrame({'accuracy':accuracy,'val_accuracy':val_accuracy})


losses.plot(title='Loss curve')
acc.plot(title='Accuracy curve')
loss,acc = model.evaluate(X_test,y_test)
print(f"Model loss: {loss:.3f}")
print(f"Model accuracy: {acc*100:.2f}%")
y_probs = model.predict(X_test)
y_preds = tf.argmax(y_probs,axis=1)
acc_score=accuracy_score(y_test,y_preds)

print(classification_report(y_test,y_preds))
print(f'Accuracy is {acc_score*100:.2f}%')

#Making Confusion Matrix
cm = confusion_matrix(y_test,y_preds)

#using ConfusionMatrixDisplay to output a good confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=bp_categories)
disp.plot()
plt.title("Confusion Matrix")
plt.xticks(rotation=90)

"""**Machine Learning Models**"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier
import lightgbm as lgb
from lightgbm import LGBMClassifier

LGBM = LGBMClassifier()
LGBM.fit(X_train, y_train)
y_pred_LGBM = LGBM.predict(X_test) # predict our file test data
LGBM_acc = accuracy_score(y_test, y_pred_LGBM)
print("LGBM accuracy is: {0:.3f}%".format(LGBM_acc * 100))
cm = confusion_matrix(y_test, y_pred_LGBM)
plt.figure(figsize=(4, 4))
sns.heatmap(cm, annot=True, fmt='.0f')
plt.xlabel("Predicted Digits")
plt.ylabel("True Digits")
plt.show()



Log = LogisticRegression()
Log.fit(X_train, y_train)
y_pred_Log = Log.predict(X_test) # predict our file test data
Log_acc = accuracy_score(y_test, y_pred_Log)
print("Log accuracy is: {0:.3f}%".format(Log_acc * 100))
cm = confusion_matrix(y_test, y_pred_Log)
plt.figure(figsize=(4, 4))
sns.heatmap(cm, annot=True, fmt='.0f')
plt.xlabel("Predicted Digits")
plt.ylabel("True Digits")
plt.show()

SGD = SGDClassifier()
SGD.fit(X_train, y_train)
y_pred_SGD = SGD.predict(X_test) # predict our file test data
SGD_acc = accuracy_score(y_test, y_pred_SGD)
print("SGD accuracy is: {0:.3f}%".format(SGD_acc * 100))
cm = confusion_matrix(y_test, y_pred_SGD)
plt.figure(figsize=(4, 4))
sns.heatmap(cm, annot=True, fmt='.0f')
plt.xlabel("Predicted Digits")
plt.ylabel("True Digits")
plt.show()

GNB = GaussianNB()
GNB.fit(X_train, y_train)
y_pred_GNB = GNB.predict(X_test) # predict our file test data
GNB_acc = accuracy_score(y_test, y_pred_GNB)
print("GNB accuracy is: {0:.3f}%".format(GNB_acc * 100))
cm = confusion_matrix(y_test, y_pred_GNB)
plt.figure(figsize=(4, 4))
sns.heatmap(cm, annot=True, fmt='.0f')
plt.xlabel("Predicted Digits")
plt.ylabel("True Digits")
plt.show()


knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test) # predict our file test data
knn_acc = accuracy_score(y_test, y_pred_knn)
print("KNN accuracy is: {0:.3f}%".format(knn_acc * 100))
cm = confusion_matrix(y_test, y_pred_knn)
plt.figure(figsize=(4, 4))
sns.heatmap(cm, annot=True, fmt='.0f')
plt.xlabel("Predicted Digits")
plt.ylabel("True Digits")
plt.show()


RF = RandomForestClassifier(n_estimators=10)
RF.fit(X_train, y_train)
y_pred_RF = RF.predict(X_test) # predict our file test data
RF_acc = accuracy_score(y_test, y_pred_RF)
print("RF accuracy is: {0:.3f}%".format(RF_acc * 100))
cm = confusion_matrix(y_test, y_pred_RF)
plt.figure(figsize=(4, 4))
sns.heatmap(cm, annot=True, fmt='.0f')
plt.xlabel("Predicted Digits")
plt.ylabel("True Digits")
plt.show()


Ext = ExtraTreesClassifier(n_estimators=10)
Ext.fit(X_train, y_train)
y_pred_Ext = Ext.predict(X_test) # predict our file test data
Ext_acc = accuracy_score(y_test, y_pred_Ext)
print("Ext accuracy is: {0:.3f}%".format(Ext_acc * 100))
cm = confusion_matrix(y_test, y_pred_Ext)
plt.figure(figsize=(4, 4))
sns.heatmap(cm, annot=True, fmt='.0f')
plt.xlabel("Predicted Digits")
plt.ylabel("True Digits")
plt.show()



HGB = HistGradientBoostingClassifier()
HGB.fit(X_train, y_train)
y_pred_HGB = HGB.predict(X_test) # predict our file test data
HGB_acc = accuracy_score(y_test, y_pred_HGB)
print("HGB accuracy is: {0:.3f}%".format(HGB_acc * 100))
cm = confusion_matrix(y_test, y_pred_HGB)
plt.figure(figsize=(4, 4))
sns.heatmap(cm, annot=True, fmt='.0f')
plt.xlabel("Predicted Digits")
plt.ylabel("True Digits")
plt.show()



XGB = XGBClassifier(n_estimators=10)
XGB.fit(X_train, y_train)
y_pred_XGB = XGB.predict(X_test) # predict our file test data
XGB_acc = accuracy_score(y_test, y_pred_XGB)
print("XGB accuracy is: {0:.3f}%".format(XGB_acc * 100))
cm = confusion_matrix(y_test, y_pred_XGB)
plt.figure(figsize=(4, 4))
sns.heatmap(cm, annot=True, fmt='.0f')
plt.xlabel("Predicted Digits")
plt.ylabel("True Digits")
plt.show()

"""**Data Preprocessing - Drop more column**"""

X = df.drop(columns=['bp_category_encoded','gluc','active','alco','smoke'],axis=1)
y = df['bp_category_encoded']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=101)
X_train.shape,X_test.shape,y_train.shape,y_test.shape

scaler = MinMaxScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)
print(X_train)

"""**Drop Column - Simple ANN Model 1**"""

#create model
model = Sequential([
    InputLayer(input_shape=10),
    Dense(10,activation='relu'),
    Dense(10,activation='relu'),
    Dense(4, activation='softmax'),
])

#compile the model
model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              metrics=['accuracy'])

history = model.fit(X_train,y_train,
                   epochs=25,
                   validation_data=[X_test,y_test])

model.summary()
plot_model(model,show_shapes=True)
#checking model training loss history
loss=history.history['loss']
val_loss=history.history['val_loss']
losses = pd.DataFrame({'loss':loss,'val_loss':val_loss})

#checking model training accuracy history
accuracy=history.history['accuracy']
val_accuracy=history.history['val_accuracy']
acc = pd.DataFrame({'accuracy':accuracy,'val_accuracy':val_accuracy})


losses.plot(title='Loss curve')
acc.plot(title='Accuracy curve')
loss,acc = model.evaluate(X_test,y_test)
print(f"Model loss: {loss:.3f}")
print(f"Model accuracy: {acc*100:.2f}%")
y_probs = model.predict(X_test)
y_preds = tf.argmax(y_probs,axis=1)
acc_score=accuracy_score(y_test,y_preds)

print(classification_report(y_test,y_preds))
print(f'Accuracy is {acc_score*100:.2f}%')

#Making Confusion Matrix
cm = confusion_matrix(y_test,y_preds)

#using ConfusionMatrixDisplay to output a good confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=bp_categories)
disp.plot()
plt.title("Confusion Matrix")
plt.xticks(rotation=90)

"""**Drop Column - Simple ANN Model 2**"""

#create model
model = Sequential([
    InputLayer(input_shape=10),
    Dense(10,activation='relu'),
    Dense(20,activation='relu'),
    Dense(10,activation='relu'),
    Dense(4, activation='softmax'),
])

#compile the model
model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              metrics=['accuracy'])

history = model.fit(X_train,y_train,
                   epochs=25,
                   validation_data=[X_test,y_test])

model.summary()
plot_model(model,show_shapes=True)
#checking model training loss history
loss=history.history['loss']
val_loss=history.history['val_loss']
losses = pd.DataFrame({'loss':loss,'val_loss':val_loss})

#checking model training accuracy history
accuracy=history.history['accuracy']
val_accuracy=history.history['val_accuracy']
acc = pd.DataFrame({'accuracy':accuracy,'val_accuracy':val_accuracy})


losses.plot(title='Loss curve')
acc.plot(title='Accuracy curve')
loss,acc = model.evaluate(X_test,y_test)
print(f"Model loss: {loss:.3f}")
print(f"Model accuracy: {acc*100:.2f}%")
y_probs = model.predict(X_test)
y_preds = tf.argmax(y_probs,axis=1)
acc_score=accuracy_score(y_test,y_preds)

print(classification_report(y_test,y_preds))
print(f'Accuracy is {acc_score*100:.2f}%')

#Making Confusion Matrix
cm = confusion_matrix(y_test,y_preds)

#using ConfusionMatrixDisplay to output a good confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=bp_categories)
disp.plot()
plt.title("Confusion Matrix")
plt.xticks(rotation=90)

"""**Drop Column - Simple ANN Model 3**"""

#create model
model = Sequential([
    InputLayer(input_shape=10),
    Dense(10,activation='relu'),
    Dense(10,activation='relu'),
    Dense(10,activation='relu'),
    Dense(4, activation='softmax'),
])

#compile the model
model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              metrics=['accuracy'])

history = model.fit(X_train,y_train,
                   epochs=25,
                   validation_data=[X_test,y_test])

model.summary()
plot_model(model,show_shapes=True)
#checking model training loss history
loss=history.history['loss']
val_loss=history.history['val_loss']
losses = pd.DataFrame({'loss':loss,'val_loss':val_loss})

#checking model training accuracy history
accuracy=history.history['accuracy']
val_accuracy=history.history['val_accuracy']
acc = pd.DataFrame({'accuracy':accuracy,'val_accuracy':val_accuracy})


losses.plot(title='Loss curve')
acc.plot(title='Accuracy curve')
loss,acc = model.evaluate(X_test,y_test)
print(f"Model loss: {loss:.3f}")
print(f"Model accuracy: {acc*100:.2f}%")
y_probs = model.predict(X_test)
y_preds = tf.argmax(y_probs,axis=1)
acc_score=accuracy_score(y_test,y_preds)

print(classification_report(y_test,y_preds))
print(f'Accuracy is {acc_score*100:.2f}%')

#Making Confusion Matrix
cm = confusion_matrix(y_test,y_preds)

#using ConfusionMatrixDisplay to output a good confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=bp_categories)
disp.plot()
plt.title("Confusion Matrix")
plt.xticks(rotation=90)

"""**Drop columns - Machine Learning Models**"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier
import lightgbm as lgb
from lightgbm import LGBMClassifier

LGBM = LGBMClassifier()
LGBM.fit(X_train, y_train)
y_pred_LGBM = LGBM.predict(X_test) # predict our file test data
LGBM_acc = accuracy_score(y_test, y_pred_LGBM)
print("LGBM accuracy is: {0:.3f}%".format(LGBM_acc * 100))
cm = confusion_matrix(y_test, y_pred_LGBM)
plt.figure(figsize=(4, 4))
sns.heatmap(cm, annot=True, fmt='.0f')
plt.xlabel("Predicted Digits")
plt.ylabel("True Digits")
plt.show()



Log = LogisticRegression()
Log.fit(X_train, y_train)
y_pred_Log = Log.predict(X_test) # predict our file test data
Log_acc = accuracy_score(y_test, y_pred_Log)
print("Log accuracy is: {0:.3f}%".format(Log_acc * 100))
cm = confusion_matrix(y_test, y_pred_Log)
plt.figure(figsize=(4, 4))
sns.heatmap(cm, annot=True, fmt='.0f')
plt.xlabel("Predicted Digits")
plt.ylabel("True Digits")
plt.show()

SGD = SGDClassifier()
SGD.fit(X_train, y_train)
y_pred_SGD = SGD.predict(X_test) # predict our file test data
SGD_acc = accuracy_score(y_test, y_pred_SGD)
print("SGD accuracy is: {0:.3f}%".format(SGD_acc * 100))
cm = confusion_matrix(y_test, y_pred_SGD)
plt.figure(figsize=(4, 4))
sns.heatmap(cm, annot=True, fmt='.0f')
plt.xlabel("Predicted Digits")
plt.ylabel("True Digits")
plt.show()

GNB = GaussianNB()
GNB.fit(X_train, y_train)
y_pred_GNB = GNB.predict(X_test) # predict our file test data
GNB_acc = accuracy_score(y_test, y_pred_GNB)
print("GNB accuracy is: {0:.3f}%".format(GNB_acc * 100))
cm = confusion_matrix(y_test, y_pred_GNB)
plt.figure(figsize=(4, 4))
sns.heatmap(cm, annot=True, fmt='.0f')
plt.xlabel("Predicted Digits")
plt.ylabel("True Digits")
plt.show()


knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test) # predict our file test data
knn_acc = accuracy_score(y_test, y_pred_knn)
print("KNN accuracy is: {0:.3f}%".format(knn_acc * 100))
cm = confusion_matrix(y_test, y_pred_knn)
plt.figure(figsize=(4, 4))
sns.heatmap(cm, annot=True, fmt='.0f')
plt.xlabel("Predicted Digits")
plt.ylabel("True Digits")
plt.show()


RF = RandomForestClassifier(n_estimators=10)
RF.fit(X_train, y_train)
y_pred_RF = RF.predict(X_test) # predict our file test data
RF_acc = accuracy_score(y_test, y_pred_RF)
print("RF accuracy is: {0:.3f}%".format(RF_acc * 100))
cm = confusion_matrix(y_test, y_pred_RF)
plt.figure(figsize=(4, 4))
sns.heatmap(cm, annot=True, fmt='.0f')
plt.xlabel("Predicted Digits")
plt.ylabel("True Digits")
plt.show()


Ext = ExtraTreesClassifier(n_estimators=10)
Ext.fit(X_train, y_train)
y_pred_Ext = Ext.predict(X_test) # predict our file test data
Ext_acc = accuracy_score(y_test, y_pred_Ext)
print("Ext accuracy is: {0:.3f}%".format(Ext_acc * 100))
cm = confusion_matrix(y_test, y_pred_Ext)
plt.figure(figsize=(4, 4))
sns.heatmap(cm, annot=True, fmt='.0f')
plt.xlabel("Predicted Digits")
plt.ylabel("True Digits")
plt.show()



HGB = HistGradientBoostingClassifier()
HGB.fit(X_train, y_train)
y_pred_HGB = HGB.predict(X_test) # predict our file test data
HGB_acc = accuracy_score(y_test, y_pred_HGB)
print("HGB accuracy is: {0:.3f}%".format(HGB_acc * 100))
cm = confusion_matrix(y_test, y_pred_HGB)
plt.figure(figsize=(4, 4))
sns.heatmap(cm, annot=True, fmt='.0f')
plt.xlabel("Predicted Digits")
plt.ylabel("True Digits")
plt.show()



XGB = XGBClassifier(n_estimators=10)
XGB.fit(X_train, y_train)
y_pred_XGB = XGB.predict(X_test) # predict our file test data
XGB_acc = accuracy_score(y_test, y_pred_XGB)
print("XGB accuracy is: {0:.3f}%".format(XGB_acc * 100))
cm = confusion_matrix(y_test, y_pred_XGB)
plt.figure(figsize=(4, 4))
sns.heatmap(cm, annot=True, fmt='.0f')
plt.xlabel("Predicted Digits")
plt.ylabel("True Digits")
plt.show()
