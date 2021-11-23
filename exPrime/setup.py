from distutils.core import setup
from Cython.Build import cythonize

setup(
    name="Fibbonacci sequence",
    ext_modules=cythonize(
        ["prime.pyx"]
    , annotate=True)
)

# python setup.py build_ext --inplace
812 

830