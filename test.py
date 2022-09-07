from red_generator import Red
import numpy as np
from matplotlib import pyplot as plt
from scipy.sparse import csr_matrix
import networkx as nx
import pandas as pd

import time
plt.rcParams.update({'font.size': 18})

def test_exponential_f_n(n):
    return np.exp(- 0.5 * n)


if __name__ == "__main__":
    Q =  np.array([10, 25, 50, 75, 100 ,250, 500 ,750, 1000, 1250, 1500, 1750, 2000, 2500, 3000, 3500, 4000, 5000])
    gamma = [0.1, 0.2, 0.3, 0.4 , 0.5, 0.6, 0.7, 0.8, 0.9]
    n_max = 10
    ensemble_size = 100

    for g in gamma:
        print("g : " , g)

        gamma_eff = []
        tiempos_Q = []
        for q in Q:
            print(q)
            
            gammas_for_mean_1 = []
            time_for_mean = []
            for i in range(ensemble_size):
                
                start_time = time.time()            
                red_algoritmo1 = Red(q, g, test_exponential_f_n, n_max) 
                time_for_mean.append(time.time() - start_time)

                gammas_for_mean_1.append(red_algoritmo1.gamma_efectivo())

            tiempos_Q.append(np.mean(time_for_mean))
            gamma_eff.append(np.mean(gammas_for_mean_1))

        df = pd.DataFrame({"Q" : Q, "mean_time" : tiempos_Q})
        df.to_csv("tiempo_medio_creacion_vs_Q_fn_exp_algoritmo_3_ensemble_" + str(ensemble_size) + "_nmax_" + str(n_max) + "_rango_10_10000_gamma_" + str(g) + ".txt", index=False, sep = '\t')

        df = pd.DataFrame({"Q" : Q, "gamma_eff" : gamma_eff})
        df.to_csv("gamma_eff_vs_Q_fn_exp_algoritmo_3_ensemble_" + str(ensemble_size) + "_nmax_" + str(n_max) + "_rango_10_10000_gamma_" + str(g) + ".txt", index=False, sep = '\t')

        plt.figure()
        plt.plot(Q, tiempos_Q, 'k.' ,label = "Algoritmo 1")
        
        plt.xlabel("Q")
        plt.ylabel("t [s]")

        plt.figure()
        plt.plot(Q, gamma_eff, 'k.' ,label = "Algoritmo 1")
        plt.plot(Q, g  + Q - Q , label = "$\gamma$ = " + str(g))
        
        plt.xlabel("Q")
        plt.ylabel("$\gamma$ efectivo")
        plt.legend(loc = 'best')
        #plt.xscale('log')
    plt.show()


    print("---main end---")






