# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 14:39:27 2016

@author: zhuolin
"""

import platform
from distutils.core import setup, Extension
from os.path import join, split, dirname

headers = ['stdafx.h', 'UserApiDataType.h', 'UserApiStruct.h', 'MdApi.h', 'TraderApi.h', 'test_PyCTP.py']
sources = ['stdafx.cpp', 'PyCTP.cpp', 'UserApiDataType.cpp', 'UserApiStruct.cpp', 'MdApi.cpp', 'TraderApi.cpp']

sources = [join('.', 'pyctp', file) for file in sources]
depends = [join('.', 'pyctp', file) for file in headers]

optional = {}
if platform.system() == 'Linux':
    optional['extra_compile_args'] = ['-std=c++11']
    optional['runtime_library_dirs'] = ['./']
    optional['include_dirs']=['./api/6.6.1_P1_linux64']
    optional['library_dirs']=['./api/6.6.1_P1_linux64']
    depend_dynamics = ['api/6.6.1_P1_linux64/libthostmduserapi_se.so', 'api/6.6.1_P1_linux64/libthosttraderapi_se.so']
if platform.system() == 'Windows':
    optional['include_dirs'] = ['./api/6.6.1_P1_win32']
    optional['library_dirs'] = ['./api/6.6.1_P1_win32']
    depend_dynamics = ['api/6.6.1_P1_win32/thostmduserapi_se.dll', 'api/6.6.1_P1_win32/thosttraderapi_se.dll']
    if '64 bit' in platform.python_compiler():
        optional['include_dirs'] = ['./api/6.6.1_P1_win64']
        optional['library_dirs'] = ['./api/6.6.1_P1_win64']
        depend_dynamics = ['api/6.6.1_P1_win64/thostmduserapi_se.dll', 'api/6.6.1_P1_win64/thosttraderapi_se.dll']
argments = dict(name='PyCTP',
                sources=sources,
                language='c++',
                libraries=['thostmduserapi_se', 'thosttraderapi_se'],
                depends=depends)
argments.update(optional)

setup(name='PyCTP',
        version='1.0.1',
        description='CTP for Python',
        long_description='CTP 6.6.1_P1 for Python',
        author='Shi Zhuolin',
        author_email='shizhuolin@hotmail.com',
        url='http://www.pyctp.org/',
        keywords=['ctp','futures','stock'],
        license='LGPL-3.0',
        platforms=['linux-x86_64','win32','win-amd64'],
        ext_modules=[Extension(**argments)],
        scripts=['./pyctp/test_PyCTP.py'],

        #data_files=[('lib', depend_dynamics)],
      )
