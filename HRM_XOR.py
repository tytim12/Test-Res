# input a list of tuples
# output if each tuple's sign are the same

list = [(1,2), (-1,-2), (1,-9), (0,-1), (1, 0), (0, 0)]
output = []
for tup in list:
    # determine if the sign of each number is the same
    if (tup[0] * tup[1] > 0):
        output.append(0)
    elif (tup[0] * tup[1] == 0):
        output.append(0)
    else:
        output.append(1)

print("Expected output: ", [0, 0, 1, 0, 0, 0])
print("XOR list output ", output)