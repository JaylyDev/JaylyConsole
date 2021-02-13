print ("Enter a temperature")
temperature = float(input())
print ("What do you want to convert the temperature to?")
print ("Type 'C' for Celeius, 'F' for Fahrenheit.")
conversion = (input())
if conversion == "C":
  output = 5*(temperature-32)/9
  print (output)
elif conversion == "F":
  output = temperature*1.8+32
  print (output)
else:
  print ("Invalid Input.")