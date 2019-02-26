import random

def create_ip_input():
    ip_list = []
    with open('packet_diff.txt', 'w') as filehandle2, open('ip400.txt', 'r') as filehandle3:
        for line in filehandle3:
            ip = line[:-1]
            ip_list.append(ip)

        for i in range(0, 100):
            ip_list.append(str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(
                random.randint(0, 255)) + '.' + str(random.randint(0, 255)))

        random.shuffle(ip_list)
        for l in ip_list:
            filehandle2.write(l)
            filehandle2.write('\n')


create_ip_input()

def write_packet():
    ip_destlist = ['161.246.34.11', '161.246.34.21']
    protocol_list = ['TCP', 'UDP','ICMP']
    with open('packet_diff.txt', 'r') as filehandle, open('packet_diff.csv', 'w') as file_data:
        d_count = 0
        a_count = 0
        for line in filehandle:
            ip = line[:-1]
            ip_dest = random.choice(ip_destlist)
            if ip_dest == '161.246.34.21':
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
            file_data.write('255.255.255.255' + ',')
            file_data.write(port + ',')
            file_data.write(ip_dest + ',')
            file_data.write('255.255.255.0' + ',')
            file_data.write(port + ',')
            file_data.write('\n')

        print(a_count)
        print(d_count)


write_packet()
