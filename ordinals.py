def numbertoordinal(n):
	special = { 1:'st', 2:'nd', 3:'rd'}
	if n == 0:
		ordinal = '0'
		return ordinal
	elif 4 <= n <= 20:
		ordinal = 'th'
		return ordinal
	elif n < 100:
		new_n = n % 10
		if new_n < 4:	
			for x in special.keys():
				if new_n == x:
					ordinal = special[x]
					return ordinal
		else:
			ordinal = 'th'
			return ordinal

for i in range(100):
	print( str(i) + ' is ' + str(numbertoordinal(i)))