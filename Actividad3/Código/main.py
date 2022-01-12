file = './data.csv'
import pandas as pd
import matplotlib.pyplot as plt      
import numpy as np
import seaborn as sns

df = pd.read_csv(file)

columnaViento = df["Wind_Speed(mph)"] #descartamos outliers
columnaVisibility = df['Visibility(mi)']

#Histogramas
  #Visibility
bins2 = np.arange(0, columnaVisibility.max() + 1.5) - 0.5
bins2 = np.arange(0, 5 + 1.5) - 0.5

df.hist(column="Visibility(mi)", bins=bins2, grid=False, orientation="horizontal", color = "coral")
plt.show()

  #Viento
bins = np.arange(0, columnaViento.max() + 1.5) - 0.5
bins = np.arange(0, 5 + 1.5) - 0.5

df.hist(column="Wind_Speed(mph)", bins=bins, grid=False, orientation="horizontal", color = "coral")
plt.show()


#Bigotes
  #Visibility
df.boxplot(column=["Visibility(mi)"], color = "green", showmeans=True )
plt.show()

  #Viento
df.boxplot(column=["Wind_Speed(mph)"], color = "green", showmeans=True )
plt.show()

#Heatmap
plt.figure(figsize=(15, 5))
sns.heatmap(df.corr(), annot=True, vmin=0, vmax=1, cmap="cividis");
plt.show()
