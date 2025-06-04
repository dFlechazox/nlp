#!/usr/bin/env python


from sklearn.datasets.base import Bunch
from sklearn.feature_extraction.text import TfidfVectorizer
from filetools import readfile, readbunchobj, writebunchobj


def vector_space(bunch_path, space_path, train_tfidf_path=None):
    bunch = readbunchobj(bunch_path)
    tfidfspace = Bunch(target_name=bunch.target_name, label=bunch.label, filenames=bunch.filenames, tdm=[],
                       vocabulary={})

    if train_tfidf_path is not None:
        trainbunch = readbunchobj(train_tfidf_path)
        tfidfspace.vocabulary = trainbunch.vocabulary
        vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,max_features=400,
                                     vocabulary=trainbunch.vocabulary)
        tfidfspace.tdm = vectorizer.fit_transform(bunch.contents)

    else:
        vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,max_features=400)
        tfidfspace.tdm = vectorizer.fit_transform(bunch.contents)
        tfidfspace.vocabulary = vectorizer.vocabulary_

    writebunchobj(space_path, tfidfspace)
    print("tf-idf词向量空间实例创建成功！！！")


if __name__ == '__main__':

    bunch_path = "word_bag/dataset.dat"
    space_path = "word_bag/tfdifspace.dat"
    vector_space(bunch_path, space_path)