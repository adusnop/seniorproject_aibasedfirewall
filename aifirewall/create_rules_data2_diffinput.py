import random
import itertools

def write_rules_train():
    ip_destlist = ['161.246.34.11/24', '161.246.34.21/24']
    protocol_list = ['tcp', 'udp']
    with open('IP_input2_diffinput.txt', 'r') as filehandle3, open('rules_train2_diffinput.csv', 'w') as file_data:
        d_count = 0
        a_count = 0
        for line in itertools.islice(filehandle3, 0, 500):
            ip = line[:-1]
            ip_dest = random.choice(ip_destlist)
            if ip_dest == '161.246.34.21/24':
                if ip[1] == '0':
                    action = 'deny,'
                    port = '21'
                    d_count += 1
                else:
                    action = 'allow,'
                    port = '21'
                    a_count += 1
            else:
                action = 'allow,'
                a_count += 1
                port = '80'

            protocol = random.choice(protocol_list)
            file_data.write(action)
            file_data.write('in,')
            file_data.write('eth0,')
            file_data.write(protocol + ',')
            file_data.write(ip + ',')
            file_data.write(port + ',')
            file_data.write(str(ip_dest) + ',')
            file_data.write(port + ',')
            file_data.write('\n')

        print(a_count)
        print(d_count)


write_rules_train()

def write_rules_input():
    ip_destlist = ['161.246.34.11/24', '161.246.34.21/24']
    protocol_list = ['tcp', 'udp']
    with open('IP_input2_diffinput.txt', 'r') as filehandle4, open('rules_input2_diffinput.csv', 'w') as file_data_input:
        d_count = 0
        a_count = 0
        for line in itertools.islice(filehandle4, 0, 500):
            ip = line[:-1]
            ip_dest = random.choice(ip_destlist)
            if ip_dest == '161.246.34.21/24':
                if ip[1] == '9':
                    action = 'allow,'
                    port = '21'
                    a_count += 1
                else:
                    action = 'deny,'
                    port = '21'
                    d_count += 1
            else:
                action = 'allow,'
                a_count += 1
                port = '80'

            protocol = random.choice(protocol_list)
            file_data_input.write(action)
            file_data_input.write('in,')
            file_data_input.write('eth0,')
            file_data_input.write(protocol + ',')
            file_data_input.write(ip + ',')
            file_data_input.write(port + ',')
            file_data_input.write(str(ip_dest) + ',')
            file_data_input.write(port + ',')
            file_data_input.write('\n')

        print(a_count)
        print(d_count)


write_rules_input()
