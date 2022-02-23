"""method for finding all teh unique words in a text used in creating teh corpus and the dictionary."""


# from nltk.probability import FreqDist


class UniqueWords:

    def __init__(self, cleaneddata):
        self.data = cleaneddata

    def CalUnique(self):
        dataUni = []
        for i in self.data:
            if i in dataUni:
                continue
            dataUni.append(i)
        return dataUni

    def CalFreqD(self):
        workingdataset = self.data
        frequency = []
        while len(workingdataset) > 0:
            removeindices = []
            for i in range(len(workingdataset)):
                if i == 0:
                    frequency.append([workingdataset[0], 1])
                    removeindices.append(i)
                    continue
                if workingdataset[i] == frequency[len(frequency) - 1][0]:
                    frequency[len(frequency) - 1][1] += 1
                    removeindices.append(i)
            for i in sorted(removeindices, reverse=True):
                del workingdataset[i]
        return sorted(frequency, key=lambda x: x[1], reverse=True)
