def find_max_min(arg):
  minimum = arg[0]
  maximum = arg[1]
  maxmin = True
  for number in arg:
  	if number < minimum:
  		minimum = number
  		
  		
  	elif number > maximum:
  		maximum = number
  		
  	elif minimum == maximum:
  	  maxmin = False
  	  
  	  
  arr = [minimum, maximum] 	  
  ar = [minimum] 	  
  if maxmin == True:
    return arr
  else:
    return ar
