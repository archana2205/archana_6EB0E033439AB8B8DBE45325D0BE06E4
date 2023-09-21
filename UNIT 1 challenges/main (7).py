year=int(input("Enter year to be checked:"))
if year%4==0:
  if year%100==0:
    if year%400==0:
       print("the year is aleap year!")
    else:
      print("the year is not a leap year!")
  else:
    print("the year is aleap year!")
else:
  print("the year is not a leap year!")