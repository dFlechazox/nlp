from sklearn.cluster import KMeans
from filetools import readbunchobj,data_decomposition
from sklearn.metrics import silhouette_score
import numpy as np
import csv

np.random.seed(5)

def MyKmeans():
    print("文本聚类_KMeans")
    clusters = [ x for x in range(3,15)]
    # 导入数据集
    trainpath = "word_bag/tfdifspace.dat"
    train_set = readbunchobj(trainpath)

    with open('result/k_means_score.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for k in clusters:
            # 训练：输入词袋向量和分类标签，alpha:0.001 alpha越小，迭代次数越多，精度越高
            model = KMeans(n_clusters=k,n_jobs=5,max_iter=100) # 分为k类
            y_predict = model.fit_predict(train_set.tdm)
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
            print("聚为{}类时，轮廓系数为{}".format(k,s))

if __name__ == '__main__':
    MyKmeans()