import random


def create_ip():
    ip_range = ['192.168.', '100.100.']
    with open('IP_train.txt', 'w') as filehandle, open('IP_input.txt', 'w') as filehandle2:
        for i in range(500):
            ip_range2 = random.choice(ip_range)
            ip_source_train = ip_range2 + str(random.randint(1, 256)) + '.' + str(random.randint(1, 256)) + '/16' + '\n'
            ip_source_input = ip_range2 + str(random.randint(1, 256)) + '.' + str(random.randint(1, 256)) + '/16' + '\n'
            filehandle.write(ip_source_train)
            filehandle2.write(ip_source_input)


create_ip()


def write_rules_train():
    ip_range = ['192.168.', '10.10.']
    ip_destlist = ['161.246.34.11/16', '161.246.34.21/16']
    protocol_list = ['tcp', 'udp']
    with open('IP_train.txt', 'r') as filehandle3, open('rules_train.csv', 'w') as file_data:
        d_count = 0
        a_count = 0
        for line in filehandle3:
            ip = line[:-1]
            ip_dest = random.choice(ip_destlist)
            if ip_dest == '161.246.34.21/16':
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
            file_data.write(ip[0:8] + ',')
            file_data.write(ip[8:len(ip)] + ',')
            file_data.write(port + ',')
            file_data.write(str(ip_dest[0:8]) + ',')
            file_data.write(str(ip_dest[8:len(ip)]) + ',')
            file_data.write(port + ',')
            file_data.write('\n')

        print(a_count)
        print(d_count)


write_rules_train()


def write_rules_input():
    ip_destlist = ['161.246.34.11/16', '161.246.34.21/16']
    protocol_list = ['tcp', 'udp']
    with open('IP_input.txt', 'r') as filehandle4, open('rules_input.csv', 'w') as file_data_input:
        d_count = 0
        a_count = 0
        for line in filehandle4:
            ip = line[:-1]
            ip_dest = random.choice(ip_destlist)
            if ip_dest == '161.246.34.21/16':
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
            file_data_input.write(action)
            file_data_input.write('in,')
            file_data_input.write('eth0,')
            file_data_input.write(protocol + ',')
            file_data_input.write(ip[0:8] + ',')
            file_data_input.write(ip[8:len(ip)] + ',')
            file_data_input.write(port + ',')
            file_data_input.write(str(ip_dest[0:8]) + ',')
            file_data_input.write(str(ip_dest[8:len(ip)]) + ',')
            file_data_input.write(port + ',')
            file_data_input.write('\n')

        print(a_count)
        print(d_count)


write_rules_input()
