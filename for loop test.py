def prime(max):
    list = []
    for num in range(2,max):
        for n in range(2,num):
            if num % n == 0:
                break
        else:
            list.append(num)
    return list

numList = prime(100)
print(numList)