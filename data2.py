# define an empty list
list_ip1 = []
list_ip2 = []

# open file and read the content in a list
with open('IP1.txt', 'r') as filehandle:  
    for line in filehandle:
        # remove linebreak which is the last character of the string
        ip = line[:-1]
        # add item to the list
        list_ip1.append(ip)

with open('IP2.txt', 'w') as filehandle:  
    for listitem in list_ip1:
        if int(listitem[1] == '.':
               listitem = '00'+ listitem
        else if int(listitem[2] == '.':
                    listitem = '0'+ listitem
                    
        if int(listitem[5] == '.':
               listitem = '00'+ listitem
        else if int(listitem[6] == '.':
                    listitem = '0'+ listitem
                    
        if int(listitem[9] == '.':
               listitem = '00'+ listitem
        else if int(listitem[10] == '.':
                    listitem = '0'+ listitem
                    
        if int(listitem[13] == '.':
               listitem = '00'+ listitem
        else if int(listitem[14] == '':
                    listitem = '0'+ listitem
            
        filehandle.write('%s\n' % listitem)

with open('action.txt', 'w') as filehandle:  
    for listitem in list_ip2:
        print(listitem)
        filehandle.write('%s\n' % listitem)
