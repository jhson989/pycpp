
# except? -2 means that an error will be checked for if -2 is returned 
# (though the ? indicates that -2 may also be used as a valid return value)
cdef double f(double x) except? -2:
    return x**2 - x

cpdef double integrate(double a, double b, int N=1):
    cdef int i
    cdef double s = 0
    cdef double dx = (b-a)/N
    
    for i in range (N):
        s += (f(a+i*dx)+f(a+(i+1)*dx))/2 * dx
    
    return s