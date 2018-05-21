#!/usr/bin/env python3
import sys

for arg in sys.argv[1:]:
    d = arg.split(':')
    try:
        num = int(d[0])
        Sa = int(d[1])
    except ValueError:
        print("Parameter Error")
    dS = Sa * 0.835 - 3500
    if dS < 0:
        tax = 0
    elif dS <= 1500:
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
    AfSa = Sa * 0.835 - tax
    print("{}:{:.2f}".format(num, AfSa))
    
