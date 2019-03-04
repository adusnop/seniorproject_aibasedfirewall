def conv_to_bit(value_hex, type):
    value_dec = int(value_hex, 16)
    value_bit = bin(value_dec)
    value_bit = value_bit[2:]

    if type == 'ip':
        if len(value_bit) != 8 :
            z_count = 8 - len(value_bit)
            value_bit = '0'*(z_count) + value_bit
    elif type == 'port':
        if len(value_bit) != 16 :
            z_count = 16 - len(value_bit)
            value_bit = '0'*(z_count) + value_bit
    elif type == 'protocol':
        if len(value_bit) != 8 :
            z_count = 8 - len(value_bit)
            value_bit = '0'*(z_count) + value_bit

    return value_bit

def convert_packet():
    with open('c_packet.csv', 'w') as file_data,  open('pk.txt', 'r') as file_packt:
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

        a = 1
        for line in file_packt:

            if line[0] == '|':
                protocol_hex = line[75]
                protocol_hex += line[76]
                protocol_bit = conv_to_bit(protocol_hex, 'protocol')

                s_ip_1hex = line[84]
                s_ip_1hex += line[85]
                s_ip_1bit = conv_to_bit(s_ip_1hex, 'ip')
                s_ip_2hex = line[87]
                s_ip_2hex += line[88]
                s_ip_2bit = conv_to_bit(s_ip_2hex, 'ip')
                s_ip_3hex = line[90]
                s_ip_3hex += line[91]
                s_ip_3bit = conv_to_bit(s_ip_3hex, 'ip')
                s_ip_4hex = line[93]
                s_ip_4hex += line[94]
                s_ip_4bit = conv_to_bit(s_ip_4hex, 'ip')
                s_ip_bit = s_ip_1bit+s_ip_2bit+s_ip_3bit+s_ip_4bit

                d_ip_1hex = line[96]
                d_ip_1hex += line[97]
                d_ip_1bit = conv_to_bit(d_ip_1hex, 'ip')
                d_ip_2hex = line[99]
                d_ip_2hex += line[100]
                d_ip_2bit = conv_to_bit(d_ip_2hex, 'ip')
                d_ip_3hex = line[102]
                d_ip_3hex += line[103]
                d_ip_3bit = conv_to_bit(d_ip_3hex, 'ip')
                d_ip_4hex = line[105]
                d_ip_4hex += line[106]
                d_ip_4bit = conv_to_bit(d_ip_4hex, 'ip')
                d_ip_bit = d_ip_1bit+d_ip_2bit+d_ip_3bit+d_ip_4bit

                s_port_hex = line[108]+line[109]+line[111]+line[112]
                s_port_bit = conv_to_bit(s_port_hex, 'port')

                d_port_hex = line[108]+line[109]+line[111]+line[112]
                d_port_bit = conv_to_bit(d_port_hex, 'port')

                file_data.write('1' + ',')
                file_data.write('0' + ',')
                file_data.write('1' + ',')
                file_data.write('000' + ',')
                file_data.write('111' + ',')
                file_data.write(s_ip_bit + ',')
                file_data.write('11111111111111111111111111111111' + ',')
                file_data.write(s_port_bit + ',')
                file_data.write('1111111111111111' + ',')
                file_data.write(d_ip_bit + ',')
                file_data.write('11111111111111111111111111111111' + ',')
                file_data.write(d_port_bit + ',')
                file_data.write('1111111111111111' + ',')
                file_data.write(protocol_bit + ',')
                file_data.write('11111111')
                file_data.write('\n')

                a += 1
                print(s_port_bit)
                print(a)




convert_packet()