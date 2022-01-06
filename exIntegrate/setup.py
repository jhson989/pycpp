from distutils.core import setup
from Cython.Build import cythonize

setup(
    name="Fibbonacci sequence",
    ext_modules=cythonize("integrate.pyx")
)

# python setup.py build_ext --inplace