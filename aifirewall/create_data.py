import random


def write_rules():
    ip_destlist = ['161.246.34.11/16', '161.246.34.21/16']
    with open('Ip_list2.txt', 'r') as filehandle, open('rules1.csv', 'w') as filehandle2, open('rules2.csv',
                                                                                               'w') as filehandle3:
        d_count = 0
        a_count = 0
        l_count = 0
        for line in filehandle:
            l_count += 1
            if l_count >= 801:
                file_data = filehandle2
            else:
                file_data = filehandle2
            ip = line[:-1]
            ip = ip + '/24'
            ip_dest = random.choice(ip_destlist)

            if ip_dest == '161.246.34.21/16':
                if ip[1] == '0':
                    file_data.write('Deny,')
                    port = '21'
                    d_count += 1
                else:
                    file_data.write('Allow,')
                    port = '21'
                    a_count += 1
            else:
                file_data.write('Allow,')
                a_count += 1
                port = '80'

            file_data.write('TCP' + ',')
            file_data.write(ip + ',')
            file_data.write(port + ',')
            file_data.write(ip_dest + ',')
            file_data.write(port)

            file_data.write('\n')
            # add item to the list
        print(a_count)
        print(d_count)


write_rules()
