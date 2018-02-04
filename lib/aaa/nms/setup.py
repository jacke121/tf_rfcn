#!/usr/bin/python
# python version: 2.7.3
# Filename: SetupTestOMP.py

# Run as:
#    python setup.py build_ext --inplace
import numpy
import sys

sys.path.insert(0, "..")
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext

# ext_module = cythonize("TestOMP.pyx")
ext_modules =[ Extension(
                "gpu_nms",
                ["gpu_nms.pyx"],
            )
            ]

setup(
    cmdclass={'build_ext': build_ext},
    include_dirs=[numpy.get_include()],
    ext_modules=ext_modules,
)
