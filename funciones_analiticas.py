# -----------------------------------------------------------------------------------------

# Archivo con funciones que calculan las expresiones analíticas para las redes.
#
# fn es la distribución de probabilidad para el tamaño de cliques (debe estar truncada y f0 = 0).
# Q es la cantidad de cliques en el sistema.
# gamma es la probabilidad de que un nodo tenga un enlace a un nodo en otro clique.

# -----------------------------------------------------------------------------------------

def suma_n_de_nfn(fn):
    sum = 0
    n = 1
    while fn(n) != 0:
        sum += n * fn(n)
        n += 1
    return sum

def cantidad_de_nodos(fn, Q):
    sum = 0
    n = 1
    while fn(n) != 0:
        sum += n * fn(n)
        n += 1
    return sum * Q   

def distribucion_de_grado(g, fn, gamma):
    A = gamma * g * fn(g) / suma_n_de_nfn(fn)
    B = (1-gamma) * (g + 1) * fn(g + 1) / suma_n_de_nfn(fn)
    return A + B

def coef_clustering_local(red, nodo):
    clique = red.clique_list[nodo[0]]
    clique_size = len(clique.nodes())    
    if red.nodes()[nodo]["ext_connection"]:
        return (clique_size - 2) / clique_size
    else:
        return 1.0

def coef_clustering_medio(fn, gamma):
    sum = 0
    n = 1
    while fn(n) != 0:
        sum += (n - 2 * gamma) * fn(n)
        n += 1
         
    return sum / suma_n_de_nfn(fn)


def coef_clustering_global(fn, gamma):
    sum1 = 0
    n = 1
    while fn != 0:
        sum1 += n * (n-1) * (n-2) * fn(n)
        n += 1

    sum2 = 0
    n = 1
    while fn != 0:
        sum2 += n * (n-1) * fn(n)
        n += 1

    return 0.5 * sum1 /(0.5 * sum1 + gamma * sum2)
