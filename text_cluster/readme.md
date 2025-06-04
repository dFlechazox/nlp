## 本实验实现对新闻英文文本的聚类

实验选取了数据集中前12类数据，每类400条项目进行聚类。

## 数据集结构
'''
├─dataset   存储20类新闻数据
│  ├─alt.atheism
│  ├─...
│  └─talk.religion.misc
├─dataset_res 存储20类新闻数据预处理后的分词结果
│  ├─alt.atheism
│  ├─...
│  └─talk.religion.misc
├─result  存储实验结果，包括Kmeans聚类与层次聚类的运行结果以及聚类可视化结果
├─word_bag
│  ├─dataset.dat  分词结果bunch存储
│  └─tfdifspace.dat  词向量空间表示
'''

## 数据预处理
直接运行 data_processing.py 便可以生成word_bag中的中间结果。
可以通过修改 data_processing.py 第18行 corpus2Bunch(wordbag_path, seg_path, 12, 400)
来更改据选取的文档的类别数目和条目，12表示12类，400表示每类条目个数

## Kmeans聚类
运行 Kmeans.py
其中不同聚类簇数的结果保存在 ./result/k_means_score.csv

## Kmeans聚类可视化
运行 Kmeans_plot.py
可视化结果保存在 ./result/kmeans_*.png

## 层次聚类
运行 Hierarchical_Clustering.py
其中不同聚类簇数的结果保存在 ./result/H_Clustering_score.csv.csv

## 层次聚类可视化
运行 H_Clustering_plot.py
可视化结果保存在 ./result/H_*.png

 
