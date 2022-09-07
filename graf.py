from matplotlib import pyplot as plt
import numpy as np
import time
from red_generator import Red

plt.rcParams.update({'font.size': 18})


data = np.loadtxt("test_algoritmo/tiempo_medio_creacion_vs_Q_fn_exp_algoritmo_1_ensemble_10_nmax_10_rango_10_10000.txt", skiprows = 1)
data2 = np.loadtxt("test_algoritmo/tiempo_medio_creacion_vs_Q_fn_exp_algoritmo_2_ensemble_10_nmax_10_rango_10_10000.txt", skiprows = 1) 

Q0 = data[:,0]
time0 = data[:,1]

Q2 = data[:,0]
time2 = data2[:,1]


gamma = 0.8
n_max = 10
ensemble_size = 10

def test_exponential_f_n(n):
    return np.exp(- n)

Q = [10,25,50,75,100,250,500,750,1000,1250,1500,1750,2000,2500,3000,3500,4000,5000,7000,10000]
time3 = []
for q in Q:
    print(q)
    
    gammas_for_mean_1 = []
    time_for_mean = []
    for i in range(ensemble_size):
        
        start_time = time.time()            
        red_algoritmo1 = Red(q, gamma, test_exponential_f_n, n_max) 
        time_for_mean.append(time.time() - start_time)

        gammas_for_mean_1.append(red_algoritmo1.gamma_efectivo())

    time3.append(np.mean(time_for_mean))






plt.figure()
plt.plot(Q, time0, 'k.' ,label = "Algoritmo 1")
plt.plot(Q2, time2, 'r.' ,label = "Algoritmo 2")
plt.plot(Q, time3, 'b.', label = "Algoritmo 3")

plt.xlabel("Q")
plt.ylabel("t [s]")


plt.legend(loc = 'best')
plt.xscale('log')
plt.yscale('log')
plt.show()