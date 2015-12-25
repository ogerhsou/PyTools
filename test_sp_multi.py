#!/usr/bin/env python
"this is test module"

import sys, os
import time
from scipy.sparse import coo_matrix
import numpy as np

def generate_random_sparse_array(nrows, ncols, numdense):
    """Generate a random sparse array"""
    i = np.random.randint(0, nrows, numdense)
    j = np.random.randint(0, ncols, numdense)
    data = np.random.randint(1,6, numdense)
    ij = np.vstack((i,j))
    return coo_matrix((data, ij), shape=(nrows, ncols))

@profile
#python -m memory_profiler xxx.py
#test memory
def test_sp_multi():
    "test function"

    print 'Test sparse matrix'
    # A = generate_random_sparse_array(72000, 10000, 10000000)
    A = generate_random_sparse_array(72000, 10000, 10000000).todense()
    B = np.random.random(size=(72000,10))

    time1 = time.time()

    test1 = A.transpose() * B
    test2 = A * test1

    time2 = time.time()
    # print C
    # print C.todense()
    print 'The elapsed time of calculating multiplication is: ', time2 - time1, 's.'


if __name__ == '__main__':
    test_sp_multi()