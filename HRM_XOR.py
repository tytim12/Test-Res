# input a list of tuples
# output if each tuple's sign are the same

def XOR(list=[()]):
    output=[]
    for tup in list:
        if tup[0] * tup[1] > 0:
            output.append(0)
        elif tup[0] * tup[1] == 0:
            output.append(0)
        else:
            output.append(1)
    return output




input = [(1,2), (-1,-2), (1,-9), (0,-1), (1, 0), (0, 0)]
output = XOR(input)

print("Expected output: ", [0, 0, 1, 0, 0, 0])
print("XOR list output ", output)