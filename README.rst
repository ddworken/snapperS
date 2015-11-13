========
snapperS
========

.. image:: https://badge.fury.io/py/snapperS.svg
    :target: https://badge.fury.io/py/snapperS

.. image:: https://travis-ci.org/ddworken/snapperS.svg?branch=master
    :target: https://travis-ci.org/ddworken/snapperS
    
A set of subcommands to supplement snapper usage. Tested on Ubuntu 15.04 and 15.10 with snapper v0.2.4 and btrfs-progs v4.0 (bug reports welcome!). 

::
    
    usage: snapperS [-h] [-d DIRECTORY] [-v] {cat,backup,delete} ...

    snapperS: A variety of supplemental snapper subcommands

    optional arguments:
      -h, --help            show this help message and exit
      -d DIRECTORY, --directory DIRECTORY
                            Directory containing the snapshots
      -v, --verbose         Enable verbose logging. If you are experiencing difficulties with this program, try with -v for debugging. 

    Subcommands:
      Delete a specified file from either a range of snapshots or from all snapshots. 
      Backup a specified snapshot to a file via btrfs send.
      Read a specified file from a specified snapshot. 

      {cat,backup,delete}



Subcommands
------------

snapperS cat

::

    usage: snapperS cat [-h] -f FILENAME -s SNAPSHOT

    Read a specified file from a specified snapshot.

    optional arguments:
      -h, --help            show this help message and exit
      -f FILENAME, --filename FILENAME
                            The file to cat
      -s SNAPSHOT, --snapshot SNAPSHOT
                            The snapshot to view


snapperS delete

::

    usage: snapperS delete [-h] -f FILENAME [-r RANGE] [--recursive]

    Delete a specified file from either a range of snapshots or from all
    snapshots.

    optional arguments:
      -h, --help            show this help message and exit
      -f FILENAME, --filename FILENAME
                            Delete a file from all past snapshots.
      -r RANGE, --range RANGE
                            The range of snapshots to delete the file from in the
                            form of startPoint..endPoint (e.g. 2..5)
      --recursive           Delete recursively (i.e. a folder)
    

snapperS backup

::

    usage: snapperS backup [-h] [-b BACKUP] [-s SNAPSHOT]

    Backup a specified snapshot to a file via btrfs send.It is recommended to compress this file.
      -In order to restore this file, run `cat backup | btrfs receive /mnt/subvol`

    optional arguments:
      -h, --help            show this help message and exit
      -b BACKUP, --backup BACKUP
                            The location to store the backup
      -s SNAPSHOT, --snapshot SNAPSHOT
                            The number of the snapshot you want to backup


snapperS restore

::

    usage: snapperS restore [-h] [-b BACKUP] [-r RESTORELOCATION]

    Restore a snapshot from a file generated with snapperS backup.

    optional arguments:
      -h, --help            show this help message and exit
      -b BACKUP, --backup BACKUP
                            The location of the backup.
      -r RESTORELOCATION, --restoreLocation RESTORELOCATION
                            The path to where you want to restore the backup.


Installation
-------------

::

    pip install snapperS

or

::

    git clone https://github.com/ddworken/snapperS.git
    cd snapperS
    python setup.py install

