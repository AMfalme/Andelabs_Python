def multiples(n):
	sum = 0
	for i in range(0,n):
		if i % 9 == 0:
			sum =sum + i
	print(sum)
multiples(250)