file = './data.csv'
import pandas as pd

df = pd.read_csv(file)

print('Numero de columnas x filas: ',df.shape)
print('(Cada columna es una variable y cada fila es un registro)')
print('Nombre y tipo de las columnas: ')
print(df.dtypes)    #tipos de datos de cada columna

#Eleji Humedad y distancia
print("Valores únicos de la humedad:")
columna = df["Humidity(%)"]
print(columna.unique()) 
print("Estadisticas de la humedad:")
print("Promedio",columna.mean())      
print("Mediana",columna.median())      
print("Max",columna.max())         
print("Min",columna.min())       
print("Desviación Estándar",columna.std())

#Distancia
print("Valores únicos de la distancia:")
columna = df["Distance(mi)"]
print(columna.unique()) #Todos los valores son unicos, por lo que en teoria no nos sirve
print("Estadisticas de la distancia:")
print("Promedio",columna.mean())      
print("Mediana",columna.median())      
print("Max",columna.max())         
print("Min",columna.min())       
print("Desviación Estándar",columna.std())        