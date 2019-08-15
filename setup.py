"""The setup script for installing the package."""
from setuptools import setup, find_packages, Extension
from distutils.core import setup, Extension

# read the contents of the README
with open('README.md') as README_md:
    README = README_md.read()

setup(
    name='gym_contra',
    version='0.0.5',
    description='Contra. for OpenAI Gym',
    keywords=' '.join([
        'OpenAI-Gym',
        'NES',
        'Contra',
        'Reinforcement-Learning-Environment',
    ]),
    classifiers=[
        'License :: Free For Educational Use',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Games/Entertainment :: Side-Scrolling/Arcade Games',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    url='https://github.com/OuYanghaoyue/gym_contra',
    author='OuYanghaoyue',
    author_email='tony1480087241@gmail.com',
    long_description=README,
    long_description_content_type="text/markdown",
    license='Proprietary',
    packages=find_packages(exclude=['tests', '*.tests', '*.tests.*']),
    package_data={'Contra': ['ROMs/*.nes']},
    install_requires=['nes-py>=8.0.0'],

)
