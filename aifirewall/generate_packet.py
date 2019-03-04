import random
def hex_random():
    value = hex(random.randint(1, 255))[2:]
    if len(value) != 2:
        value = '0' + value
    value = value + '|'
    return value
def generate_packet():
    with open('pk.txt', 'w') as file_data:
        protocol_set = ['01|','06|','11|']
        destination_ip = ['a1|f6|22|15|', 'a1|f6|22|0b|']
        port = ['00|50|', '00|16|']
        for i in range(0,100):
            file_data.write('+---------+---------------+----------+' + '\n')
            file_data.write('17:58:28,100,000   ETHER' + '\n')
            file_data.write('|0   |2a|19|e2|37|d7|76|ab|6f|f4|2c|6a|00|08|00|45|00|00|2e|00|00|40|00|40|')

            protocol = random.choice(protocol_set)
            dest_ip = random.choice(destination_ip)
            s_port = random.choice(port)
            d_port = s_port
            file_data.write(protocol)
            file_data.write(hex_random())
            file_data.write(hex_random())
            file_data.write('c0' + '|' + 'a8' + '|')
            file_data.write(hex_random())
            file_data.write(hex_random())
            file_data.write(dest_ip)
            file_data.write(s_port)
            file_data.write(d_port)
            file_data.write('00|00|00|00|00|00|00|00|00|00|00|00|17|fd|00|00|00|00|00|00|00|00|')


            file_data.write('\n\n')

generate_packet()