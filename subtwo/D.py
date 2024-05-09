# subtwo/D.py

print("importing from /subtwo/D.py")
# if this fails, you need to run update_importpaths to create the symlink
import update_importpaths

# importing from sibling folder!
from B import PrintB


def PrintD():
    print("PrintD")
    print("printing B from D: ")
    PrintB()


if __name__ == "__main__":
    print("running D")
    PrintD()

