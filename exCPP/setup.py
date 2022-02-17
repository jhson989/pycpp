from distutils.core import Extension, setup
from Cython.Build import cythonize
import os

PROJ_NAME = "excpp"

ext_modules = [
    Extension(PROJ_NAME,
              sources=[
                "cython/Rectangle.pyx",
                "cython/Circle.pyx",
                "cpp/Rectangle.cpp",
                "cpp/Circle.cpp"
              ],
              include_dirs=["include"],
              language="c++"
              )
]


os.environ["CC"] = "g++"
setup(name=PROJ_NAME,
      ext_modules=cythonize(ext_modules))