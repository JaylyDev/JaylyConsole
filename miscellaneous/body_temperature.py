print ("What is your current temperature? " + "(Answer in degree calcius.)")
temperature = float(input())
if temperature >= 39.4:
  print ("Go to the hospital!")
elif temperature >= 37.6:
  print ("Go take some rest.")
else:
  print ("You're fine.")