from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
def test_data():
    # define an empty list
    list_ip1 = []
    list_action = []

    # open file and read the content in a list
    with open('ip_test.txt', 'r+') as filehandle:  
        for line in filehandle:
            # remove linebreak which is the last character of the string
            ip = line[:-1]
            ip = ip + '/24'
            filehandle.write(ip+'\n')
            # add item to the list
            list_ip1.append(ip)
            print(ip)
    with open('action_test.txt', 'w') as filehandle:  
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
    print(array_action)
    # integer encode
    label_encoder = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(array_ip)
    integer_encoded2 = label_encoder.fit_transform(array_action)
    print(integer_encoded2)
    # binary encode
    onehot_encoder = OneHotEncoder(sparse=False)
    integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
    onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
    integer_encoded2 = integer_encoded2.reshape(len(integer_encoded2), 1)
    onehot_encoded2 = onehot_encoder.fit_transform(integer_encoded2)

    print(onehot_encoded)
    print(onehot_encoded2)
    # invert first example
    # inverted = label_encoder.inverse_transform([argmax(onehot_encoded[0, :])])
    inverted2 = label_encoder.inverse_transform([argmax(onehot_encoded2[0, :])])
    #print(inverted)
    print(inverted2)
    return onehot_encoded, onehot_encoded2
