from distutils.core import Extension, setup
from Cython.Build import cythonize
import pathlib

ext_modules = [
    Extension("pyPI",
              sources=["pyInterface.pyx"],
              libraries=["piCalculator"],
              library_dirs=[str(pathlib.Path().resolve())],
              include_dirs=[str(pathlib.Path().resolve())+"/../../include/"]
              )
]

setup(name="pyPI",
      ext_modules=cythonize(ext_modules))