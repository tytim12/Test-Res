#output every 0 in list parameter

def findZero(list=[]):
    output = []
    length = len(list)
    for i in range(0,length):
        if list[i] == 0:
            output.append(list[i])
    return output

input = [-1, 0, 0, 8, -9, 2, 0, 2, 1, 0, 'a']
output = findZero(input)
print('List of zeros: ', output)


