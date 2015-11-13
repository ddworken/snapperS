from distutils.core import setup

setup(
    name='snapperS',
    version='0.3.3',
    author='David Dworken',
    author_email='david@daviddworken.com',
    packages=['snapperS'],
    url='http://pypi.python.org/pypi/snapperS/',
    license='LICENSE.txt',
    description='A set of supplementary commands to be used with snapper',
    long_description=open('README.rst').read(),
    install_requires=[
        "argparse",
        "subprocess",
    ],
)

