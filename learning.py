from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


df = pd.read_excel('./xlsx_/f_029df (1).xlsx')
df = df.drop(columns=['Unnamed: 0', 'highway','X','Y','nfnc','nfc','nsnc','nsc','anfnc','anfc','ansnc','ansc','ffc','affc'])
np.random.seed(100)
tf.random.set_seed(100)

df.set_index('dong')

X = df.drop(columns=['총생활인구수','dong']).astype(float)
y = df['총생활인구수'].astype(float)

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size = 0)

train_ds = tf.data.Dataset.from_tensor_slices((train_X.values, train_y))
train_ds = train_ds.shuffle(len(train_X)).batch(batch_size=5)

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(7),
    tf.keras.layers.Dense(3, activation='relu'),
    tf.keras.layers.Dense(1, activation='relu')
    ])

model.compile(loss='mean_squared_logarithmic_error', optimizer='adam')
history = model.fit(train_ds, epochs=100)

loss = model.evaluate(test_X, test_y)

print("테스트 데이터의 Loss 값: ", loss)

predictions = model.predict(test_X)

model.save('029_model.h5')
model.save_weights("029_model_weights.h5")

# for i, val in enumerate(model.get_weights()):
#     print(f'{i}번째 가중치 : ', val)
# kfold = KFold(n_splits=5)
# cv_accuracy=[]
# 
# n_iter=0
# for train_idx, test_idx in kfold.split(X):
#     X_train, X_test = X[train_idx], X[test_idx]
#     y_train, y_test = Y[train_idx], Y[test_idx]
#     
#     fold_df_clf.fit(X_train, y_train)
#     fold_pred = fold_df_clf.predict(X_test)
#     
#     n_iter += 1
#     accuracy = np.round(accuracy_score(y_test, fold_pred), 4)
#     print('\n{} 교차검증 정확도 : {}, 학습 데이터 크기 : {}, 검증 데이터 크기 : {}# '.format(n_iter, accuracy, X_train.shape[0], X_test.shape[0]))
#     cv_accuracy.append(accuracy)
# print('\n')
# 
# print('\n 평균 검증 정확도 : ', np.mean(cv_accuracy))