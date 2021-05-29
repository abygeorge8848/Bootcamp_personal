def is_leap(year):
	leap = False
	if year%4==0:
		leap = True
		return "Leap year"
	else:
		return "Not leap"
year = 0
while(year is not 2020):		
	year = int(input("Enter the year: "))
	print(is_leap(year))
	break


