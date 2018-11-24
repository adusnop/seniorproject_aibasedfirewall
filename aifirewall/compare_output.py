import csv


def compare_output():
    with open('output.csv', 'r') as filehandle, open('rules_input.csv', 'r') as filehandle2:
        line = csv.reader(filehandle)
        line2 = csv.reader(filehandle2)
        a = 0
        list_input = [li[:-1] for li in line]
        list_output = [li[:-1] for li in line2]
        for i in range(300):
            if list_input[i] == list_output[i]:
                a += 1
                print(list_output[i])
        print(a)
        print('percent: ' + str((a/300)*100))

compare_output()