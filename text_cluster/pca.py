from sklearn import decomposition
from sklearn.manifold import TSNE
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
from filetools import readbunchobj
import numpy as np
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()

def data_decomposition(data,label):

    # pca = decomposition.PCA(n_components=2)
    # pca.fit(data)
    # new_data = pca.transform(data)

    tsne = TSNE(n_components=2)
    new_data = tsne.fit_transform(data)
    plt.scatter(new_data[:, 0], new_data[:, 1], c=label)
    plt.show()
    print(new_data.shape)

if __name__ == '__main__':
    trainpath = "word_bag/tfdifspace.dat"
    train_set = readbunchobj(trainpath)
    x = train_set.tdm.toarray()
    label = encoder.fit_transform(train_set.label)
    label = np.array(label).T
    print(label.shape)
    data_decomposition(x,label)