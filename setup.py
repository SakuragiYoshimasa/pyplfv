from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext

import numpy
import scipy

ext_modules = [
    Extension('pyplfv.utility',
              sources=['pyplfv/utility.pyx'],
              include_dirs=[numpy.get_include(), scipy.get_include()]),
    Extension('pyplfv.wavelet',
              sources=['pyplfv/wavelet.pyx'],
              include_dirs=[numpy.get_include(), scipy.get_include()]),
    Extension('pyplfv.tve',
              sources=['pyplfv/tve.pyx'],
              include_dirs=[numpy.get_include(), scipy.get_include()]),
    Extension('pyplfv.plf',
              sources=['pyplfv/plf.pyx'],
              include_dirs=[numpy.get_include(), scipy.get_include()]),
    Extension('pyplfv.plv',
              sources=['pyplfv/plv.pyx'],
              include_dirs=[numpy.get_include(), scipy.get_include()])
]

setup(
    name='pyplfv',
    version='0.0.1',
    description='Python package for the Phase-locking statistical analysis of EEG data.',
    long_description='README.md',
    author='Yoshimasa Sakuragi',
    author_email='ysakuragi16@gmail.com',
    install_requires=['numpy', 'matplotlib'],
    url='https://github.com/SakuragiYoshimasa/pyplfv',
    license=license,
    packages=['pyplfv'],
    ext_modules=ext_modules,
    test_suite='tests',
    cmdclass={'build_ext': build_ext}
)
