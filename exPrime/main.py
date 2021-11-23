import prime
import time

start = time.time_ns()
prime.findPrimes(100000)
print("Elapsed time: %.3fs" % ((time.time_ns()-start)*1e-9))
