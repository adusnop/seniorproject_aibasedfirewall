import random

def c_action(act):
    if act == 'allow':
        value_b = '1'
    else:
        value_b = '0'
    return value_b

def c_direction(direct):
    if direct == 'in':
        value_b = '1'
        mask = '1'
    else:
        value_b = '0'
        mask = '1'
    return value_b, mask

def c_interface(intf):
    if intf == 'eth0':
        value_b = '001'
        mask = '001'
    else:
        value_b = '000'
        mask = '000'
    return value_b, mask

def c_ip(r_ip):
    ip_split = r_ip.split('.')
    value_b = ''
    for i in range(0, 4):
        ip = ip_split[i]
        ip_b = bin(int(ip))
        ip_b = ip_b[2:]
        if len(ip_b) != 8 :
            z_count = 8 - len(ip_b)
            ip_b = '0'*(z_count) + ip_b
        value_b += ip_b

    return value_b

def c_port(port):
    if port != 'any':
        port_b = bin(int(port))
        value_b = port_b[2:]
        length1 = len(value_b)
        if length1 != 8:
            z_count = 8 - length1
            value_b = '0'*(z_count) + value_b
        mask = '0'*(16-int(length1)) + '1'*length1
    else:
        value_b = '0000000000000000'
        mask = '0000000000000000'

    return value_b, mask

def c_protocol(protocol):
    protocol = protocol[:3]
    if protocol != 'any':
        port_b = bin(int(protocol))
        value_b = port_b[2:]
        length1 = len(value_b)
        mask = '0'*(8-int(length1)) + '1'*length1
    else:
        value_b = '00000000'
        mask = '00000000'
    return value_b, mask

def convert_rules():
    rule_list = []
    with open('c_rule.csv', 'w') as file_data,  open('t_rule.csv', 'r') as filehandle2:
        file_data.write('Action' + ',')
        file_data.write('Direction' + ',')
        file_data.write('Mask' + ',')
        file_data.write('Interface' + ',')
        file_data.write('Mask' + ',')
        file_data.write('Source_ip' + ',')
        file_data.write('Mask' + ',')
        file_data.write('Port' + ',')
        file_data.write('Mask' + ',')
        file_data.write('Dest_ip' + ',')
        file_data.write('Mask' + ',')
        file_data.write('Port' + ',')
        file_data.write('Mask' + ',')
        file_data.write('Protocol' + ',')
        file_data.write('Mask' + ',')
        file_data.write('\n')


        for line in filehandle2:
            if line[0] != 'A':
                data_list = []
                line_rule = line.split(',')
                action_bit = c_action(line_rule[0])
                print(line_rule[1])
                direct_bit, direct_mask = c_direction(line_rule[1])
                interface_bit, interface_mask = c_interface(line_rule[2])
                source_ip_bit = c_ip(line_rule[3])
                source_ip_mask_bit = c_ip(line_rule[4])
                source_port_bit,source_port_mask_bit = c_port(line_rule[5])
                dest_ip_bit = c_ip(line_rule[6])
                dest_ip_mask_bit = c_ip(line_rule[7])
                dest_port_bit, dest_port_mask_bit = c_port(line_rule[8])
                protocol_bit, protocol_mask_bit = c_protocol(line_rule[9])
                file_data.write(action_bit+',')
                file_data.write(direct_bit+',')
                file_data.write(direct_mask+',')
                file_data.write(interface_bit + ',')
                file_data.write(interface_mask + ',')
                file_data.write(source_ip_bit+',')
                file_data.write(source_ip_mask_bit + ',')
                file_data.write(source_port_bit + ',')
                file_data.write(source_port_mask_bit+',')
                file_data.write(dest_ip_bit + ',')
                file_data.write(dest_ip_mask_bit + ',')
                file_data.write(dest_port_bit+',')
                file_data.write(dest_port_mask_bit + ',')
                file_data.write(protocol_bit + ',')
                file_data.write(protocol_mask_bit)
                file_data.write('\n')


convert_rules()
