from flask import Flask, render_template, request
import random

app = Flask("Pi Estimation")

@app.route("/")
def pi_estimator():
	return render_template("index.html")
	
@app.route("/estimate")
def estimate():
	method = request.form['Method']
	iterations = request.form['iter']
	
	
@app.route("/pi")	
def monte_carlo(iters = 5000):
	inside = 0.0
	for _ in range(iters):
		x = random.random()
		y = random.random()
		if (x**2 + y**2) <=1:
			inside += 1
	answer = 4*inside/iters
	
	return render_template("estimate.html", algorithm = "Monte Carlo", iters = iters, value = answer)
	

@app.route("/pi2")	
def wallis(n = 5000):
	x = 1
	for i in range(1, n+1):
		x = x*4*(i**2)/(4*(i**2)-1)
	x = x*2
	return render_template("estimate.html", algorithm = "Wallis", iters = n, value = x)
	 
if __name__ == "__main__":
	app.run()
