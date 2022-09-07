import numpy as np

path_03_sept_2022 = "mediciones/03_sept_2022/clustering"

data_clustering_exponencial =  "Q_1500_Nmax_10_exponencial_alpha_0.5_ensembleSize_100_gamma_0.1_clustering.txt"
data_clustering_constante =  "Q_1500_Nmax_10_constante_alpha_0.5_ensembleSize_100_gamma_0.1_clustering.txt"
data_clustering_Kronecker =  "Q_1500_Nmax_10_Kronecker_alpha_0.5_ensembleSize_100_gamma_0.1_clustering.txt"


clustering_medio_exponencial = data_clustering_exponencial[:, 0]
clustering_global_exponencial = data_clustering_exponencial[:, 1]

clustering_medio_constante = data_clustering_constante[:, 0]
clustering_global_constante = data_clustering_constante[:, 1]

clustering_medio_Kronecker = data_clustering_Kronecker[:, 0]
clustering_global_Kronecker = data_clustering_Kronecker[:, 1]






