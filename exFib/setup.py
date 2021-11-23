from distutils.core import setup
from Cython.Build import cythonize

setup(
    name="Fibbonacci sequence",
    ext_modules=cythonize("fib.pyx"),
    zip_safe=False
)

# python setup.py build_ext --inplace
812 

830