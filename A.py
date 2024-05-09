# A.py
import update_importpaths
from sub import B, C
# importing 'C' would normally fail


if __name__ == "__main__":
    print("running A")
    B.PrintB()
    C.PrintC()
