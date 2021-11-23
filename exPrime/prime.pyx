# distutils: language=c++
'''
With Cython, it is also possible to take advantage of the C++ language, 
notably, part of the C++ standard library is directly importable from Cython code.
The first line is a compiler directive. It tells Cython to compile your code to C++.
'''

from libcpp.vector cimport vector

def findPrimes(unsigned int num_primes=1):
    cdef int n, i
    cdef vector[int] primes
    primes.reserve(num_primes)

    n = 2
    while primes.size() < num_primes:
        for i in primes:
            if n % i == 0:
                break
        else:
            primes.push_back(n)
        n+=1
        
    # If possible, C values and C++ objects are automatically converted to Python objects at need.
    # so here, the vector will be copied into a Python list.
    return primes