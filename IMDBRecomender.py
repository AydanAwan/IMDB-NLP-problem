"""takes the imdb data then transforms it using the transform methods then impliments the lsa model."""


import csv
from DataTransforms.Tokenizing import tokenizing
from DataTransforms.Cleaning import Cleaning
from DataTransforms.UniqueWords import UniqueWords
from DataTransforms.tfidfOnSet import tfidfOnSet
from DataTransforms.tfidfmatrix import tfidfmatrix
from DataTransforms.SingValDecom import SingValDecom


class IMDBRecomender:
    fulldata = open('mpst_full_data.csv', encoding='utf-8')
    collist = ["title", "plot_synopsis"]
    readdata = csv.reader(fulldata)
    data = list(readdata)
    titles = []
    synopses = []
    countvar = 0
    for i in data:
        titles.append(i[1])
        synopses.append(i[2])
        if countvar == 5:
            break
        countvar += 1
    del titles[0]
    del synopses[0]
    tokenedsynops = []
    for i in synopses:
        tokenedsynops.append(tokenizing(i).nltktokenize())
    cleanedsyn = []
    for i in tokenedsynops:
        cleaned = Cleaning(i).DelNames()
        cleaned = Cleaning(cleaned).DelPunc()
        cleaned = Cleaning(cleaned).DelStop()
        cleanedsyn.append(cleaned)
    allwords = []
    fullcorpus = []
    fullfreqdis = []
    for i in cleanedsyn:
        for j in i:
            allwords.append(j)
    fulldictionary = UniqueWords(allwords).CalUnique()
    allfreqdis = UniqueWords(allwords).CalFreqD()
    for i in cleanedsyn:
        fullcorpus.append(UniqueWords(i).CalUnique())
    for i in cleanedsyn:
        fullfreqdis.append(UniqueWords(i).CalFreqD())
    tfidfscores = []
    doccount = len(fullfreqdis)
    for i in fullfreqdis:
        tfidfscores.append(tfidfOnSet(doccount, i, allfreqdis).runtfidf())
    scoresmatrix = tfidfmatrix(tfidfscores).gettfiidfmatrix()
    #print(scoresmatrix)
    dataSVD = SingValDecom(scoresmatrix).CalSVD()
    print(dataSVD)
