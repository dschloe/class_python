#!venv/bin/python
# -*- encoding: utf-8 -*-

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd

def models(X_train, X_test, y_train, y_test):
    # 결정 트리, random Forest, Logistic Regression 객체 생성
    dt_clf = DecisionTreeClassifier(random_state=1)
    rf_clf = RandomForestClassifier(random_state=1)
    lr_clf = LogisticRegression()

    # 모형 학습
    dt_clf.fit(X_train, y_train)
    rf_clf.fit(X_train, y_train)
    lr_clf.fit(X_train, y_train)

    # 모형 예측
    dt_pred = dt_clf.predict(X_test)
    rf_pred = rf_clf.predict(X_test)
    lr_pred = lr_clf.predict(X_test)

    # 모형 평가
    dt_acc = accuracy_score(y_test, dt_pred)
    rf_acc = accuracy_score(y_test, rf_pred)
    lr_acc = accuracy_score(y_test, lr_pred)

    result_dict = {'name_of_model':['Decision', 'RandomForest', 'Logistic'],
                   'accuracy':[dt_acc, rf_acc, lr_acc]}
    pred_df = pd.DataFrame(result_dict)

    return pred_df
