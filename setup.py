# Copyright (c) 2016-2019 CEA
#
# This software is governed by the CeCILL license under French law and
# abiding by the rules of distribution of free software. You can use,
# modify and/ or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# "http://www.cecill.info".
#
# As a counterpart to the access to the source code and rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty and the software's author, the holder of the
# economic rights, and the successive licensors have only limited
# liability.
#
# In this respect, the user's attention is drawn to the risks associated
# with loading, using, modifying and/or developing or reproducing the
# software by the user in light of its specific status of free software,
# that may mean that it is complicated to manipulate, and that also
# therefore means that it is reserved for developers and experienced
# professionals having in-depth computer knowledge. Users are therefore
# encouraged to load and test the software's suitability as regards their
# requirements in conditions enabling the security of their systems and/or
# data to be ensured and, more generally, to use and operate it in the
# same conditions as regards security.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.

from setuptools import setup
from cveda_databank import __version__
from imagen_databank import __author__
from cveda_databank import __email__
from cveda_databank import __license__


def readme():
    with open('README.rst') as f:
        return f.read()


def license():
    with open('LICENSE') as f:
        return f.read()


setup(
    name='cveda_databank',
    version=__version__,
    author=__author__,
    author_email=__email__,
    description='c-VEDA project databank software',
    long_description=readme(),
    license=__license__,
    url='https://github.com/cveda/cveda_databank',
    packages=['cveda_databank'],
    scripts=[
        'follow_up/cveda_follow_up_planning_2017.py',
        'follow_up/cveda_follow_up_planning_2018.py',
        'freeze/cveda_freeze_psytools.py',
        'mri/cveda_mri_deidentify.py',
        'psc/cveda_generate_psc1.py',
        'psc/cveda_generate_psc2.py',
        'psytools/cveda_psytools_download.py',
        'psytools/cveda_psytools_deidentify.py',
        'recruitment_files/cveda_recruitment_files.py',
    ],
    classifiers=[
        "License :: OSI Approved :: CEA CNRS Inria Logiciel Libre License, version 2.1 (CeCILL-2.1)",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Environment :: Console",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Utilities",
    ],
    install_requires=[
        'pydicom',
        'jellyfish',
        'openpyxl',
    ],
)
