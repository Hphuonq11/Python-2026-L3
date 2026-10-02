def remove_dollar_sign(s):
  return s.replace("$", "")

s = (input("Enter a string:"))
result = remove_dollar_sign(s)
print(result)