import random
import math

def wallis(n):
	x = 1
	for i in range(1, n+1):
		x = x*4*(i**2)/(4*(i**2)-1)
	return x*2

		

def monte_carlo(n):
	area_sq = 0
	area_cir = 0
	for i in range(0, n) :
		x, y = random.random(), random.random()
		if math.sqrt(x**2 + y**2)<=1:
			area_cir+=1
		else :
			area_sq+=1
	return 4*area_cir/(area_cir + area_sq)
	
n = int(input("Enter number of iterations : "))
print(wallis(n))
print(monte_carlo(n))
