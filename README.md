# **Overcoming Python's Import System**
### because working around it
### is easier than working with it...

## Usage:
#### The main file is "update_importpaths.py"
Running "update_importpaths" does two things:
1) Print the updated paths
2) Create symlinks, if any are missing


All other files are examples/tests. \
All examples can be run from any working-directory. \
Examples D and E will require you to run "update_importpaths" once beforehand.


## Incorporating into other projects:
1) Copy "update_importpaths.py" into the top-level directory.
2) Rewrite the variables: "toplevel\_name", "subdir\_names", and "symlink_into".
3) Run "update_importpaths" to create any symlinks and to check that the updated paths are correct.

Then simply import "update_importpaths" wherever needed; it will make everything else available for import.
