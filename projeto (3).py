import numpy as np
import pandas as pd

path = "C:/Users/berna/OneDrive/Ambiente de Trabalho/projetoNova/bb21a10summarytables.xlsx"

df = pd.read_excel(path, sheet_name=22, usecols="C:L", header=None, skiprows=52, nrows=10)
z = np.array(df, dtype=float)# £ million

dfx = pd.read_excel(path, sheet_name=22, usecols="C:L", header=None, skiprows=75, nrows=1)
x = np.array(dfx, dtype=float)[0] # £ million

#Alinea a)
def coef_mat(z,x):
    return z/x

#Alinea b)
def leon(a, dif = 1e-6):
    matrix_identity = np.identity(a.shape[0])
    diff_mat = 0
    expo = 1
    collector = matrix_identity
    while(True):
        atual_matrix = np.linalg.matrix_power(a, expo)
        new_matrix = np.linalg.matrix_power(a, expo + 1)
        diff_mat = abs(new_matrix - atual_matrix)
        collector = abs(atual_matrix + collector)
        expo = expo + 1
        for x in diff_mat:
            for y in x:
                if (y < dif):
                    return collector

def impact_output(a):
    return np.sum(leon(a), 0)

def maximp(a):
    return  "Sector " + str(np.argmax(impact_output(a)) + 1)

a=coef_mat(np.array([[3, 2],[1, 4]]),np.array([10, 10]))
E = np.array([1, 5])

#Alinea c)

def impact_ghg(a, ghg):
    res = []
    leon_matrix = leon(a)
    for s in range(len(leon_matrix)):
        acc = 0
        for l in range(len(leon_matrix)):
            acc += leon_matrix[l][s] / 1000 * ghg[l]
        res = res + [acc]
    return res


#Alinea d)

def wellbeing(a, ghg, p = 50):
    res = []
    list_ighg  = impact_ghg(a, ghg)
    for l in list_ighg:
        res.append(l*p)
    return impact_output(a) - res

def maxwell(a, ghg, p = 50):
    arg_max = str(np.argmax(wellbeing(a, ghg, p)) + 1)
    return "Sector" + " " + arg_max


def price_range(a, ghg):
    res = []
    for p in range(201) :
        if maxwell(a, ghg, p) == maxwell(a, ghg):
            res.append(p)
    return [res[0] , res[-1]]               


        
        
        
        
        
        
        
        
        
        
        
    
    
    
    