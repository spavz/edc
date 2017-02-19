import numpy as np
from scipy.optimize import curve_fit
import scipy
import csv

def do2():

	x=[]
	y=[]
	with open('2.csv', 'r') as csvfile:
		spamreader = csv.reader(csvfile)
		for row in spamreader:
			x.append(float(row[0]))
			y.append(float(row[1]))


	def func(x, a, b,c):
			return c-(a*(x-b)**2)


	popt, pcov = curve_fit(func, x, y)

	a1,b1,c1=popt





	import matplotlib.pyplot as plt
	plt.plot(x,y)
	plt.show()	

	print(popt)
	max_x = scipy.optimize.fmin(lambda x: -func(x,a1,b1,c1), 0)
	max_y = abs(func(max_x,a1,b1,c1))
	return max_y 









