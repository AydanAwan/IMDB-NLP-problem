"""takes in the list which has the tfidf values and removes the words from it so we are left with a matrix with just the values."""


class tfidfmatrix:

    def __init__(self, tfidfscores):
        self.tfidfscores = tfidfscores

    def gettfiidfmatrix(self):
        tfmat = []
        for i in self.tfidfscores:
            doctfidf = []
            count = 0
            for j in i:
                count += 1
                doctfidf.append(j[1])
                if count == 6:
                    break
            tfmat.append(doctfidf)
        return tfmat
