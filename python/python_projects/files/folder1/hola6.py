str = 'X-DSPAM-Confidence: 0.8475'

print(str)
findme = str.find(":")
print(findme)
numbers = str[findme + 2:]
print(numbers)
floatn = float(numbers)
print(floatn)