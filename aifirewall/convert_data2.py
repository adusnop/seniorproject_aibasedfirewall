import numpy as np
def array_rule():
    array_data = []
    array_action = []

    with open('ftest.txt', 'r') as filehandle2:
        for line in filehandle2:
            lst = []
            if line[0] != 'A' :
                for i in line:
                    if i != ',' and i != '\n':
                        lst.append(float(i))
                array_action.append([lst.pop(0)])
                array_data.append(lst)

    test_data = np.array(array_data)
    test_data = np.float32(test_data)
    print(test_data)
    print(test_data.dtype)

    action_test_data = np.array(array_action)
    action_test_data = np.float32(action_test_data)

    print(action_test_data)
    return test_data, action_test_data
array_rule()

def array_packet():
    array_data = []
    array_action = []

    with open('ftrain.txt', 'r') as filehandle2:
        for line in filehandle2:
            lst = []
            if line[0] != 'A':
                for i in line:
                    if i != ',' and i != '\n':
                        lst.append(float(i))
                array_action.append([lst.pop(0)])
                array_data.append(lst)

    test_data = np.array(array_data)
    test_data = np.float32(test_data)
    print(test_data)
    print(test_data.shape)
    action_test_data = np.array(array_action)
    action_test_data = np.float32(action_test_data)

    print(action_test_data)
    print(action_test_data.shape)

    return test_data,action_test_data


array_packet()