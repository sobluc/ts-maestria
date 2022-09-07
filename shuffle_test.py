import numpy as np
from matplotlib import pyplot as plt
import time

times = []
ns = []

N1 = 10000000000
N2 = 10000000000000
for n in range(N1, N2):
    v = np.linspace(0, 10, n)
    t0 = time.time()
    np.random.shuffle(v)
    t = time.time() - t0
    

    times.append(t)
    ns.append(n)


plt.plot(ns, times, 'ko')
plt.ylabel("tiempo [s]")
plt.ylabel("N")
plt.show()

