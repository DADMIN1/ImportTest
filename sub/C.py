# sub/C.py
# this import statement would normally fail when importing C into A
from B import PrintB


def PrintC():
    print("PrintC")
    print("printing B from C: ")
    PrintB()


if __name__ == "__main__":
    print("running C")
    PrintC()
