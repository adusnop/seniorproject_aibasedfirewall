import random
def write_rules():
    ip_destlist = ['161.246.34.11/16', '161.246.34.21/16']
    # open file and read the content in a list
    with open('ip_test.txt', 'r') as filehandle, open('rules1.txt', 'w') as filehandle2:  
        for line in filehandle:
            # remove linebreak which is the last character of the string
            ip = line[:-1]
            ip = ip + '/24'
            filehandle2.write(ip+',')
            
            ip_dest = random.choice(ip_destlist)
            filehandle2.write(ip_dest+',')
            if ip[1] == '0':
                if ip_dest == '161.246.34.21/16':
                    filehandle2.write('Deny')
                else:
                    filehandle2.write('Allow')
            else:
                filehandle2.write('Allow')
            filehandle2.write('\n')
            # add item to the list
            print(ip)
