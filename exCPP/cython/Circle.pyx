# distutils: language = c++

cdef extern from "Circle.hpp" namespace "excpp":
    cdef cppclass Circle:
        Circle(int x, int y, int r)
        double get_circumference()
        double get_area()

cdef class PyCircle:
    cdef Circle *thisptr

    def __cinit__(self, int x, int y, int r):
        self.thisptr = new Circle(x, y, r)

    def __dealloc__(self):
        del self.thisptr

    def getCircumference(self):
        return self.thisptr.get_circumference()

    def getArea(self):
        return self.thisptr.get_area()
