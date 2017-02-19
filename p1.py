import numpy as np
from scipy.optimize import curve_fit
import scipy
import csv


def do1():

	x=[]
	y=[]
	with open('1.csv', 'r') as csvfile:
		spamreader = csv.reader(csvfile)
		for row in spamreader:
			x.append(float(row[0]))
			y.append(float(row[1]))


	import matplotlib.pyplot as plt
	plt.plot(x,y)
	plt.show()

	max_y = max(y)
	return max_y