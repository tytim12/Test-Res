for i in range(1,10):
	for j in range(1,i+1):
		str = '{} x {} = {}'.format(i, j, i*j)
		print(str.ljust(12), end=' ')
	print()