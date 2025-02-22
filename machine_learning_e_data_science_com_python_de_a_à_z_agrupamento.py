# -*- coding: utf-8 -*-
"""Machine Learning e Data Science com Python de A à Z - Agrupamento.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Up81lDmA-1dM-4ckm0yQ0o-OQPDogcbU

# Machine Learning e Data Science com Python de A à Z IA Expert Academy - Agrupamento
"""

!pip install plotly --upgrade

import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from sklearn.preprocessing import StandardScaler

"""# K-means

## Base idade e salário
"""

from sklearn.cluster import KMeans

x=[20,  27,  21,  37,  46, 53, 55,  47,  52,  32,  39,  41,  39,  48,  48]
y=[1000,1200,2900,1850,900,950,2000,2100,3000,5900,4100,5100,7000,5000,6500]

grafico = px.scatter(x = x, y = y)
grafico.show()

base_salario = np.array([[20,1000],[27,1200],[21,2900],[37,1850],[46,900],
                        [53,950],[55,2000],[47,2100],[52,3000],[32,5900],
                        [39,4100],[41,5100],[39,7000],[48,5000],[48,6500]])

base_salario

scaler_salario = StandardScaler()
base_salario = scaler_salario.fit_transform(base_salario)

base_salario

kmeans_salario = KMeans(n_clusters=3)
kmeans_salario.fit(base_salario)

centroides = kmeans_salario.cluster_centers_
centroides

scaler_salario.inverse_transform(kmeans_salario.cluster_centers_)

rotulos = kmeans_salario.labels_
rotulos

grafico1 = px.scatter(x = base_salario[:,0], y = base_salario[:,1], color=rotulos)
grafico2 = px.scatter(x = centroides[:,0], y = centroides[:,1], size = [12, 12, 12])
grafico3 = go.Figure(data = grafico1.data + grafico2.data)
grafico3.show()

"""## Dados randômicos"""

from sklearn.datasets import make_blobs

X_random, y_random = make_blobs(n_samples=200, centers=5, random_state=1)

X_random

y_random

grafico = px.scatter(x = X_random[:,0], y = X_random[:,1])
grafico.show()

kmeans_blobs = KMeans(n_clusters=5)
kmeans_blobs.fit(X_random)

rotulos = kmeans_blobs.predict(X_random)
rotulos

centroides = kmeans_blobs.cluster_centers_
centroides

grafico1 = px.scatter(x = X_random[:,0], y = X_random[:,1], color = rotulos)
grafico2 = px.scatter(x = centroides[:,0], y = centroides[:,1], size = [5, 5, 5, 5, 5])
grafico3 = go.Figure(data = grafico1.data + grafico2.data)
grafico3.show()

"""## Base de dados cartão de crédito - 1 atributo

- Fonte: https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients
"""

import pandas as pd
base_cartao = pd.read_csv('/content/credit_card_clients.csv', header = 1)
base_cartao

base_cartao['BILL_TOTAL'] = base_cartao['BILL_AMT1'] + base_cartao['BILL_AMT2'] + base_cartao['BILL_AMT3'] + base_cartao['BILL_AMT4'] + base_cartao['BILL_AMT5'] + base_cartao['BILL_AMT6']

base_cartao

X_cartao = base_cartao.iloc[:, [1, 25]].values
X_cartao

scaler_cartao = StandardScaler()
X_cartao = scaler_cartao.fit_transform(X_cartao)

X_cartao

wcss = []
for i in range(1, 11):
  #print(i)
  kmeans_cartao = KMeans(n_clusters=i, random_state=0)
  kmeans_cartao.fit(X_cartao)
  wcss.append(kmeans_cartao.inertia_)

wcss

grafico = px.line(x = range(1,11), y = wcss)
grafico.show()

kmeans_cartao = KMeans(n_clusters=4, random_state=0)
rotulos = kmeans_cartao.fit_predict(X_cartao)

grafico = px.scatter(x = X_cartao[:,0], y = X_cartao[:,1], color=rotulos)
grafico.show()

lista_clientes = np.column_stack((base_cartao, rotulos))
lista_clientes

