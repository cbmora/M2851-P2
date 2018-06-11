import pandas as pd
from matplotlib import  pyplot as plt
df= pd.read_csv('winequality-red.csv',sep=';') #leemos los datos en un dataframe


for col in df: 
    plt.hist(df[col],bins=20)
    plt.ylabel('No of times')
    plt.xlabel(col)
    #plt.show()
    plt.savefig('..\Fig\Hist\Hist_'+col+'.png')
    plt.close()
