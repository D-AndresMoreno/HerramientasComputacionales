file = './data.csv'
import pandas as pd
import matplotlib.pyplot as plt      
from sklearn.cluster import KMeans
import random
import math

df = pd.read_csv(file)

def kmeans(df, centers=2, maxiter=100):
    cs = []
    cols = df.columns
    for i in range(centers):
        c = []
        for col in cols:
            c.append(random.uniform(df[col].min(),df[col].max()))
        cs.append(c)
    
    convergencia = False
    cs_aux = []
    classes = []
    classes_aux = []
    i=0
    
    while i<maxiter and not convergencia:
        
        cs_aux = []
        classes_aux = []
        
        for index, row in df.iterrows():
            aux = []
            for c in cs:
                res = 0
                for j in range(len(c)):
                    res = res + (c[j]-row[j])*(c[j]-row[j])
                aux.append(math.sqrt(res))
            classes_aux.append(aux.index(min(aux)))
        
        aux_df = df.copy()
        aux_df["classes"] = classes_aux
        
        for j in range(len(cs)):
            c_points = aux_df[aux_df.classes==j]
            new_center = []
            for col in c_points.columns:
                if col!="classes":
                    new_center.append(c_points[col].mean())
            cs_aux.append(new_center)
        
        if cs == cs_aux:
            convergencia = True
        
        cs = cs_aux
        classes = classes_aux
        
        i = i+1
    
    return cs,classes
    

##############################################################
#  k means
##############################################################

test = df[["Start_Lat","Start_Lng"]]
test = test.dropna(axis = 0, how = 'any')

c,cla = kmeans(test, centers=4)
print(c)

plt.scatter(df["Start_Lat"],df["Start_Lng"],c=cla)
for i in range(len(c)):
  plt.scatter(c[i][0],c[i][1],marker="*",c="red")
plt.show()

#Predicción
kmeansCenter = KMeans(n_clusters=4).fit(test)
centroids = kmeansCenter.cluster_centers_
print('Centroid: ', centroids)