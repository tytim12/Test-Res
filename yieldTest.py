def prime(max):
    for num1 in range(2, max):
        for num2 in range(2, num1):
            if num1 % num2 == 0:
                break
        else:
            yield num1

maxNum = 100
list=[]
for i in prime(maxNum):
    list.append(i)
print(list)