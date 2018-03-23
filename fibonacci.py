def fib(max):
    a,b = 0,1
    while a <= max:
        yield a
        a,b = b, a+b

list=[]
maxNum = 10000
for i in fib(maxNum):
    list.append(i)

print(list)

