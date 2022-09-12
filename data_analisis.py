import numpy as np
from matplotlib import pyplot as plt
from funciones_analiticas import coef_clustering_medio, coef_clustering_global
from distributions import fn_Kronecker, fn_constante, fn_exponencial
from red_generator import Red
import networkx as nx

plt.rcParams.update({'font.size': 18})



Q = 1000
n_max = 10
alpha = 0.5
cte = 1
m0 = 5

ensemble_size = 100


path = "mediciones/12_sept_2022/clustering/"
name_clustering_analitico = "clustering_analitico_"
name_ensemble_exponencial = "Q_"+ str(Q) + "_Nmax_"+ str(n_max) + "_exponencial_alpha_" + str(alpha) + "_ensembleSize_" + str(ensemble_size) + "_gamma_"
name_ensemble_constante = "Q_"+ str(Q) + "_Nmax_"+ str(n_max) + "_constante_cte_" + str(cte) + "_ensembleSize_" + str(ensemble_size) + "_gamma_"
name_ensemble_Kronecker = "Q_"+ str(Q) + "_Nmax_"+ str(n_max) + "_Kronecker_m0_" + str(m0) + "_ensembleSize_" + str(ensemble_size) + "_gamma_"


####################################################################################################################################################################
########################################################    exponencial   ########################################################################################## 
####################################################################################################################################################################

data_analitico_exponencial = np.loadtxt(path + name_clustering_analitico + "exponencial.txt", skiprows = 1)

gammas_exponencial = data_analitico_exponencial[:,0]
medio_analiticos_exponencial = {} 
global_analiticos_exponencial = {} 
for i in range(len(gammas_exponencial)):
    medio_analiticos_exponencial[gammas_exponencial[i]] = data_analitico_exponencial[:,1][i]
    global_analiticos_exponencial[gammas_exponencial[i]] = data_analitico_exponencial[:,2][i]

medio_ensemble_exponencial = {}
global_ensemble_exponencial = {}
for g in gammas_exponencial:       
    ifile = path + name_ensemble_exponencial + str(g) + "_clustering.txt"
    data_ensemble = np.loadtxt(ifile, skiprows = 1)

    medio_ensemble_exponencial[g] = data_ensemble[:,0]
    global_ensemble_exponencial[g] = data_ensemble[:,1]


errores_medio_exponencial = [np.std(medio_ensemble_exponencial[g]) for g in gammas_exponencial]
medias_medio_exponencial = [np.mean(medio_ensemble_exponencial[g]) for g in gammas_exponencial]

errores_global_exponencial = [np.std(global_ensemble_exponencial[g]) for g in gammas_exponencial]
medias_global_exponencial = [np.mean(global_ensemble_exponencial[g]) for g in gammas_exponencial]

plt.figure("exponencial")

plt.errorbar(gammas_exponencial, medias_medio_exponencial, yerr = errores_medio_exponencial, fmt = '.', color = "blue" ,
                elinewidth = 0.3, capsize = 3, label = "Clustering medio simulado")
plt.plot(gammas_exponencial, [medio_analiticos_exponencial[g] for g in gammas_exponencial], '-', color = "blue" , label = "Clustering medio analitico")


plt.errorbar(gammas_exponencial, medias_global_exponencial, yerr = errores_global_exponencial, fmt = '.', color = "green" ,
                elinewidth = 0.3, capsize = 3, label = "Clustering global simulado")
plt.plot(gammas_exponencial, [global_analiticos_exponencial[g] for g in gammas_exponencial], '-', color = "green" , label = "Clustering global analitico")

plt.title("exponencial $alpha = $" + str(alpha))
plt.xlabel("$\gamma$")
plt.ylabel("Clustering")
plt.legend(loc = 'best')

####################################################################################################################################################################
########################################################    constante   ############################################################################################ 
####################################################################################################################################################################

data_analitico_constante = np.loadtxt(path + name_clustering_analitico + "constante.txt", skiprows = 1)

gammas_constante = data_analitico_constante[:,0]
medio_analiticos_constante = {} 
global_analiticos_constante = {} 
for i in range(len(gammas_constante)):
    medio_analiticos_constante[gammas_constante[i]] = data_analitico_constante[:,1][i]
    global_analiticos_constante[gammas_constante[i]] = data_analitico_constante[:,2][i]

medio_ensemble_constante = {}
global_ensemble_constante = {}
for g in gammas_constante:       
    ifile = path + name_ensemble_constante + str(g) + "_clustering.txt"
    data_ensemble = np.loadtxt(ifile, skiprows = 1)

    medio_ensemble_constante[g] = data_ensemble[:,0]
    global_ensemble_constante[g] = data_ensemble[:,1]

