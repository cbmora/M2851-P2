import pandas as pd
from matplotlib import  pyplot as plt

df= pd.read_csv('winequality-red.csv',sep=';') #leemos los datos en un dataframe
#
df_corr=df.corr()
df_corr.to_csv('MatrizCorrelacion.csv')

df2=df.copy()
# Graficos Correlacion
for col in df:
    df2.pop(col)
    for col2 in df2:   
        plt.title(col + ' vs. '+ col2)
        plt.scatter(df[col], df[col2])
        plt.xlabel(col)
        plt.ylabel(col2)
        #plt.show()
        plt.savefig('..\Fig\Corr\\' + col+'-vs-'+col2+'.png')
        plt.close()
        
