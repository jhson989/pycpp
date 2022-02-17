from distutils.core import Extension, setup
from Cython.Build import cythonize
import os

PROJ_NAME = "excpp"

ext_modules = [
    Extension(PROJ_NAME,
              sources=[
                "cython/rectInterface.pyx",
                "cpp/Rectangle.cpp"
              ],
              include_dirs=["include"],
              language="c++"
              )
]


os.environ["CC"] = "g++"
setup(name=PROJ_NAME,
      ext_modules=cythonize(ext_modules))