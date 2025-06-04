from words_segment import corpus_segment
from wordsToBunch import corpus2Bunch
from TF_IDF import vector_space


def main():
    print("1.对训练集进行分词")
    # 对训练集进行分词
    corpus_path = "./dataset/"  # 未分词分类语料库路径
    seg_path = "./dataset_res/"  # 分词后分类语料库路径
    corpus_segment(corpus_path, seg_path)

    print("2.对训练集进行Bunch化操作")
    # 对训练集进行Bunch化操作：
    # print ('*************************\nKNN\n*************************')
    wordbag_path = "word_bag/dataset.dat"  # Bunch存储路径
    seg_path = "dataset_res/"  # 分词后分类语料库路径
    corpus2Bunch(wordbag_path, seg_path, 12, 400)

    print("3.对数据集创建if-idf词向量空间实例")
    bunch_path = "word_bag/dataset.dat"
    space_path = "word_bag/tfdifspace.dat"
    vector_space(bunch_path, space_path)

if __name__ == "__main__":
    main()