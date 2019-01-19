import random

def create_ip_train():
    ip_list = []
    ip_range_1 = random.sample(range(255), 250)
    ip_range_2 = random.sample(range(255), 250)
    with open('IP_train2.txt', 'w') as train_ip:

        for i in range(0, 250):
            ip_list.append('192.168.' + str(ip_range_1[i]) + '.' + '0' + '/16')
            ip_list.append('100.100.' + str(ip_range_2[i]) + '.' + '0' + '/16')

        random.shuffle(ip_list)
        for l in ip_list:
            train_ip.write(l)
            train_ip.write('\n')


create_ip_train()


def create_ip_input():
    ip_list = []
    with open('IP_input2_diffinput.txt', 'w') as filehandle2, open('ip_input_2diff500.txt', 'r') as filehandle3:
        for line in filehandle3:
            ip = line[:-1]
            ip_list.append(ip + '/24')

        for i in range(0, 200):
            ip_list.append(str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(
                random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '/24')

        random.shuffle(ip_list)
        for l in ip_list:
            filehandle2.write(l)
            filehandle2.write('\n')


create_ip_input()