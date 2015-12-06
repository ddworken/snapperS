from distutils.core import setup

setup(
    name='snapperS',
    version='1.1.8',
    author='David Dworken',
    author_email='david@daviddworken.com',
    packages=['snapperS'],
    url='http://pypi.python.org/pypi/snapperS/',
    license='LICENSE.txt',
    description='A set of supplementary commands to be used with snapper',
    long_description=open('README.rst').read(),
    scripts=['snapperS/snapperS'],
    install_requires=[
        "argparse",
        "tabulate",
    ],
)
