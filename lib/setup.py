# --------------------------------------------------------
# Fast R-CNN
# Copyright (c) 2015 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Ross Girshick
# --------------------------------------------------------

import numpy as np
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
try:
    numpy_include = np.get_include()
except AttributeError:
    numpy_include = np.get_numpy_include()
cmdclass = {}
CUDA=r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v8.0"
ext_modules = [
    Extension(
        "utils.cython_bbox",
        ["utils/bbox.pyx"],
    ),
    Extension(
        "utils.cython_nms",
        ["utils/nms.pyx"],
    ),
    Extension(
        "nms.cpu_nms",
        ["nms/cpu_nms.pyx"],
    ),
    Extension(
        "nms.cpu_nms",
        ["nms/cpu_nms.pyx"],
        extra_compile_args={'gcc': ["-Wno-cpp", "-Wno-unused-function"]},
        include_dirs=[numpy_include]
    ),
    Extension('nms.gpu_nms',
              ['nms/gpu_nms.pyx'],
              library_dirs=[CUDA+'\lib'],
              libraries=['cudart'],
              language='c++',
              runtime_library_dirs=[CUDA+'\lib'],
              include_dirs=[numpy_include, CUDA+'\include']
              )
]
cmdclass.update({'build_ext': build_ext})

setup(
    name='fast_rcnn',
    cmdclass=cmdclass,
    ext_modules=ext_modules,
    include_dirs=[np.get_include()]
)