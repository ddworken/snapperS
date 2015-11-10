# snapperS

A set of subcommands to supplement snapper. 

```
usage: snapperS [-h] {cat,delete} ...

snapperS: A variety of supplemental snapper subcommands

optional arguments:
  -h, --help    show this help message and exit

subcommands:
  Different Subcommands

  {cat,delete}  additional help
```

```
usage: snapperS cat [-h] -f FILENAME -s SNAPSHOT

optional arguments:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        The file to cat
  -s SNAPSHOT, --snapshot SNAPSHOT
                        The snapshot to view
```

```
usage: snapperS delete [-h] [-f FILENAME]

optional arguments:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        Delete a file from all past snapshots.
```
