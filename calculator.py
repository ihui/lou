#!/usr/bin/env python3
import sys
d = sys.argv[1]
try:
    Sa = int(d)
except ValueError:
    print("Parameter Error")
if Sa < 3500:
    tax = 0
else:
    dS = Sa - 3500
    if dS <= 1500:
        tax = dS * 0.03
    elif (dS > 1500 and dS <= 4500):
        tax = dS * 0.1 - 105
    elif (dS > 4500 and dS <= 9000):
        tax = dS * 0.2 - 555
    elif (dS > 9000 and dS <= 35000):
        tax = dS * 0.25 - 1005
    elif (dS > 35000 and dS <= 55000):
        tax = dS * 0.3 - 2755
    elif (dS > 5500 and dS <= 80000):
        tax = dS * 0.35 - 5505
    else:
        tax = dS * 0.45 - 13505
print("{:.2f}".format(tax))
    
