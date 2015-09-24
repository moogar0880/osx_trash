osx_trash
=========
Easily move files to the trash on OS X from the commandline, or programatically.

CLI
---
The `osx_trash` package exposes a cli utility called `trash`.

```shell
usage: trash [-h] [-v] [--version] [src [src ...]]

positional arguments:
  src            A list of files and directories to move to the Trash.
                 Relative and absolute paths are both fine.

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Toggle verbose output
  --version      Print version info and exit
```

The `trash` utility can be used to specify a relative or absolute filepath to
move to the trash by simply running:

```shell
$ trash file1 file2 file3
```

API
---
The `osx_trash` package also exposes an API that you can use to programatically
move files to the trash on an OS X system.

```python
from osx_trash import trash

trash('my_file.txt')
```

For more advanced use-cases, you can also tap into the base classes of the
osx_trash API.

```python
from osx_trash import LocalTrash

# Delete a file stored locally on the filesystem
f = LocalTrash('my_file.txt')
f.delete()

from osx_trash import MountedTrash

# Delete a file stored on a mounted volume
f = MountedTrash('/Volumes/MyDrive/my_file.txt')
f.delete()
```

When running programatically, be careful of the `TrashException`'s that can be
raised.

* A `NoLocalTrash` Exception is raised if a user's .Trash directory can't be found.
* An `UnsupportedDiskFormat` is raised if the filepath can't be deduced. Ie, doesn't start with /Users or /Volumes
