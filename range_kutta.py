import sys
import math
import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    return math.pow(math.e, t - y)

def true_sol(t):
    return np.log(np.exp(t) + math.e - 1)
    
def range_kutta(a, b, N, alpha):
    h = (b - a) / N
    t = a
    w = alpha
    new_point = [t, w]
    li = []
    li.append(new_point)
    print ("t: " + str(t) + " w: " + str(w))

    for i in range (1, N + 1):
        k1 = h * f(t, w)
        k2 = h * f(t + (h / 2), w + (k1 / 2))
        k3 = h * f(t + (h / 2), w + (k2 / 2))
        k4 = h * f(t + h, w + k3)

        w = w + (k1 + 2 * k2 + 2* k3 + k4) / 6
        t = a + i * h
        
        new_point = [t, w]
        li.append(new_point)
        print ("t: " + str(t) + " w: " + str(w))

    plt.grid(True)

    domain = np.array(np.linspace(0, 1, num=100))
    plt.plot(domain, true_sol(domain), "b-")

    tw = [(t, w) for t, w in li]
    plt.plot([x[0] for x in tw], [x[1] for x in tw], "ro--")

    plt.show()

def main(argv):    
    range_kutta(float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]))

if __name__ == "__main__":
    main(sys.argv[1:])
