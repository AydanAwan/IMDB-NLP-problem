"""methods so tehat you can impliment the transformations on a set."""


from DataTransforms.Transformations import Transformations  # ask if there is a better way to make this work because this is the dumbest thing ive ever seen in any language ever


class tfidfOnSet:

    def __init__(self, doccount, synopFreq, freqalldoc):
        self.doccount = doccount
        self.synopFreq = synopFreq
        self.freqalldoc = freqalldoc

    def runtfidf(self):
        freqdisforsyn = []
        for i in self.synopFreq:
            alldoccount = self.findFullDocCount(i[0])
            indoccount = i[1]
            tfidf = Transformations(self.doccount, indoccount, alldoccount).CalTFIDF()
            freqdisforsyn.append([i[0], tfidf])
        return sorted(freqdisforsyn, key=lambda x: x[1], reverse=True)

    def findFullDocCount(self, word):
        for i in self.freqalldoc:
            if i[0] == word:
                return i[1]
