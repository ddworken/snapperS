========
snapperS
========

.. image:: https://badge.fury.io/py/snapperS.svg
    :target: https://badge.fury.io/py/snapperS

.. image:: https://travis-ci.org/ddworken/snapperS.svg?branch=master
    :target: https://travis-ci.org/ddworken/snapperS
    
A set of subcommands to supplement snapper usage. Tested only on Ubuntu 15.10 (bug reports welcome!). 

::

    usage: snapperS [-h] [-d DIRECTORY] {cat,delete} ...
    
    snapperS: A variety of supplemental snapper subcommands
    
    optional arguments:
      -h, --help            show this help message and exit
      -d DIRECTORY, --directory DIRECTORY
                            Directory containing the snapshots
    
    subcommands:
      cat to run cat on a file from a specific snapshot. 
      delete to delete files from either all snapshots or a range of snapshots. 
    
      {cat,delete}


Subcommands
------------
::

    usage: snapperS cat [-h] -f FILENAME -s SNAPSHOT

    optional arguments:
      -h, --help            show this help message and exit
      -f FILENAME, --filename FILENAME
                            The file to cat
      -s SNAPSHOT, --snapshot SNAPSHOT
                            The snapshot to view



::

    usage: snapperS delete [-h] -f FILENAME [-r RANGE] [--recursive]
    
    optional arguments:
      -h, --help            show this help message and exit
      -f FILENAME, --filename FILENAME
                            Delete a file from all past snapshots.
      -r RANGE, --range RANGE
                            The range of snapshots to delete the file from in the
                            form of startPoint..endPoint (e.g. 2..5)
      --recursive           Delete recursively (i.e. a folder)
    

Installation
-------------

::

    pip install snapperS

or

::

    git clone https://github.com/ddworken/snapperS.git
    cd snapperS
    python setup.py install
