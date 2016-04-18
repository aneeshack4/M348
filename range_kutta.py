import sys
import math
import numpy as np

def f(t, w):
    y(t) = 
    
def range_kutta(a, b, N, alpha):
    h = (b - a) / N
    t = alpha
    w = alpha
    print ("t: " + str(t) + " w: " + str(w))

    for i in range (1, N + 1):
        k1 = h * f(t, w)
        k2 = h * f(t + (h / 2), w + (k1 / 2))
        k3 = h * f(t + (h / 2), w + (k2 / 2))
        k4 = h * f(t + h, w + k3)

        w = w + (k1 + 2 * k2 + 2* k3 + k4) / 6
        t = a + i * h

        print ("t: " + str(t) + " w: " + str(w))

def main(argv):    
    range_kutta(float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]))

if __name__ == "__main__":
    main(sys.argv[1:])