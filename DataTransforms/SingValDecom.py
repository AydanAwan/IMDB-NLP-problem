"""calculate the singular value decompostion of the tfidf values."""

import numpy


class SingValDecom:

    def __init__(self, tfidfmatrix):
        self.tfidfmatrix = tfidfmatrix

    def CalSVD(self):
        mat = numpy.array(self.tfidfmatrix)
        return numpy.linalg.svd(mat, full_matrices=True, compute_uv=True, hermitian=False)
