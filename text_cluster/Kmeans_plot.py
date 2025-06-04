
from sklearn.cluster import KMeans
from filetools import readbunchobj
from sklearn.metrics import silhouette_score
import numpy as np
from sklearn.manifold import TSNE
import csv
import matplotlib.pyplot as plt
np.random.seed(5)

def MyKmeans():
    print("文本聚类_KMeans_结果可视化")
    clusters = [ x for x in range(6, 13, 3)]
    # 导入训练集
    trainpath = "word_bag/tfdifspace.dat"
    train_set = readbunchobj(trainpath)
    tsne = TSNE(n_components=2)
    new_data = tsne.fit_transform(train_set.tdm.toarray())

    for k in clusters:
        # 训练：输入词袋向量和分类标签，alpha:0.001 alpha越小，迭代次数越多，精度越高
        model = KMeans(n_clusters=k,n_jobs=5,max_iter=100) # 分为k类
        y_predict = model.fit_predict(train_set.tdm)
        label_pred = model.labels_  # 获取聚类标签
        plt.scatter(new_data[:, 0], new_data[:, 1], c=label_pred)
        plt.title("k_means cluster_k="+str(k))
        plt.savefig("./result/kmeans_"+str(k)+".png")
        print(k)
        # plt.show()
    print("kmeans_plot_finish!")


if __name__ == '__main__':
    MyKmeans()