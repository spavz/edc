import numpy as np
from scipy.optimize import curve_fit
import scipy
import csv
from p5 import *
from p3 import *
from p4 import *
from p1 import *
from p2 import *

print("Reading data from the CSV files generated on analysing graph pattern...")
a=do1()
print("Optimum value of concentration is: "+str(a))
b=do2()
print("Optimum value of mixingspeed is: "+str(b))
c = do3()
print(str(c))











