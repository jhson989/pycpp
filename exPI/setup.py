from distutils.core import setup
from Cython.Build import cythonize

setup(
    name="Monte Carlo PI calculator",
    ext_modules=cythonize(
        ["src/pyInterface.pyx"]
    , annotate=True)
)