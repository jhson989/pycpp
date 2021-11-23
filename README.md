# pycpp

### 0. Introduction
Cython project for calling c++ routines from a python program   
Cython is a Python compiler.  
[https://cython.readthedocs.io/en/latest/src/quickstart/overview.html]

### 1. Cython’s two major use cases
- Extending the CPython interpreter with fast binary modules
    - Static type declarations 
    - Translated into optimized C/C++ code
- Interfacing Python code with external C libraries.

### 2. Building Cython code : setuptools
Cython code must, unlike Python, be compiled in two stages:
- A .pyx or .py file is compiled by Cython to a .c file
    - Containing the code of a Python extension module.
- The .c file is compiled by a C compiler to a .so file
    - Can be import-ed directly into a Python session