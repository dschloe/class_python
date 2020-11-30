#!/venv/bin/python
# -*- coding: utf-8 -*-

import pandas as pd

def get_data(data_path):
    data = pd.read_csv(data_path)
    print('/n ### 학습 데이터 정보 ### /n')
    print(data.info())
    return data