import os, shutil

path = "text.txt"
try:
    os.remove(path)
    #os.rmdir(path)         # removes an empty dir
    #shutil.rmtree(path)    # removes a dir with everything that is inside

except FileNotFoundError:
    print("The file was not found")

except PermissionError:
    print("Access was denied")

except OSError:
    print("You cannot delete that using that function")
    
else:
    print(path + " was removed")