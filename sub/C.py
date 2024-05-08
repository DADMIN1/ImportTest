# sub/C.py
from B import PrintB
# import B.PrintB

def PrintC():
    print("PrintC")
    print("printing B from C: ")
    PrintB()


if __name__ == "__main__":
    print("running C")
    PrintC()
