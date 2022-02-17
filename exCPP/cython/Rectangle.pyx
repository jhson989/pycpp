# distutils: language = c++


cdef extern from "Rectangle.hpp" namespace "excpp":
    cdef cppclass Rectangle:
        Rectangle(int x0, int y0, int x1, int y1)
        int get_length()
        int get_height()
        int get_area()
        void move(int dx, int dy)
     
cdef class PyRectangle:
    cdef Rectangle *thisptr

    def __cinit__(self, int x0, int y0, int x1, int y1):
        self.thisptr = new Rectangle(x0, y0, x1, y1)

    def __dealloc__(self):
        del self.thisptr

    def getLength(self):
        return self.thisptr.get_length()
    def getHeight(self):
        return self.thisptr.get_height()
    def getArea(self):
        return self.thisptr.get_area()

    def move(self, int dx, int dy):
        self.thisptr.move(dx, dy)
    
