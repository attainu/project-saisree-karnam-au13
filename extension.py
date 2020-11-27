import os

def by_extension():
    dir_path  = input("enter directory path :- ")
    if os.path.isdir(dir_path):
        return dir_path
    else:
        dir_path = by_extension()
        return dir_path

if __name__ == '__main__':
# for getting the directory path from the user.
   dir_p = by_extension() 
# to get all the file names from the given path
   all_files = os.listdir(dir_p)
   all_fext = [] # empty list, stores all folders that are to be created with extensions

# split all file extensions from the dir
   for f in all_files: # iterate through all files 
       _, fext = os.path.splitext(f) #splits extensions and file names
       if fext not in all_fext :
           all_fext.append(fext)
# create all dirs to organise files
   for ext in all_fext :
        if ext :
            os.mkdir(os.path.join(dir_p, ext)) # creates folders with ext names in path 

# move all files to their respective dirs
   for f in all_files:
	    _, ext = os.path.splitext(f)
	    old_path = os.path.join(dir_p, f)
	    new_path = os.path.join(dir_p, ext, f)
# move all folders with respective extensions
	    os.rename(old_path, new_path) 
print("Done! check folders")