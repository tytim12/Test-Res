#bump every number to 0 from input list, and output results

def countDown(input=[]):
    list = []
    for num in input:
        list.append(num)
        if num < 0:
            while num < 0:
                num += 1
                list.append(num)
        else:
            while num > 0:
                num -= 1
                list.append(num)
    return list

input = [4,0,-3]
output = countDown(input)
print(output)