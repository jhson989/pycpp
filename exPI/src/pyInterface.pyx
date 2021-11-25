#cython: language_level=3

cdef extern from "pi_calculator.h":
    double get_PI(int num_iters)

def getPI(num_iters = 100):
    return get_PI(num_iters)