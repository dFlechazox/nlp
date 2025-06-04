from sklearn.cluster import AgglomerativeClustering
from filetools import readbunchobj
from sklearn.metrics import silhouette_score
import csv

def H_Clustering():
    print("文本聚类_层次聚类")
    # 导入训练集
    trainpath = "word_bag/tfdifspace.dat"
    train_set = readbunchobj(trainpath)
    clusters = [x for x in range(3, 15)]

    with open('result/H_Clustering_score.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for k in clusters:
            model = AgglomerativeClustering(n_clusters=k, affinity='euclidean')
            y_predict = model.fit_predict(train_set.tdm.toarray())
            label_pred = model.labels_  # 获取聚类标签

            result = {}
            for label in label_pred:
                if label in result:  # 直接判断key在不在字典中
                    result[label] += 1
                else:
                    result[label] = 1
            print(sorted(result.items(),key=lambda item:item[0]))
            s = silhouette_score(train_set.tdm, y_predict)
            temp = [k, s]
            writer.writerow(temp)
            print("聚为{}类时，轮廓系数为{}".format(k, s))


if __name__ == '__main__':
    H_Clustering()