import numpy as np
from sklearn.preprocessing import OneHotEncoder
import csv


def create_data_model():
    with open('rules_train.csv', 'r') as f:
        line = csv.reader(f)
        list_ip = [li[:-1] for li in line]
        list_action = [item.pop(0) for item in list_ip]
        print(list_action)
        print(list_ip)

    enc = OneHotEncoder(handle_unknown='ignore')
    enc2 = OneHotEncoder(handle_unknown='ignore')

    list_action = np.reshape(list_action, (-1, 1))

    list_ipenc = enc.fit_transform(list_ip).toarray()
    list_actionenc = enc2.fit_transform(list_action).toarray()

    list_iptrain = list_ipenc[:400]
    list_actiontrain = list_actionenc[:400]

    print(list_ipenc.shape)
    print(len(list_ipenc))



    return list_iptrain, list_actiontrain, list_ip


create_data_model()


def create_data_input():
    with open('packet_diff.csv', 'r') as f:
        line1 = csv.reader(f)
        list_ip1 = [li[:-1] for li in line1]
        list_action = [item.pop(0) for item in list_ip1]
        print(list_ip1)

    enc3 = OneHotEncoder(handle_unknown='ignore')
    list_ipenc1 = enc3.fit_transform(list_ip1).toarray()

    print(list_ipenc1.shape)
    print(len(list_ipenc1))

    return list_ipenc1, list_ip1

create_data_input()
