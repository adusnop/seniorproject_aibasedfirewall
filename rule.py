import numpy as np
from sklearn.preprocessing import OneHotEncoder
import csv
def create_data():
    list_ip = []
    list_action = []
    with open('rules1.csv', 'r') as f:
        line = csv.reader(f)
        next(line)
        for row in line:
            list_ip.append(row[0])
            list_ip.append(row[1])
            list_action.append(row[2])
            
        print(list_ip)
    enc = OneHotEncoder(handle_unknown='ignore')
    list_ipenc = enc.fit(list_ip)
    print(list_ipenc[101:])
    list_ipenc = enc.transform(list_ip).toarray()
    a =  enc.inverse_transform(list_ipenc[:,101:])

    print(list_ipenc[1])
    print(list_ipenc[:,101:])
    print(a)

    
