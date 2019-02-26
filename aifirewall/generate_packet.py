import random
def generate_packet():
    with open('pk.txt', 'w') as file_data:
        protocol = ['01','06','11']
        for i in range(0,100):
            file_data.write('+---------+---------------+----------+' + '\n')
            file_data.write('17:58:28,100,000   ETHER' + '\n')
            file_data.write('|0   |2a|19|e2|37|d7|76|ab|6f|f4|2c|6a|00|08|00|45|00|00|2e|00|00|40|00|40|')

            protocol = random.choice(protocol)
            chksm = hex(random.randint(1, 256))[2:]
            if len(chksm) != 2:
                chksm = '0'+chksm
            file_data.write(chksm)

            file_data.write('\n\n')

generate_packet()