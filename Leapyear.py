yearNum=int(input("Enter a year:"))
count=0

if yearNum % 4 == 0 and yearNum % 100 != 0 or yearNum % 400 == 0:
 print("This year is a leap year!")

else:
  print("This year is not a leap year!")
count=count+1