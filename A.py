# A.py
import update_importpaths

from sub import B, C

# if this fails, you need to run "update_importpaths" to create the symlink
from subtwo import D


if __name__ == "__main__":
    print("running A")
    B.PrintB()
    C.PrintC()
    D.PrintD()
