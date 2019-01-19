import csv


def compare_output():
    with open('output.csv', 'r') as filehandle, open('rules_input2_diffinput.csv', 'r') as filehandle2:
        line = csv.reader(filehandle)
        line2 = csv.reader(filehandle2)
        correct = 0
        list_input = [li[:-1] for li in line2]
        list_output = [li[:-1] for li in line]
        for i in range(500):
            if list_input[i] == list_output[i]:
                correct += 1
                print(list_output[i])
            else:
                print('**************' + str(list_output[i]))
        print(correct)
        print('percent: ' + str((correct/500)*100))

compare_output()