"""method for doing the tf-idf transformation."""


import math


class Transformations:
    def __init__(self, doccount, freqdoc, freqalldoc):
        self.doccount = doccount
        self.freqdoc = freqdoc
        self.freqalldoc = freqalldoc

    def CalIDF(self):
        return math.log(1 + self.freqdoc)

    def CalTF(self):
        return math.log(self.doccount / self.freqalldoc)

    def CalTFIDF(self):
        return self.CalIDF() * self.CalTF()
