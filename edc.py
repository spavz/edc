import numpy as np
from scipy.optimize import curve_fit

def temp_fit(x, a, b, c):
	return c-(a*(x-b)**2) 

def uv_fit(x, a, b):
	return a*x + b
print("Enter nominal dye concentration at STP")
_M = int(input())

print("Enter nominal temperature (Celcius)")
Tc = int(input())

x = []
y = []
print("Enter five values of temp v/s rate of dye degrad. (space-separated)")
for _ in range(4):
	a, b = map(float,input().split())
	x.append(a)
	y.append(b)

popt, pcov = curve_fit(temp_fit, x, y)
a1,b1,c1=popt

print("Enter five values of UV v/s rate of dye degrad. (space-separated)")
for _ in range(4):
	a, b = map(float,input().split())
	x.append(a)
	y.append(b)
popt, pcov = curve_fit(uv_fit, x, y)
a2,b2=popt

print('At T = 30 degree Celcius, UV exposure of 1.5 hours, rate = ',temp_fit(5, a1,b1,c1) + uv_fit(1.5,a2,b2) )
print()

