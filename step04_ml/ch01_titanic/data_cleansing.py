#!/venv/bin/python
# -*- coding: utf-8 -*-
from sklearn.preprocessing import LabelEncoder

# Null 처리 함수
def fill_na(data, var_list):
    data[var_list[0]].fillna(data[var_list[0]].mean(), inplace=True)
    data[var_list[1]].fillna('N', inplace=True)
    data[var_list[2]].fillna('N', inplace=True)
    data[var_list[3]].fillna(0, inplace=True)
    print("--fill_na--")
    print('데이터 셋 Null 값 개수', data.isnull().sum().sum())

    return data

# 머신러닝 알고리즘에 불필요한 속성 제거
def drop_features(data, drop_var_list):
    data.drop(drop_var_list, axis=1, inplace=True)
    print("drop features done")
    return data

# 레이블 인코딩 수행
def format_features(data, encoding_feaatures):
    data['Cabin'] = data['Cabin'].str[:1]
    features = encoding_feaatures
    for feature in features:
        le = LabelEncoder()
        le = le.fit(data[feature])
        data[feature] = le.transform(data[feature])
    return data

def transform_features(data, var_list, drop_var_list, encoding_feaatures):
    data = fill_na(data, var_list)
    data = drop_features(data, drop_var_list)
    data = format_features(data, encoding_feaatures)
    return data