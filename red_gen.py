from unicodedata import name
from unittest import skip
import numpy as np
from matplotlib import pyplot as plt
import networkx as nx


class Red():
    '''
        Atributos : -> Q = numero total de cliques (int)
                    -> n_max = tamaño maximo de un clique (int)
                    -> gamma = probabilidad de que un nodo se conecte a otro clique (float)
                    -> fn = funcion de distribucion de probabilidad de que un clique tenga tamaño n (function)
                    -> clique_list = lista de cliques en la red (list[nx.Graph])
                    -> red_total = toda la red (nx.Graph)
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
        f_n_vals = f_n_vals / np.sum(f_n_vals)

        for i in range(Q):
            name_list.append("clique " + str(i) + " nodo ")
            
            n = np.random.choice(n_vals, p = f_n_vals) # Revisar distribucion de probabilidad
            
            aux_clique = nx.complete_graph(n) # genero el clique
            self.clique_list.append(aux_clique)

        self.red_total = nx.union_all(self.clique_list, rename = name_list) # red_total es un grafo de la red completa
        
        # Renombro los nodos para que sean pares (clique, nodo) :
        aux_names = {}
        for node in self.red_total.nodes():
            par_clique_nodo = tuple([int(s) for s in node.split() if s.isdigit()])
            aux_names[node] = par_clique_nodo

        self.red_total = nx.relabel_nodes(self.red_total, aux_names)

        # Asigno los enlaces entre cliques :
        #num_enlaces_ext = int(self.gamma * len(self.red_total.nodes())) # calculo cuántos enlaces necesito aproximadamente (si no anda lo hago asi)
        
        aux_node_list = []
        for nodo in self.red_total.nodes():
            nro_random = np.random.choice([0,1], p = [1 - self.gamma, self.gamma])        
            if nro_random:
                aux_node_list.append(nodo)
            
        try:
            assert len(aux_node_list) > 0
        except:
            print("La lista auxiliar esta vacia")

        while len(aux_node_list) > 1:
            G = self.red_total.subgraph(aux_node_list)
            if nx.number_connected_components(G) == 1:
                break

            random_i = np.random.randint(0, len(aux_node_list))
            random_j = np.random.randint(0, len(aux_node_list))
            while random_j == random_i:
                random_j = np.random.randint(0, len(aux_node_list))

            nodoi = aux_node_list[random_i]
            nodoj = aux_node_list[random_j]               
            if not self.red_total.has_edge(nodoi, nodoj):
                self.red_total.add_edge(nodoi, nodoj)
                aux_node_list.remove(nodoi)
                aux_node_list.remove(nodoj)


    def plot(self):
        nx.draw(self.red_total)

    def degree(self, node):
        return self.red_total.degree[node]

    def local_clustering(self, nodo):
        return nx.clustering(self.red_total, nodo)

    def mean_clustering(self):
        return nx.average_clustering(self.red_total)

    def global_clustering(self):
        return nx.transitivity(self.red_total)
        


if __name__ == "__main__":
    Q = 10
    gamma = 0.8
    n_max = 10

    def fn(n):
        return  np.exp(-n)

    primer_red = Red(Q, gamma, fn, n_max)

    primer_red.plot()
    plt.show()

    A = nx.adjacency_matrix(primer_red.red_total)
    B = nx.to_numpy_array(primer_red.red_total)
    print(A)
    print(B)

 