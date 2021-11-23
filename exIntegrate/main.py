from integrate import integrate_typed, integrate_untyped
import time


def f(x):
    return x**2 - 2*x

def integrate_python(a, b, N=1):
    s = 0
    dx = (b-a)/N
    for i in range (N):
        s += (f(a+i*dx)+f(a+(i+1)*dx))/2 * dx
    
    return s
if __name__ == "__main__":

    print("\nCython performance test")

    for i in range(6, 9):
        
        print("Divide into 1e+%d" % i)

        start = time.time_ns() 
        result_python = integrate_python(-50, 100, int(10**i))
        time_python = time.time_ns() - start
        
        start = time.time_ns() 
        result_untyped = integrate_untyped(-50, 100, int(10**i))
        time_untyped = time.time_ns() - start

        start = time.time_ns() 
        result_typed = integrate_typed(-50, 100, int(10**i))
        time_typed = time.time_ns() - start

        print("Result : %f = %f = %f" % (result_python, result_untyped, result_typed))
        print("Elaped time: python(%fs) untyped cython(%fs) typed cython(%fs)" % (time_python*1e-9, time_untyped*1e-9, time_typed*1e-9))
        print("Speed up : untyped cython(%f), typed cython(%f)" % (time_python/time_untyped, time_python/time_typed))
