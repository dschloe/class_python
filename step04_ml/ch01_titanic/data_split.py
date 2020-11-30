#!venv/bin/python
# -*- conding: utf-8 -*-

from sklearn.model_selection import train_test_split

def x_y_df(data, y_var):
    y_df = data[y_var]
    X_df = data.drop(y_var, axis=1)

    return X_df, y_df

def train_test(X_df, y_df):
    X_train, X_test, y_train, y_test = train_test_split(X_df, y_df, test_size=0.2, random_state=1)
    return X_train, X_test, y_train, y_test
