def longest_substring(digits):
  longSubString = ""
  currentDigits = [int(digits[0])]
  for digit in digits[1:]:
    if (currentDigits[-1] + int(digit)) % 2 == 1:
      currentDigits.append(int(digit))
    else:
      if len(currentDigits) > len(longSubString):
        longSubString = ''.join(str(d) for d in currentDigits)
      currentDigits = [int(digit)]
  if len(currentDigits) > len(longSubString):
    longSubString = ''.join(str(d) for d in currentDigits)
  return longSubString


print(longest_substring("225424272163254474441338664823"))
print(longest_substring("594127169973391692147228678476") )
print(longest_substring("721449827599186159274227324466") )