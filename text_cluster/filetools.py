
import pickle
import nltk
import re
from sklearn import decomposition

# 保存至文件
def savefile(savepath, content):
    with open(savepath, "wb") as fp:
        fp.write(content)

def processString(string):
    stopwords = nltk.corpus.stopwords.words('english')
    porter = nltk.PorterStemmer()
    split_re = re.compile('[^a-zA-Z]')
    # words = ""
    # for word in split_re.split(string):
    #     if len(word) > 0 and word.lower() not in stopwords:
    #         words = words+" "+porter.stem(word.lower())
    words = [porter.stem(word.lower()) for word in split_re.split(string)\
              if len(word)>0 and\
              word.lower() not in stopwords]
    # wordMap = {}
    # for word in words:
    #     # if len(word)<3:continue
    #     wordMap[word] = wordMap.get(word,0)+1
    return words



# 读取文件
def readfile(path):
    with open(path, "rb") as fp:
        content = fp.read()
    return content


def writebunchobj(path, bunchobj):
    with open(path, "wb") as file_obj:
        pickle.dump(bunchobj, file_obj)

def data_decomposition(data):
    pca = decomposition.PCA(n_components=3)
    pca.fit(data)
    new_data = pca.transform(data)
    return new_data

# 读取bunch对象
def readbunchobj(path):
    with open(path, "rb") as file_obj:
        bunch = pickle.load(file_obj)
    return bunch