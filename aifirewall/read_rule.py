import random

def read_rules():
    with open('rule.txt', 'r') as filehandle2,  open('t_rule.csv', 'w') as file_data:
        file_data.write('Action' + ',')
        file_data.write('Direction' + ',')
        file_data.write('Interface' + ',')
        file_data.write('Source_ip' + ',')
        file_data.write('Subnet_ip' + ',')
        file_data.write('Port' + ',')
        file_data.write('Dest_ip' + ',')
        file_data.write('Subnet_ip' + ',')
        file_data.write('Port' + ',')
        file_data.write('Protocol' + ',')
        file_data.write('\n')

        for line in filehandle2:
            line_ip = line.split(' ')
            subnet_ip = '255.255.255.0'
            action = line_ip[0]
            direction = line_ip[1]
            source_ip = line_ip[5]
            source_ip = source_ip[:8]
            interface = line_ip[3]
            dest_ip = line_ip[7]
            dest_ip = dest_ip[:13]
            port = line_ip[9]
            protocol_rule = line_ip[10]


            for j in range(100):
                source_ip = source_ip[:8]
                host_ip = str(random.randint(0,255))
                host_ip += '.'
                host_ip += str(random.randint(0,255))
                source_ip += host_ip
                file_data.write(action + ',')
                file_data.write(direction + ',')
                file_data.write(interface+ ',')
                file_data.write(source_ip + ',')
                file_data.write(subnet_ip + ',')
                file_data.write(port + ',')
                file_data.write(dest_ip + ',')
                file_data.write(subnet_ip + ',')
                file_data.write(port+',')
                file_data.write(protocol_rule)
            print(source_ip)


read_rules()