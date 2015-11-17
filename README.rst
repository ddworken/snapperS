========
snapperS
========

.. image:: https://badge.fury.io/py/snapperS.svg
    :target: https://badge.fury.io/py/snapperS

.. image:: https://travis-ci.org/ddworken/snapperS.svg?branch=master
    :target: https://travis-ci.org/ddworken/snapperS
    
A set of subcommands to supplement snapper usage. Tested on Ubuntu 15.04 and 15.10 with snapper v0.2.4 and btrfs-progs v4.0 (bug reports welcome!).

::
    
    usage: snapperS [-h] [-d DIRECTORY] [-v] {cat,backup,restore,rm,list} ...

    snapperS: A variety of supplemental snapper subcommands

    optional arguments:
      -h, --help            show this help message and exit
      -d DIRECTORY, --directory DIRECTORY
                            Directory containing the snapshots
      -v, --verbose         Enable verbose logging. If you are experiencing difficulties with this program, try with -v for debugging. 

    Subcommands:
      Restore a snapshot from a file generated with snapperS backup. 
      A more comprehensive version of snapper list that includes information on space usage. 
      Backup a specified snapshot to a file via btrfs send. 
      Delete a specified file from either a range of snapshots or from all snapshots. 
      Read a specified file from a specified snapshot. 

      {cat,backup,restore,rm,list}


Subcommands
------------

snapperS cat

::

    usage: snapperS cat [-h] -f ~/file.txt -s SNAPSHOT

    Read a specified file from a specified snapshot.

    optional arguments:
      -h, --help            show this help message and exit
      -f ~/file.txt, --filename ~/file.txt
                            The file to cat
      -s SNAPSHOT, --snapshot SNAPSHOT
                            The snapshot to view


snapperS rm

::

    usage: snapperS rm [-h] -f ~/largeFile.img [-r 1..42] [--recursive]

    Delete a specified file from either a range of snapshots or from all
    snapshots.

    optional arguments:
      -h, --help            show this help message and exit
      -f ~/largeFile.img, --filename ~/largeFile.img
                            Delete a file from all past snapshots.
      -r 1..42, --range 1..42
                            The range of snapshots to delete the file from in the
                            form of startPoint..endPoint (e.g. 2..5)
      --recursive           Delete recursively (i.e. a folder)
    

snapperS backup

::

    usage: snapperS backup [-h] -b ~/BTRFS_Backup.send -s 42
    
    Backup a specified snapshot to a file via btrfs send. It is recommended to compress this file.
        -In order to restore this file, run `cat backup | btrfs receive /mnt/subvol`
        -If you want to sync your backups to another BTRFS filesystem, ButterSink is better suited for that purpose. 
    
    optional arguments:
      -h, --help            show this help message and exit
      -b ~/BTRFS_Backup.send, --backup ~/BTRFS_Backup.send
                            The location to store the backup
      -s 42, --snapshot 42  The number of the snapshot you want to backup


snapperS restore

::

    usage: snapperS restore [-h] -b ~/BTRFS_Backup.send -r ~/newRestoredSubvolume/

    Restore a snapshot from a file generated with snapperS backup.

    optional arguments:
      -h, --help            show this help message and exit
      -b ~/BTRFS_Backup.send, --backup ~/BTRFS_Backup.send
                            The location of the backup.
      -r ~/newRestoredSubvolume/, --restoreLocation ~/newRestoredSubvolume/
                            The path to where you want to restore the backup.


snapperS list

::

    usage: snapperS list [-h]

    A more comprehensive version of snapper list that includes information on
    space usage.

    optional arguments:
      -h, --help  show this help message and exit


Installation
-------------

::

    pip install snapperS

or

::

    git clone https://github.com/ddworken/snapperS.git
    cd snapperS
    python setup.py install

Source
-------

Source is available on at github.com/ddworken/snapperS
