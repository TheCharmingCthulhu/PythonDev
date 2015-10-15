def FirstReverse(str): 
  output = ''
  for I in range(len(str)-1, -1, -1):
    output += str[I]
  return output

print FirstReverse('Hello World');
