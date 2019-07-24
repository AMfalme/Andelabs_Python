def arith_geo(arg):
	
    if len(arg) == 0:
        return 0
    arith_prog = arg[1] - arg[0]
    geo_prog = arg[1]/arg[0]
    arithmetic = True
    Geometric = True
    for index in range(len(arg)-1):
      if arg[index + 1] - arg[index] != arith_prog:
        arithmetic = False

      try:
        if arg[index + 1]/arg[index] != geo_prog:
          Geometric = False
      except ZeroDivisionError:
        Geometric = False
        
    if Geometric:
      return ('Geometric')
    elif arithmetic:
      return ('Arithmetic')
      
    else:
      return -1