lista_clientes = lista_clientes[lista_clientes[:,26].argsort()]
lista_clientes

"""## Base de dados cartão de crédito - mais atributos"""

base_cartao.columns

X_cartao_mais = base_cartao.iloc[:,[1,2,3,4,5,25]].values
X_cartao_mais

scaler_cartao_mais = StandardScaler()
X_cartao_mais = scaler_cartao.fit_transform(X_cartao_mais)

X_cartao_mais

wcss = []
for i in range(1, 11):
  kmeans_cartao_mais = KMeans(n_clusters = i, random_state = 0)
  kmeans_cartao_mais.fit(X_cartao_mais)
  wcss.append(kmeans_cartao_mais.inertia_)

grafico = px.line(x = range(1,11), y = wcss)
grafico.show()

kmeans_cartao_mais = KMeans(n_clusters=2, random_state=0)
rotulos = kmeans_cartao_mais.fit_predict(X_cartao_mais)

rotulos

from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_cartao_mais_pca = pca.fit_transform(X_cartao_mais)

X_cartao_mais_pca.shape

X_cartao_mais_pca

grafico = px.scatter(x= X_cartao_mais_pca[:,0], y = X_cartao_mais_pca[:,1], color=rotulos)
grafico.show()

lista_clientes = np.column_stack((base_cartao, rotulos))
lista_clientes = lista_clientes[lista_clientes[:,26].argsort()]
lista_clientes

"""# Agrupamento hierárquico

## Base salário idade
"""

base_salario

grafico = px.scatter(x = base_salario[:,0], y = base_salario[:,1])
grafico.show()

import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

dendrograma = dendrogram(linkage(base_salario, method='ward'))
plt.title('Dendrograma')
plt.xlabel('Pessoas')
plt.ylabel('Distância');

from sklearn.cluster import AgglomerativeClustering

hc_salario = AgglomerativeClustering(n_clusters=3, linkage='ward', affinity='euclidean')
rotulos = hc_salario.fit_predict(base_salario)

rotulos

grafico = px.scatter(x = base_salario[:,0], y = base_salario[:,1], color = rotulos)
grafico.show()

"""## Base cartão de crédito"""

X_cartao

dendrograma = dendrogram(linkage(X_cartao, method = 'ward'))

hc_cartao = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage = 'ward')
rotulos = hc_cartao.fit_predict(X_cartao)

rotulos

grafico = px.scatter(x = X_cartao[:,0], y = X_cartao[:,1], color = rotulos)
grafico.show()

"""# DBSCAN

## Base salário idade
"""

base_salario

from sklearn.cluster import DBSCAN

dbscan_salario = DBSCAN(eps = 0.95, min_samples=2)
dbscan_salario.fit(base_salario)

rotulos = dbscan_salario.labels_
rotulos

grafico = px.scatter(x = base_salario[:,0], y = base_salario[:,1], color = rotulos)
grafico.show()

"""## Base cartão de crédito"""

X_cartao

dbscan_cartao = DBSCAN(eps=0.37, min_samples=5)
rotulos = dbscan_cartao.fit_predict(X_cartao)

rotulos

np.unique(rotulos, return_counts=True)

grafico = px.scatter(x = X_cartao[:,0], y = X_cartao[:,1], color = rotulos)
grafico.show()

"""# K-means x Hierárquico x DBSCAN"""

from sklearn import datasets

X_random, y_random = datasets.make_moons(n_samples=1500, noise = 0.09)

X_random

y_random

np.unique(y_random)

grafico = px.scatter(x = X_random[:,0], y = X_random[:,1])
grafico.show()

kmeans = KMeans(n_clusters=2)
rotulos = kmeans.fit_predict(X_random)
grafico = px.scatter(x = X_random[:,0], y = X_random[:, 1], color = rotulos)
grafico.show()

hc = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
rotulos = hc.fit_predict(X_random)
grafico = px.scatter(x = X_random[:,0], y = X_random[:, 1], color = rotulos)
grafico.show()

dbscan = DBSCAN(eps=0.1)
rotulos = dbscan.fit_predict(X_random)
grafico = px.scatter(x = X_random[:,0], y = X_random[:, 1], color = rotulos)
grafico.show()