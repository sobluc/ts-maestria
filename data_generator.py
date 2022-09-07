import pandas as pd
from red_generator import Red
import distributions as mis_distr
import funciones_analiticas as fun_ana


if __name__ == "__main__":

    gammas = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8 , 0.9]
    Q = 1500
    n_max = 10

    alpha = 0.5
    cte = 1
    m0 = 5

    ensemble_size = 100

    fileName_exponencial = "Q_" + str(Q) + "_Nmax_" + str(n_max) + "_exponencial_alpha_" + str(alpha) + "_ensembleSize_" + str(ensemble_size)
    fileName_constante = "Q_" + str(Q)  + "_Nmax_" + str(n_max) + "_constante_cte_" + str(cte) + "_ensembleSize_" + str(ensemble_size)
    fileName_Kronecker = "Q_" + str(Q)  + "_Nmax_" + str(n_max) + "_Kronecker_m0_" + str(m0) + "_ensembleSize_" + str(ensemble_size)


    fun_exponencial = mis_distr.fn_exponencial(alpha)
    fun_constante = mis_distr.fn_constante(cte)
    fun_Kronecker = mis_distr.fn_Kronecker(m0)


    clust_medio_analitico_exponencial_list = []
    clust_medio_analitico_constante_list = []
    clust_medio_analitico_Kronecker_list = []

    clust_global_analitico_exponencial_list = []
    clust_global_analitico_constante_list = []
    clust_global_analitico_Kronecker_list = []

    for g in gammas:
        print("gamma : ", g)

        clust_medio_analitico_exponencial = fun_ana.coef_clustering_medio(fun_exponencial, g, n_max)
        clust_medio_analitico_constante = fun_ana.coef_clustering_medio(fun_constante, g, n_max)
        clust_medio_analitico_Kronecker = fun_ana.coef_clustering_medio(fun_Kronecker, g, n_max)        

        clust_global_analitico_exponencial = fun_ana.coef_clustering_global(fun_exponencial, g, n_max)
        clust_global_analitico_constante = fun_ana.coef_clustering_global(fun_constante, g, n_max)
        clust_global_analitico_Kronecker = fun_ana.coef_clustering_global(fun_Kronecker, g, n_max)

        clust_medio_analitico_exponencial_list.append(clust_medio_analitico_exponencial)
        clust_medio_analitico_constante_list.append(clust_medio_analitico_constante)
        clust_medio_analitico_Kronecker_list.append(clust_medio_analitico_Kronecker)

        clust_global_analitico_exponencial_list.append(clust_global_analitico_exponencial)
        clust_global_analitico_constante_list.append(clust_global_analitico_constante)
        clust_global_analitico_Kronecker_list.append(clust_global_analitico_Kronecker)


        fileName_exponencial_gamma =  fileName_exponencial + "_gamma_" + str(g) 
        fileName_constante_gamma =  fileName_constante + "_gamma_" + str(g)
        fileName_Kronecker_gamma =  fileName_Kronecker + "_gamma_" + str(g)

        exponencial_ensemble_values_clustering_medio = []
        constante_ensemble_values_clustering_medio = []
        Kronecker_ensemble_values_clustering_medio = []

        exponencial_ensemble_values_clustering_global = []
        constante_ensemble_values_clustering_global = []
        Kronecker_ensemble_values_clustering_global = []

        for i in range(ensemble_size):     
            print(i + 1, " de ", ensemble_size)
            
            red_i_exponencial = Red(Q, g , fun_exponencial, n_max)
            red_i_constante = Red(Q, g , fun_constante, n_max)
            red_i_Kronecker = Red(Q, g , fun_Kronecker, n_max)

            # file_i_exponencial = pd.DataFrame({"nodos" : red_i_exponencial.nodes(), "edges" : red_i_exponencial.edges()})
            # file_i_exponencial.to_csv( "mediciones/03_sept_2022/redes/exponencial/red_exponencial_" + str(i) + ".txt", index=False, sep = '\t')

            # file_i_constante = pd.DataFrame({"nodos" : red_i_constante.nodes(), "edges" : red_i_constante.edges()})
            # file_i_constante.to_csv( "mediciones/03_sept_2022/redes/constante/red_constante_" + str(i) + ".txt", index=False, sep = '\t')

            # file_i_Kronecker = pd.DataFrame({"nodos" : red_i_Kronecker.nodes(), "edges" : red_i_Kronecker.edges()})
            # file_i_Kronecker.to_csv( "mediciones/03_sept_2022/redes/kronecker/red_Kronecker_" + str(i) + ".txt", index=False, sep = '\t')


            exponencial_ensemble_values_clustering_medio.append(red_i_exponencial.mean_clustering())
            constante_ensemble_values_clustering_medio.append(red_i_constante.mean_clustering())
            Kronecker_ensemble_values_clustering_medio.append(red_i_Kronecker.mean_clustering())

            exponencial_ensemble_values_clustering_global.append(red_i_exponencial.global_clustering())
            constante_ensemble_values_clustering_global.append(red_i_constante.global_clustering())
            Kronecker_ensemble_values_clustering_global.append(red_i_Kronecker.global_clustering())

        file_ensemble_exponencial = pd.DataFrame({"medio" : exponencial_ensemble_values_clustering_medio , "global" : exponencial_ensemble_values_clustering_global})
        file_ensemble_constante = pd.DataFrame({"medio" : constante_ensemble_values_clustering_medio, "global" : constante_ensemble_values_clustering_global})
        file_ensemble_Kronecker = pd.DataFrame({"medio" : Kronecker_ensemble_values_clustering_medio, "global" : Kronecker_ensemble_values_clustering_global})

        file_ensemble_exponencial.to_csv("mediciones/03_sept_2022/clustering/" + fileName_exponencial_gamma + "_clustering.txt", index = False, sep = '\t')
        file_ensemble_constante.to_csv("mediciones/03_sept_2022/clustering/" + fileName_constante_gamma + "_clustering.txt", index = False, sep = '\t')
        file_ensemble_Kronecker.to_csv("mediciones/03_sept_2022/clustering/" + fileName_Kronecker_gamma + "_clustering.txt", index = False, sep = '\t')

    file_analitico_exponencial = pd.DataFrame({"gamma" : gammas, "medio" : clust_medio_analitico_exponencial_list, "global" : clust_global_analitico_exponencial_list})
    file_analitico_constante = pd.DataFrame({"gamma" : gammas, "medio" : clust_medio_analitico_constante_list, "global" : clust_global_analitico_constante_list})
    file_analitico_Kronecker = pd.DataFrame({"gamma" : gammas, "medio" : clust_medio_analitico_Kronecker_list, "global" : clust_global_analitico_Kronecker_list})

    file_analitico_exponencial.to_csv("mediciones/03_sept_2022/clustering/clustering_analitico_exponencial.txt", index = False, sep = '\t')
    file_analitico_constante.to_csv("mediciones/03_sept_2022/clustering/clustering_analitico_constante.txt", index = False, sep = '\t')
    file_analitico_Kronecker.to_csv("mediciones/03_sept_2022/clustering/clustering_analitico_Kronecker.txt", index = False, sep = '\t')


            



    print("-- main end --")