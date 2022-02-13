def count_letters(text):
  result = {}
  text = text.lower() 
  # Go through each letter in the text
  for letter in text:
    # Check if the letter needs to be counted or not
    if letter.isalpha():
       if letter not in result:
         result[letter] = 1 
       else:
          result[letter] += 1   
    # Add or increment the value in the dictionary
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}