import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import csv


def create_data_model():
    with open('rules_train.csv', 'r') as f:
        line = csv.reader(f)
        list_ip = list(line)
        list_action = [item.pop(0) for item in list_ip]
        print(list_action)
        print(list_ip)

    values = np.array(list_ip)
    print(values)
    # integer encode
    label_encoder = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(values)
    print(integer_encoded)
    # binary encode
    onehot_encoder = OneHotEncoder(sparse=False)
    integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
    onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
    print(onehot_encoded)

    print(list_ip1)
    list_iptrain = list_ipenc[:150]
    list_iptest = list_ipenc[150:]
    list_actiontrain = list_actionenc[:150]
    list_actiontest = list_actionenc[150:]

    print(len(list_iptest))

    return list_iptrain, list_actiontrain, list_iptest, list_actiontest, list_ip


create_data_model()

def create_data_input():
    a =3
create_data_input()

