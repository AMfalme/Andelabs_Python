def data_type(arg):
  
  if isinstance(arg, str):
    return len(arg)
    
  elif type(arg) == type(None):
    return ("no value" )
    
  elif isinstance(arg, bool):
    return arg
    
  elif isinstance(arg, int):
    if arg < 100:
      return ("less than 100")
      
    elif arg > 100:
      return ("more than 100")
      
    else:
      return ("equal to 100")
      
  elif type(arg) == type([]):
    try:
      return arg[2]
    except IndexError:
        return (None)
          
    

  
  
