"""methods for cleaning the data by removing puctuation stop words and names."""

from nltk.corpus import stopwords
from nltk.tag.stanford import StanfordNERTagger
import os
java_path = "C:/Program Files/Common Files/Oracle/Java/javapath/java.exe"
os.environ['JAVAHOME'] = java_path
PATH_TO_JAR = '/Users/aydan/AppData/Local/Programs/Python/Python310/Lib/stanford-ner-2020-11-17/stanford-ner.jar'
PATH_TO_MODEL = '/Users/aydan/AppData/Local/Programs/Python/Python310/Lib/stanford-ner-2020-11-17/classifiers/english.all.3class.distsim.crf.ser.gz'
tagger = StanfordNERTagger(model_filename=PATH_TO_MODEL, path_to_jar=PATH_TO_JAR, encoding='utf-8')


class Cleaning:

    def __init__(self, data):
        self.data = data

    def DelPunc(self):
        dataNoPunc = []
        for i in self.data:
            if i.isalpha():
                dataNoPunc.append(i.lower())
        return dataNoPunc

    def DelStop(self):
        dataNostop = []
        for i in self.data:
            if i not in stopwords.words("english"):
                dataNostop.append(i)
        return dataNostop

    def DelNames(self):
        dataNoNames = []
        datatags = self.TagData()
        for i in datatags:
            if i[1] != 'PERSON':
                dataNoNames.append(i[0])
        return dataNoNames

    def TagData(self):
        return tagger.tag(self.data)
