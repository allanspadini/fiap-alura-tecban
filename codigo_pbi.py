# O código a seguir para criar um dataframe e remover as linhas duplicadas sempre é executado e age como um preâmbulo para o script: 

#dataset = pandas.DataFrame('age', 'charges')
#dataset = dataset.drop_duplicates()

# Cole ou digite aqui seu código de script:

dataset['smoker'] = [bool(sm == 'yes') for sm in dataset['smoker']]
dataset['sex_male'] = [bool(sm =='yes') for sm in dataset['sex']]
dataset['charges/age'] = dataset['charges'] - dataset['age']*200

import matplotlib.pyplot as plt
import numpy as np


#dataset.plot(kind='scatter', x='age', y='charges', color=dataset['smoker'])
#plt.show()

from sklearn.cluster import KMeans

X = np.array(dataset[['charges/age']])
modelo = KMeans(n_clusters=3, max_iter=500, init=np.array([16000, 28000, 48000]).reshape(-1, 1), n_init=1)
modelo = modelo.fit(X.reshape(-1, 1))
dataset['cluster'] = modelo.labels_

dataset.plot(kind='scatter', x='age', y='charges', color=dataset['cluster'],colormap='plasma')

plt.title('Clusters of Patients')
plt.show()

