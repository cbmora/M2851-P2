import pandas as pd
#import statmodels.formula.api as smf
import statsmodels.api as sm
from matplotlib import  pyplot as plt 

df= pd.read_csv('winequality-red.csv',sep=';') #leemos los datos en un dataframe
y=df['quality'] 
x=df.drop( ["fixed acidity", "free sulfur dioxide", "quality"], axis='columns') # eliminamos atributos  redundantes
#x=df.drop( ["quality"], axis='columns') #  sin eliminar atributos  redundantes
#Eliminamos tambien "residual sugar"y "total sulfur dioxide":
#x=df.drop( ["residual sugar","fixed acidity", "total sulfur dioxide","free sulfur dioxide", "quality"], axis='columns')
#
model = sm.OLS(y, x).fit() 
print(model.params) # mostramos pesos obtenidos para cada variable

print(model.summary())

# q-q plot para verificar graficamente distribucion normal de 
qq = sm.qqplot(model.resid, line = 'r')
#plt.show()
plt.savefig('..\Fig\\' + 'QQplot.png')
plt.close()

#predictions = model.predict(x)

# plot of residuals
stdres = pd.DataFrame(model.resid_pearson)
plt.plot(stdres, 'o', ls = 'None')
l = plt.axhline(y=0, color = 'r')
plt.ylabel('Standardized residual')
plt.xlabel('Numero de muestra')
#plt.show()
plt.savefig('..\Fig\\' + 'Residuals.png')
plt.close()

