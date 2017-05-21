from setuptools import setup
import os.path

__version__ = '1.3.3'

descr_file = os.path.join(os.path.dirname(__file__), 'README.rst')

setup(
    name='riotwatcher',
    version=__version__,
    
    packages=['riotwatcher'],

    description='RiotWatcher is a thin wrapper on top of the Riot Games API for League of Legends.',
    long_description=open(descr_file).read(),
    author='Original - AG Stephan, New - MD Sangster',
    url='https://github.com/CogWorks/Riot-Watcher',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
        'Topic :: Games/Entertainment :: Real Time Strategy',
        'Topic :: Games/Entertainment :: Role-Playing'
    ],
    license='MIT',
    install_requires=[
        'requests'
    ],
 )
