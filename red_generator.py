from copy import copy
from unicodedata import name
from unittest import skip
import numpy as np
from matplotlib import pyplot as plt
import networkx as nx
import time
import math

class Red():
    '''
        Attributes : -> Q = total number of cliques (int)
                    -> n_max = maximum size a cliue can have (int)
                    -> gamma = probability of a node having an edge to connecting to other clique (float)
                    -> fn = probability distribution for a clique being of size n (function)
                    -> clique_list = clique list (list[nx.Graph])
                    -> red_total = full network (nx.Graph)
    '''

    def __init__(self, Q, Gamma , fn, n_max):
        # Asigno valores y creo la lista de cliques:
        self.Q = Q  # cantidad total de cliques
        self.gamma = Gamma # probabilidad de que un nodo tenga enlace a otro clique
        self.n_max = n_max # maximo tamaño de clique
        self.fn = fn  # distribucion de probabilidad para el tamaño de clique
        self.clique_list = [] # lista con los cliques de la red 
        
        # Creo una lista de nombres de la forma "clique " + str(i) + " nodo " :
        name_list = []

        # Genero una seed aleatoria :
        np.random.seed()

        # Creo un array de los posibles valores de tamaño de clique :
        n_vals = np.arange(1, n_max + 1)
        f_n_vals = fn(n_vals)
        f_n_vals = f_n_vals / np.sum(f_n_vals) # lo puedo hacer para todas las redes directo

        for i in range(Q):
            name_list.append("clique " + str(i) + " nodo ")
            
            n = np.random.choice(n_vals, p = f_n_vals) # Revisar distribucion de probabilidad
            
            aux_clique = nx.complete_graph(n) # genero el clique
            self.clique_list.append(aux_clique)

        self.red_total_cliques_desconectados = nx.union_all(self.clique_list, rename = name_list) # red_total es un grafo de la red completa
        
        # Renombro los nodos para que sean pares (clique, nodo) :
        aux_names = {}
        estado_conexion_ext = {}
        for node in self.red_total_cliques_desconectados.nodes():
            par_clique_nodo = tuple([int(s) for s in node.split() if s.isdigit()])
            aux_names[node] = par_clique_nodo
            estado_conexion_ext[node] = {"ext_connection" : False}

        nx.set_node_attributes(self.red_total_cliques_desconectados, estado_conexion_ext)
        self.red_total_cliques_desconectados = nx.relabel_nodes(self.red_total_cliques_desconectados, aux_names)
        
        
        self.red_total_cliques_conectados = self.red_total_cliques_desconectados.copy()

                
        # # Asigno los enlaces entre cliques :
        
        aux_node_list = []        
        for nodo in self.red_total_cliques_conectados.nodes():
            nro_random = np.random.choice([0,1], p = [1 - self.gamma, self.gamma])        
            if nro_random:
                aux_node_list.append(nodo)
            
        # PRIMER ALGORITMO COREGIDO:

        np.random.shuffle(aux_node_list)

        while len(aux_node_list) > 1:
            G = self.red_total_cliques_conectados.subgraph(aux_node_list) # revisar si vale la pena esta linea
            if nx.number_connected_components(G) == 1:
                break
    
            nodo0 = aux_node_list[0]
            nodo1 = aux_node_list[1]

            while self.red_total_cliques_conectados.has_edge(nodo0, nodo1):
                np.random.shuffle(aux_node_list)
                nodo0 = aux_node_list[0]
                nodo1 = aux_node_list[1]         

            self.red_total_cliques_conectados.add_edge(nodo0, nodo1)
            aux_node_list.remove(nodo0)
            aux_node_list.remove(nodo1)
            self.red_total_cliques_conectados.nodes()[nodo0]["ext_connection"] = True
            self.red_total_cliques_conectados.nodes()[nodo1]["ext_connection"] = True






    def plot_conectado(self):
        nx.draw(self.red_total_cliques_conectados)
    
    def plot_desconectado(self):
        nx.draw(self.red_total_cliques_desconectados)

    def degree(self, node):
        return self.red_total_cliques_conectados.degree[node]

    def local_clustering(self, nodo):
        return nx.clustering(self.red_total_cliques_conectados, nodo)

    def mean_clustering(self):
        return nx.average_clustering(self.red_total_cliques_conectados)

    def global_clustering(self):
        return nx.transitivity(self.red_total_cliques_conectados)

    def nodes(self):
        return self.red_total_cliques_conectados.nodes()

    def edges(self):
        return self.red_total_cliques_conectados.edges()

    def gamma_efectivo(self):
        num_nodos_con_enlace_externo = sum(2 for edge in self.edges() if edge[0][0] != edge[1][0])
        return num_nodos_con_enlace_externo / len(self.nodes())



if __name__ == "__main__":

    Q = 10000
    n_max = 10
    gamma = 0.1

    def f_n_exponencial(n):
        return np.exp( -0.5 * n)

    start_time = time.time()
    red_test = Red(Q , gamma, f_n_exponencial , n_max)
    print("--- %s seconds ---" % (time.time() - start_time))    

    print("gamma efectivo : " , red_test.gamma_efectivo())


    # red_test.plot_conectado()
    # plt.show()

    print("---main end---")