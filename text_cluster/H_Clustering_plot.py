from sklearn.cluster import AgglomerativeClustering
from filetools import readbunchobj
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

def H_Clustering():
    print("文本聚类_层次聚类_plot")
    # 导入训练集
    trainpath = "word_bag/tfdifspace.dat"
    train_set = readbunchobj(trainpath)
    clusters = [x for x in range(6, 13, 3)]
    tsne = TSNE(n_components=2)
    new_data = tsne.fit_transform(train_set.tdm.toarray())

    for k in clusters:
        model = AgglomerativeClustering(n_clusters=k, affinity='euclidean')
        y_predict = model.fit_predict(train_set.tdm.toarray())
        label_pred = model.labels_  # 获取聚类标签
        plt.scatter(new_data[:, 0], new_data[:, 1], c=label_pred)
        plt.title("H cluster_k=" + str(k))
        plt.savefig("./result/H_" + str(k) + ".png")
        # plt.show()
    print("H_Clustering_plot_finish!")


if __name__ == '__main__':
    H_Clustering()