def format_address(address_string):
  # Declare variables
  x = str('')
  y = str('')
  # Separate the address string into parts
  parts = address_string.split() 
  # Traverse through the address parts
  for i in parts:
    # Determine if the address part is the
    # house number or part of the street name
    if(i.isdigit()):
      x = i 
    else:
      y += i 
      y += ' '

  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
  return "house number {} on street named {}".format(x,y)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 cairth Center Drive"))
# Should print "house number 55 on street named North Center Drive"
