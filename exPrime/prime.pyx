
def findPrimes(int num_primes=1):
    cdef int len_p, n, i # Local C variables
    cdef int primes[1000] # C array variable
    num_primes = 1000 if num_primes > 1000 else num_primes

    len_p = 0
    n = 2
    while len_p < num_primes:
        # This loop is translated entirely into C code, because no Python objects are referred to.
        for i in primes[:len_p]:
            if n % i == 0:
                break
        else: # Executed if no break occured
            primes[len_p] = n
            len_p += 1
        n+=1
        
    # Conver a C array to a Python list. result_as_list is a Python object type
    # Cython can automatically convert many C types from and to Python types.
    result_as_list = [prime for prime in primes[:len_p]]

    return result_as_list