def wallis(n):
	x = 1
	for i in range(1, n+1):
		x = x*4*(i**2)/(4*(i**2)-1)
	return x*2

n = int(input("Enter the number of iterations"))
print(wallis(n))	
		
