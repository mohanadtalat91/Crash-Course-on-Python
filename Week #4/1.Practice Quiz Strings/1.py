def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	input_string = input_string.lower()
	# Traverse through each letter of the input string
	for i in range( 0 , len(input_string) ):
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		if input_string[i] != " ":
			new_string += input_string[i]
		if input_string[len(input_string)-i-1] != " ":
			reverse_string += input_string[len(input_string)-i-1]
	# Compare the strings
	if new_string == reverse_string:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True