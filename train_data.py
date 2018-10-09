from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

def train_data():
    # define an empty list
    list_ip1 = []
    list_action = []

    # open file and read the content in a list
    with open('IP1.txt', 'r') as filehandle:  
        for line in filehandle:
            # remove linebreak which is the last character of the string
            ip = line[:-1]
            # add item to the list
            list_ip1.append(ip)
    with open('action.txt', 'w') as filehandle:  
        for listitem in list_ip1:
            if listitem[1] == '9':
                filehandle.write('Allow\n')
                list_action.append('Allow')
            else:
                filehandle.write('Deny\n')
                list_action.append('Deny')
   
    # define example
    array_ip = array(list_ip1)
    array_action = array(list_action)
    #print(array_action)
    # integer encode
    label_encoder = LabelEncoder()
    label_encoder2 = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(array_ip)
    integer_encoded2 = label_encoder2.fit_transform(array_action)
    #print(integer_encoded2)
    # binary encode
    onehot_encoder = OneHotEncoder(sparse=False)
    onehot_encoder2 = OneHotEncoder(sparse=False)
    integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
    onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
    
    integer_encoded2 = integer_encoded2.reshape(len(integer_encoded2), 1)
    onehot_encoded2 = onehot_encoder2.fit_transform(integer_encoded2)

    return onehot_encoded, onehot_encoded2,label_encoder2
    
    #print(onehot_encoded)
    #print(onehot_encoded2)
def invert_output(label_encoder2, onehot_encoded2):
    # invert first example
    #inverted = label_encoder.inverse_transform([argmax(onehot_encoded[0, :])])
    for i in range(len(onehot_encoded2)):
        inverted2 = label_encoder2.inverse_transform([argmax(onehot_encoded2[i, :])])
    #print(inverted)
        print(inverted2)
    
