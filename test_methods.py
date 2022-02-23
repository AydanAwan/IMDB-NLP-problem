"""testing for all the NLP methods."""


import unittest
from DataTransforms.Tokenizing import tokenizing
from DataTransforms.Cleaning import Cleaning
from DataTransforms.UniqueWords import UniqueWords


class TestMethods(unittest.TestCase):
    def test_tokenize(self):
        result = tokenizing("hello my name is aydan, what is yours? you're not from around here are you, I'm form here myself; raised in london town and i work as a programmer. i like being a programmer").nltktokenize()
        self.assertEquals(result, ['hello', 'my', 'name', 'is', 'aydan', ',', 'what', 'is', 'yours', '?', 'you', "'re", 'not', 'from', 'around', 'here', 'are', 'you', ',', 'I', "'m", 'form', 'here', 'myself', ';', 'raised', 'in', 'london', 'town', 'and', 'i', 'work', 'as', 'a', 'programmer', '.', 'i', 'like', 'being', 'a', 'programmer'])

    def test_removePunc(self):
        result = Cleaning(['hello', 'my', 'name', 'is', 'aydan', ',', 'what', 'is', 'yours', '?', 'you', "'re", 'not', 'from', 'around', 'here', 'are', 'you', ',', 'I', "'m", 'form', 'here', 'myself', ';', 'raised', 'in', 'london', 'town', 'and', 'i', 'work', 'as', 'a', 'programmer', '.', 'i', 'like', 'being', 'a', 'programmer']).DelPunc()
        self.assertEquals(result, ['hello', 'my', 'name', 'is', 'aydan', 'what', 'is', 'yours', 'you', 'not', 'from', 'around', 'here', 'are', 'you', 'i', 'form', 'here', 'myself', 'raised', 'in', 'london', 'town', 'and', 'i', 'work', 'as', 'a', 'programmer', 'i', 'like', 'being', 'a', 'programmer'])

    def test_removeStop(self):
        result = Cleaning(['hello', 'my', 'name', 'is', 'aydan', ',', 'what', 'is', 'yours', '?', 'you', "'re", 'not', 'from', 'around', 'here', 'are', 'you', ',', 'I', "'m", 'form', 'here', 'myself', ';', 'raised', 'in', 'london', 'town', 'and', 'i', 'work', 'as', 'a', 'programmer', '.', 'i', 'like', 'being', 'a', 'programmer']).DelStop()
        self.assertEquals(result, ['hello', 'name', 'aydan', ',', '?', "'re", 'around', ',', 'I', "'m", 'form', ';', 'raised', 'london', 'town', 'work', 'programmer', '.', 'like', 'programmer'])

    def test_getUnique(self):
        result = UniqueWords(['hello', 'my', 'name', 'is', 'aydan', ',', 'what', 'is', 'yours', '?', 'you', "'re", 'not', 'from', 'around', 'here', 'are', 'you', ',', 'I', "'m", 'form', 'here', 'myself', ';', 'raised', 'in', 'london', 'town', 'and', 'I', 'work', 'as', 'a', 'programmer', '.', 'I', 'like', 'being', 'a', 'programmer']).CalUnique()
        self.assertEquals(result, ['hello', 'my', 'name', 'is', 'aydan', ',', 'what', 'yours', '?', 'you', "'re", 'not', 'from', 'around', 'here', 'are', 'I', "'m", 'form', 'myself', ';', 'raised', 'in', 'london', 'town', 'and', 'work', 'as', 'a', 'programmer', '.', 'like', 'being'])

    def test_getFreqD(self):
        result = UniqueWords(['hello', 'my', 'name', 'is', 'aydan', ',', 'what', 'is', 'yours', '?', 'you', "'re", 'not', 'from', 'around', 'here', 'are', 'you', ',', 'I', "'m", 'form', 'here', 'myself', ';', 'raised', 'in', 'london', 'town', 'and', 'I', 'work', 'as', 'a', 'programmer', '.', 'I', 'like', 'being', 'a', 'programmer']).CalFreqD()
        self.assertEquals(result, [['I', 3], ['is', 2], [',', 2], ['you', 2], ['here', 2], ['a', 2], ['programmer', 2], ['hello', 1], ['my', 1], ['name', 1], ['aydan', 1], ['what', 1], ['yours', 1], ['?', 1], ["'re", 1], ['not', 1], ['from', 1], ['around', 1], ['are', 1], ["'m", 1], ['form', 1], ['myself', 1], [';', 1], ['raised', 1], ['in', 1], ['london', 1], ['town', 1], ['and', 1], ['work', 1], ['as', 1], ['.', 1], ['like', 1], ['being', 1]])

    def test_removeNames(self):
        result = Cleaning(['hello', 'my', 'name', 'is', 'Aydan', ',', 'what', 'is', 'yours', '?', 'you', "'re", 'not', 'from', 'around', 'here', 'are', 'you', ',', 'I', "'m", 'form', 'here', 'myself', ';', 'raised', 'in', 'London', 'town', 'and', 'I', 'work', 'as', 'a', 'programmer', '.', 'I', 'like', 'being', 'a', 'programmer']).DelNames()
        self.assertEquals(result, ['hello', 'my', 'name', 'is', ',', 'what', 'is', 'yours', '?', 'you', "'re", 'not', 'from', 'around', 'here', 'are', 'you', ',', 'I', "'m", 'form', 'here', 'myself', ';', 'raised', 'in', 'London', 'town', 'and', 'I', 'work', 'as', 'a', 'programmer', '.', 'I', 'like', 'being', 'a', 'programmer'])


if __name__ == '__main__':
    unittest.main()
