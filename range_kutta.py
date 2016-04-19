import sys
import math
import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    return math.pow(math.e, t - y)
    
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

    # evenly sampled time at 200ms intervals
    t = np.arange(0., 5., 0.2)

    # red dashes, blue squares
    plt.plot(t, math.pow(math.e, t - y), 'r--', t, math.log(math.pow(math.e, t) + math.e - 1), 'bs')
    plt.show()

def main(argv):    
    range_kutta(float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]))

if __name__ == "__main__":
    main(sys.argv[1:])
