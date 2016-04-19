import sys
import math
import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    return math.pow(math.e, t - y)
    
def range_kutta_fehlberg(a, b, alpha, tol, hmax, hmin):
    t = a
    w = alpha
    h = hmax
    flag = 1
    print ("t: " + str(t) + " w: " + str(w))

    while (flag == 1):
        k1 = h * f(t, w)
        k2 = h * f(t + (1.0 / 4.0) * h, w + (1.0 / 4.0) * k1)
        k3 = h * f(t + (3.0 / 8.0) * h, w + (3.0 / 32.0) * k1 + (9.0 / 32.0) * k2)
        k4 = h * f(t + (12.0 / 13.0) * h, w + (1932.0 / 2197.0) * k1 - (7200.0 / 2197.0) * k2 + (7296.0 / 2197.0) * k3)
        k5 = h * f(t + h, w + (439.0 / 216.0) * k1 - 8 * k2 + (3680.0 / 513.0) * k3 - (845.0 / 4104.0) * k4)
        k6 = h * f(t + (1.0 / 2.0) * h, w - (8.0 / 27.0) * k1 + 2 * k2 - (3544.0 / 2565.0) * k3 + (1859.0 / 4104.0) * k4 - (11.0 / 40.0) * k5)

        r = (1 / h) * math.fabs((1.0/360.0)*k1 - (128.0/4275.0)*k3 - (2197.0/75240.0)*k4 + (1.0/50.0)*k5 + (2.0/55.0)*k6)

        if (r < tol or r == tol):
            t = t + h
            w = w + (25.0/216.0)*k1 + (1408.0/2565.0)*k3 + (2197.0/4104.0)*k4 - (1.0/5.0)*k5
            print ("t: " + str(t) + " w: " + str(w) + " h: " + str(h))

        psi = 0.84 * math.pow((float(tol))/(float(r)), .25)

        if (psi < 0.1 or psi == 0.1):
            h = 0.1 * h
        elif (psi > 4 or psi == 4):
            h = 4 * h
        else:
            h = psi * h

        if (h > hmax):
            h = hmax

        if (t > b or t == b):
            flag = 0
        elif (t + h > b):
            h = b - t
        elif (h < hmin):
            flag = 0
            print ("minimum h exceeded") #procedure completed unsuccessfully

def main(argv):    
    range_kutta_fehlberg(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6]))

if __name__ == "__main__":
    main(sys.argv[1:])
