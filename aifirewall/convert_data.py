import numpy as np
from sklearn.preprocessing import OneHotEncoder
import csv


def create_data_model():
    with open('rules_train.csv', 'r') as f:
        line = csv.reader(f)
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

    print(len(list_ipenc))
    list_iptrain = list_ipenc[:150]
    list_iptest = list_ipenc[150:]
    list_actiontrain = list_actionenc[:150]
    list_actiontest = list_actionenc[150:]
    print('******')
    print(len(list_iptest))

    return list_iptrain, list_actiontrain, list_iptest, list_actiontest, list_ip


create_data_model()

def create_data_input():
    a =3
create_data_input()

