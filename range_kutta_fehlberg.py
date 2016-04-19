import sys
import math
import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    return math.pow(math.e, t - y)
    
def range_kutta_fehlberg(a, b, alpha, tol, hmax, hmin):
    t = alpha
    w = alpha
    h = hmax
    flag = 1
    print ("t: " + str(t) + " w: " + str(w))

    while (flag == 1):
        k1 = h * f(t, w)
        k2 = h * f(t + (1 / 4) * h, w + (1 / 4) * k1)
        k3 = h * f(t + (3 / 8) * h, w + (3 / 32) * k1 + (9 / 32) * k2)
        k4 = h * f(t + (12 / 13) * h, w + (1932 / 2197) * k1 - (7200 / 2197) * k2 + (7296 / 2197) * k3)
        k5 = h * f(t + h, w + (439 / 216) * k1 - 8 * k2 + (3680 / 513) * k3 - (845 / 4104) * k4)
        k6 = h * f(t + (1 / 2) * h, w - (8 / 27) * k1 + 2 * k2 - (3544 / 2565) * k3 + (1859 / 4104) * k4 - (11 / 40) * k5)

        r = (1 / h) * math.abs((1/360)*k1 - (128/4275)*k3 - (2197/75240)*k4 + (1/50)*k5 + (2/55)*k6)

        if (r < tol or r == tol):
            t = t + h
            w = w + (25/216)*k1 + (1408/2565)*k3 + (2197/4104)*k4 - (1/5)*k5
            print ("t: " + str(t) + " w: " + str(w) + " h: " + str(h))

        psi = 0.84 * math.pow(tol/r, .25)

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

    # # evenly sampled time at 200ms intervals
    # t = np.arange(0., 5., 0.2)

    # # red dashes, blue squares
    # plt.plot(t, math.pow(math.e, t - y), 'r--', t, math.log(math.pow(math.e, t) + math.e - 1), 'bs')
    # plt.show()

def main(argv):    
    range_kutta(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6]))

if __name__ == "__main__":
    main(sys.argv[1:])
