#!/venv/bin/python
# -*- coding: utf-8 -*-

from ch01_titanic import data_import
from ch01_titanic import data_cleansing
from ch01_titanic import data_split
from ch01_titanic import model

# 데이터 경로
data_path = "ch01_titanic/data/titanic_train.csv"

# 결측치 처리 변수들
var_list = ["Age", "Cabin", "Embarked", 'Fare']

# 삭제될 변수 리스트
drop_var_list = ['PassengerId', 'Name', 'Ticket']

# encoding features
encoding_feaatures = ['Cabin', 'Sex', 'Embarked']

# 종속변수 이름
y_var = 'Survived'

if __name__ == '__main__':
    print("--get_started--")
    # print(data_import.get_data(data_path))
    data = data_import.get_data(data_path)

    # raw data split
    X_df, y_df = data_split.x_y_df(data, y_var)

    # data transformation
    X_df = data_cleansing.transform_features(X_df, var_list, drop_var_list, encoding_feaatures)

    # ML data split
    X_train, X_test, y_train, y_test = data_split.train_test(X_df, y_df)

    # modeling
    print(model.models(X_train, X_test, y_train, y_test))
