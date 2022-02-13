def lucky_number(name):
  number = len(name) * 9
  res = "Hello " + name + ". Your lucky number is " + str(number)
  return res
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))