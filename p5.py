import numpy as np
from scipy.optimize import curve_fit
import scipy
import csv


def do5():

	x=[]
	y=[]
	with open('5.csv', 'r') as csvfile:
		spamreader = csv.reader(csvfile)
		for row in spamreader:
			x.append(float(row[0]))
			y.append(float(row[1]))


	max_y = max(y)
	return max_y