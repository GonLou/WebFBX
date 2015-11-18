import glob

import fbx
import Image
import sys

path = "C:\Python27\Scripts\WebFbx"
tmp_file_path = "files\PG.FBX";

#get files from FILES directory
found_files = glob.glob("files/*.fbx")
for found_file in found_files:
    print found_file
    #tmp_file_path = found_file #process each file in FBX SDK

#just doing one file to see how it goes, later will put it on function

#creating instance (acess to C++ SDK) with a custom name
manager = fbx.FbxManager.Create()
importer = fbx.FbxImporter.Create(manager, "myImporter")
status = importer.Initialize(tmp_file_path)

#check if file is ok for load
if status == False:
    print "WARNING! FbxImporter intialization failed"
    #print importer.GetError()
    sys.exit()

#import scene
scene = fbx.FbxScene.Create(manager, "myScene")
importer.Import(scene)
importer.Destroy()

#extract first node
node = scene.GetRootNode()
print("%s" % node.GetNodeAttribute())
for i in range(node.GetChildCount()):
    child = node.GetChild(i)
    attr_type = child.GetNodeAttribute().GetAttributeType()

    if attr_type == fbx.FbxNodeAttribute.eMesh:
        print(child)

#render to image

#shows up in HTML page