errores_medio_constante = [np.std(medio_ensemble_constante[g]) for g in gammas_constante]
medias_medio_constante = [np.mean(medio_ensemble_constante[g]) for g in gammas_constante]

errores_global_constante = [np.std(global_ensemble_constante[g]) for g in gammas_constante]
medias_global_constante = [np.mean(global_ensemble_constante[g]) for g in gammas_constante]

plt.figure("Constante")

plt.errorbar(gammas_constante, medias_medio_constante, yerr = errores_medio_constante, fmt = '.', color = "blue" ,
                elinewidth = 0.3, capsize = 3, label = "Clustering medio simulado")
plt.plot(gammas_constante, [medio_analiticos_constante[g] for g in gammas_constante], '-', color = "blue" , label = "Clustering medio analitico")


plt.errorbar(gammas_constante, medias_global_constante, yerr = errores_global_constante, fmt = '.', color = "green" ,
                elinewidth = 0.3, capsize = 3, label = "Clustering global simulado")
plt.plot(gammas_constante, [global_analiticos_constante[g] for g in gammas_constante], '-', color = "green" , label = "Clustering global analitico")

plt.title("constante c = " + str(cte))
plt.xlabel("$\gamma$")
plt.ylabel("Clustering")
plt.legend(loc = 'best')

####################################################################################################################################################################
########################################################    Kronecker   ############################################################################################ 
####################################################################################################################################################################

data_analitico_Kronecker = np.loadtxt(path + name_clustering_analitico + "Kronecker.txt", skiprows = 1)

gammas_Kronecker = data_analitico_Kronecker[:,0]
medio_analiticos_Kronecker = {} 
global_analiticos_Kronecker = {} 
for i in range(len(gammas_Kronecker)):
    medio_analiticos_Kronecker[gammas_Kronecker[i]] = data_analitico_Kronecker[:,1][i]
    global_analiticos_Kronecker[gammas_Kronecker[i]] = data_analitico_Kronecker[:,2][i]

medio_ensemble_Kronecker = {}
global_ensemble_Kronecker = {}
for g in gammas_Kronecker:       
    ifile = path + name_ensemble_Kronecker + str(g) + "_clustering.txt"
    data_ensemble = np.loadtxt(ifile, skiprows = 1)

    medio_ensemble_Kronecker[g] = data_ensemble[:,0]
    global_ensemble_Kronecker[g] = data_ensemble[:,1]


# Correccion del valor analitico (estaba mal la funcion distribucion para los vectores):
# [solo para las mediciones del 3 de septiembre 2022 que igualmente salieron mal]
# fn_Kro = fn_Kronecker(6)
# n_max = 10
# for g in gammas_Kronecker:
#     medio_analiticos_Kronecker[g] = coef_clustering_medio(fn_Kro, g, n_max)
#     global_analiticos_Kronecker[g] = coef_clustering_global(fn_Kro, g, n_max)


errores_medio_Kronecker = [np.std(medio_ensemble_Kronecker[g]) for g in gammas_Kronecker]
medias_medio_Kronecker = [np.mean(medio_ensemble_Kronecker[g]) for g in gammas_Kronecker]

errores_global_Kronecker = [np.std(global_ensemble_Kronecker[g]) for g in gammas_Kronecker]
medias_global_Kronecker = [np.mean(global_ensemble_Kronecker[g]) for g in gammas_Kronecker]

plt.figure("Kronecker")

plt.errorbar(gammas_Kronecker, medias_medio_Kronecker, yerr = errores_medio_Kronecker, fmt = '.', color = "blue" ,
                elinewidth = 0.3, capsize = 3, label = "Clustering medio simulado")
plt.plot(gammas_Kronecker, [medio_analiticos_Kronecker[g] for g in gammas_Kronecker], '-', color = "blue" , label = "Clustering medio analitico")


plt.errorbar(gammas_Kronecker, medias_global_Kronecker, yerr = errores_global_Kronecker, fmt = '.', color = "green" ,
                elinewidth = 0.3, capsize = 3, label = "Clustering global simulado")
plt.plot(gammas_Kronecker, [global_analiticos_Kronecker[g] for g in gammas_Kronecker], '-', color = "green" , label = "Clustering global analitico")

plt.title("Kronecker m = " + str(m0))
plt.xlabel("$\gamma$")
plt.ylabel("Clustering")
plt.legend(loc = 'best')
plt.show()

