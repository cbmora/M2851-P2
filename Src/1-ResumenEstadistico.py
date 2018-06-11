import pandas as pd

df= pd.read_csv('winequality-red.csv',sep=';') #leemos los datos en un dataframe
# Calculamos resumen estadistico
df.describe().to_csv('ResumenEstadistico.csv')
