from setuptools import Extension, find_packages, setup
from Cython.Build import cythonize
import platform
import codecs
from dl85 import __version__

from os import listdir
print([f for f in listdir("..")])

DISTNAME = 'pydl8.5'
DESCRIPTION = 'A package to build an optimal binary decision tree classifier.'
with codecs.open('../README.rst', encoding='utf-8-sig') as f:
    LONG_DESCRIPTION = f.read()
AUTHORS = 'Gael Aglin, Siegfried Nijssen, Pierre Schaus'
AUTHORS_EMAIL = 'aglingael@gmail.com, siegfried.nijssen@gmail.com, pschaus@gmail.com'
URL = 'https://github.com/aia-uclouvain/pydl8.5'
LICENSE = '../LICENSE.txt'
DOWNLOAD_URL = 'https://github.com/aia-uclouvain/pydl8.5'
VERSION = __version__
INSTALL_REQUIRES = ['setuptools', 'cython', 'numpy', 'scikit-learn', 'gurobipy', 'cvxpy']
SETUP_REQUIRES = ['setuptools', 'cython', 'numpy', 'scikit-learn', 'gurobipy', 'cvxpy']
KEYWORDS = ['decision trees', 'discrete optimization', 'classification']
CLASSIFIERS = ['Programming Language :: Python :: 3',
               'License :: OSI Approved :: MIT License',
               'Operating System :: OS Independent',
               'Intended Audience :: Science/Research',
               'Intended Audience :: Developers',
               'Topic :: Software Development',
               'Topic :: Scientific/Engineering']
EXTRAS_REQUIRE = {
    'tests': [
        'pytest',
        'pytest-cov'],
    'docs': [
        'sphinx',
        'sphinx-gallery',
        'sphinx_rtd_theme',
        'numpydoc',
        'sphinxcontrib',
        'sphinx_copybutton',
        'matplotlib'
    ]
}
PROJECT_URLS = {
    "Source on github": "https://github.com/aia-uclouvain/pydl8.5",
    "Documentation": "https://pydl85.readthedocs.io/en/latest/?badge=latest",
}

EXTENSION_NAME = 'dl85Optimizer'
EXTENSION_LANGUAGE = 'c++'
EXTENSION_SOURCE_FILES = ['cython_extension/error_function.pyx',
                          'cython_extension/dl85Optimizer.pyx',
                          '../cpp/src/dataManager.cpp',
                          '../cpp/src/depthTwoComputer.cpp',
                          '../cpp/src/dl85.cpp',
                          '../cpp/src/globals.cpp',
                          '../cpp/src/lcm_pruned.cpp',
                          '../cpp/src/query.cpp',
                          '../cpp/src/query_best.cpp',
                          '../cpp/src/query_totalfreq.cpp',
                          '../cpp/src/rCover.cpp',
                          '../cpp/src/rCoverTotalFreq.cpp',
                          '../cpp/src/rCoverWeighted.cpp',
                          '../cpp/src/trie.cpp', ]
EXTENSION_INCLUDE_DIR = ['../cpp/src', 'cython_extension']
# EXTENSION_BUILD_ARGS = ['-std=c++11']
EXTENSION_BUILD_ARGS = ['-std=c++11', '-DCYTHON_PEP489_MULTI_PHASE_INIT=0']
if platform.system() == 'Darwin':
    EXTENSION_BUILD_ARGS.append('-mmacosx-version-min=10.12')

dl85_extension = Extension(
    name=EXTENSION_NAME,
    language=EXTENSION_LANGUAGE,
    sources=EXTENSION_SOURCE_FILES,
    include_dirs=EXTENSION_INCLUDE_DIR,  # path for headers
    extra_compile_args=EXTENSION_BUILD_ARGS,
    extra_link_args=EXTENSION_BUILD_ARGS
)

setup(
    name=DISTNAME,
    version=VERSION,
    url=URL,
    project_urls=PROJECT_URLS,
    author=AUTHORS,
    author_email=AUTHORS_EMAIL,
    maintainer=AUTHORS,
    maintainer_email=AUTHORS_EMAIL,
    download_url=DOWNLOAD_URL,
    license=LICENSE,
    packages=find_packages(),  # ["dl85", "dl85.classifiers", "dl85.errors"],
    keywords=KEYWORDS,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    setup_requires=SETUP_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    # extras_require=EXTRAS_REQUIRE,
    zip_safe=True,  # the package can run out of an .egg file
    ext_modules=cythonize(
        [dl85_extension],
        compiler_directives={"language_level": "3"}
    )
)
