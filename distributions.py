import numpy as np

def fn_exponencial(alpha):
    def exp_return(n):
        return np.exp(- alpha * n)

    return exp_return

def fn_constante(cte):

    def cte_return(n):
        return  cte + n - n   
    
    return cte_return

def fn_Kronecker(m):

    def Kronecker_return(n):
            if isinstance(n, np.ndarray):
                ret_array = np.zeros(len(n))
                ret_array[m - 1] = 1
                return ret_array
            else:
                if n == m:
                    return 1 
                else:
                    return 0 
    
    return Kronecker_return



