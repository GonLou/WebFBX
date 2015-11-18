import glob

#get files from FILES directory
found_files = glob.glob("files/*.fbx")
for found_file in found_files:
    print found_file

#process each file in FBX SDK