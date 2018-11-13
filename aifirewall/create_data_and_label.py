import numpy as np
from sklearn.preprocessing import OneHotEncoder
import csv


def create_data_train():
    list_ip = []
    list_action = []
    with open('rules1.csv', 'r') as f:
        line = csv.reader(f)
        next(line)
        list_ip = list(line)
        list_action = [item.pop(0) for item in list_ip]
        print(list_action)
        print(list_ip)

    enc = OneHotEncoder(handle_unknown='ignore')
    enc2 = OneHotEncoder(handle_unknown='ignore')
    list_ipenc = enc.fit(list_ip)
    list_action = np.reshape(list_action, (-1, 1))
    list_actionenc = enc2.fit(list_action)
    print(list_actionenc)

    list_ipenc = enc.transform(list_ip).toarray()
    list_actionenc = enc2.transform(list_action).toarray()

    print(list_ipenc.shape)
    print(list_actionenc)

    return list_ipenc, list_actionenc


create_data_train()

def create_data_test():
    list_ip = []
    list_action = []
    with open('rules2.csv', 'r') as f:
        line = csv.reader(f)
        next(line)
        list_ip = list(line)
        list_action = [item.pop(0) for item in list_ip]
        print(list_action)
        print(list_ip)

    enc = OneHotEncoder(handle_unknown='ignore')
    enc2 = OneHotEncoder(handle_unknown='ignore')
    list_ipenc = enc.fit(list_ip)
    list_action = np.reshape(list_action, (-1, 1))
    list_actionenc = enc2.fit(list_action)
    print(list_actionenc)

    list_ipenc = enc.transform(list_ip).toarray()
    list_actionenc = enc2.transform(list_action).toarray()

    print(list_ipenc.shape)
    print(list_actionenc)

    return list_ipenc, list_actionenc

create_data_test()
