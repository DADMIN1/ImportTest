# A.py
import update_importpaths

# works with "PYTHONPATH=sub" on cmdline
from sub import B, C

if __name__ == "__main__":
    print("running A")
    B.PrintB()
    C.PrintC()
