## Distribuciones
# Exponencial
from scipy.stats import expon
import pandas as pd

lam = 0.5 # lamda = 1/mean  

probabilidades = [0.15, 0.5, 0.75]

cuantiles = expon.ppf(probabilidades, scale=1/lam)
dfprobpointfunc = pd.DataFrame({'Probabilidad':probabilidades, 'Cuantiles':cuantiles})
print(dfprobpointfunc)

# Normal
from scipy.stats import norm

cuantiles_norm = norm.ppf(probabilidades, scale=1/lam)
norm_dfprobpointfunc = pd.DataFrame({'Probabilidad':probabilidades, 'Cuantiles_norm':cuantiles_norm})
print(norm_dfprobpointfunc)


#print(expon.stats(0.2, scale = 1/lam))






