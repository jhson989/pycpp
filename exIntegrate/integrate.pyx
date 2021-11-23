
# except? -2 means that an error will be checked for if -2 is returned 
# (though the ? indicates that -2 may also be used as a valid return value)
cdef double f_typed(double x) except? -2:
    return x**2 - 2*x

cpdef double integrate_typed(double a, double b, int N=1):
    cdef int i
    cdef double s = 0
    cdef double dx = (b-a)/N
    
    for i in range (N):
        s += (f_typed(a+i*dx)+f_typed(a+(i+1)*dx))/2 * dx
    
    return s


def f_untyped(x):
    return x**2 - 2*x

def integrate_untyped(a, b, N=1):
    s = 0
    dx = (b-a)/N
    for i in range (N):
        s += (f_untyped(a+i*dx)+f_untyped(a+(i+1)*dx))/2 * dx
    
    return s