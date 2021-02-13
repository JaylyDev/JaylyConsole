print ("Which year you were born in?")
year_they_were_born_in = int(input())
if year_they_were_born_in >= 1996:
  print ("You were born in " + "Gen Z" + ".")
elif year_they_were_born_in >= 1977 <= 1995:
  print ("You were born in " + "Millennials" + ".")
elif year_they_were_born_in >= 1965 <= 1976:
  print ("You were born in " + "Generation X" + ".")
elif year_they_were_born_in >= 1946 <= 1964:
  print ("You were born in " + "Baby Boomers" + ".")
elif year_they_were_born_in <= 1945:
  print ("You were born in " + "Traditionalists" + ".")
elif year_they_were_born_in >= 1977 <= 1985:
  print ("You were born in " + "micro-generation" + ".")