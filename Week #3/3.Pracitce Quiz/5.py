def sum_positive_numbers(n):
  if n == 0:
    return 0
  return sum_positive_numbers( n - 1 ) + n 

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15