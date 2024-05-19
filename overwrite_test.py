# this script sets up files in 'subthree' to test handling of pre-existing files
from update_importpaths import *
import shutil

# injecting name into the global lists for 'CreateSymlinks()'
testdir_name = "subthree" 
for listref in (subdir_names, symlink_into):
    #if testdir_name not in listref: listref.append(testdir_name)
    listref.clear()
    listref.append("subthree")

testdir = FindToplevelPath() / testdir_name
testdir.mkdir(exist_ok=True)
# Update_ImportPaths(onlyGood=True)  # returns only the 'subthree' path, but throws if it doesn't exist


def ClearTestdir():
    if not testdir.exists(): return
    print(f"WIPING '{testdir}'")
    shutil.rmtree(testdir)
    testdir.mkdir()
    return


def SetupTestdir(nonsymlink=False, createbroken=False):
    print("\n Resetting testdir... \n")
    ClearTestdir()
    # testdir must be recreated before calling CreateSymLinks
    if nonsymlink:
        nonsymlink_file = testdir / "update_importpaths.py"
        nonsymlink_file.write_text("this file is not a symlink!\n")
        return
    elif createbroken:
        pass # TODO: handle
    newlinks = CreateSymlinks()
    return


if __name__ == "__main__":
    print("\n testing overwrite-behavior \n")
    
    # TODO: generate all possible configurations/combinations
    # TODO: create a nested subdir for each combination
    SetupTestdir()
    print(CreateSymlinks(report_existing=True, overwrite=False))
    print(CreateSymlinks(report_existing=False, overwrite=False))
    print(CreateSymlinks(report_existing=True, overwrite=True))
    
    SetupTestdir(nonsymlink=True)
    print(CreateSymlinks(report_existing=True, overwrite=False))
    print(CreateSymlinks(report_existing=True, overwrite=True))
    
    print("\n end test \n")
