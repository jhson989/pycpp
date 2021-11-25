from distutils.core import Extension, setup
from Cython.Build import cythonize
import pathlib

ext_modules = [
    Extension("pyInterface",
              sources=["pyInterface.pyx"],
              libraries=["piCalculator"],
              library_dirs=[str(pathlib.Path().resolve())],
              include_dirs=[str(pathlib.Path().resolve())+"/../../include/"]
              )
]

setup(name="pyInterface",
      ext_modules=cythonize(ext_modules))