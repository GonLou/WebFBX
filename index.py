import glob
from dominate import document
from dominate.tags import *

from xml.etree import ElementTree as et

import fbx
import FbxCommon
from PIL import Image
import sys

def DisplayControlsPoints(pMesh):
    lControlPointsCount = pMesh.GetControlPointsCount()
    lControlPoints = pMesh.GetControlPoints()

    print ("    Control Points")

    for i in range(lControlPointsCount):
        print("        Control Point %i" % i)
        print("            Coordinates: %s" % lControlPoints[i])

        for j in range(pMesh.GetLayerCount()):
            leNormals = pMesh.GetLayer(j).GetNormals()
            if leNormals:
                if leNormals.GetMappingMode() == fbx.FbxLayerElement.eByControlPoint:
                    header = "            Normal Vector (on layer %d): " % j
                    if leNormals.GetReferenceMode() == fbx.FbxLayerElement.eDirect:
                        print(header, leNormals.GetDirectArray().GetAt(i))
        print("")

#temporary variables
path = "C:\Python27\Scripts\WebFbx"
tmp_file_path = "files\cube.FBX";
#tmp_file_path = "files\bat.fbx";
#end temporary variables

########################################
#get files from FILES directory
########################################
found_files = glob.glob("files/*.fbx")
for found_file in found_files:
    print found_file
    #tmp_file_path = found_file #process each file in FBX SDK

########################################
#just doing one file to see how it goes, later will put it on function
########################################

#creating instance (acess to C++ SDK) with a custom name
manager = fbx.FbxManager.Create()
importer = fbx.FbxImporter.Create(manager, "myImporter")
status = importer.Initialize(tmp_file_path)

#check if file is ok for load
if status == False:
    print "WARNING: FbxImporter intialization failed"
    #print importer.GetError()
    sys.exit()

#import scene
scene = fbx.FbxScene.Create(manager, "myScene")
importer.Import(scene)
importer.Destroy()

#extract first node
node = scene.GetRootNode()
print("INFO: number of nodes = %i" % scene.GetNodeCount())
print("INFO: number of geometries = %i" % scene.GetGeometryCount())

for i in range(node.GetChildCount()):
    print("INFO: number of child from node = %i" % node.GetChildCount())
    child = node.GetChild(i)

    if child.GetNodeAttribute().GetAttributeType() == fbx.FbxNodeAttribute.eMesh:
        print("INFO: child = %s" % child)
        mesh = child.GetNodeAttribute()
        #i = lmesh.GetControlPointsCount()
        DisplayControlsPoints(mesh)



#NEW NEW NEW
# mySdkManager, myScene = FbxCommon.InitializeSdkObjects()
# myResult = FbxCommon.LoadScene(mySdkManager, myScene, tmp_file_path)

sceneInfo = scene.GetSceneInfo()
if sceneInfo:
    print("INFO: Title = %s" % sceneInfo.mTitle.Buffer())
    print("INFO: Subject = %s" % sceneInfo.mSubject.Buffer())
    print("INFO: Author = %s" % sceneInfo.mAuthor.Buffer())
    print("INFO: Keywords = %s" % sceneInfo.mKeywords.Buffer())
    print("INFO: Revision = %s" % sceneInfo.mRevision.Buffer())
    print("INFO: Comment = %s" % sceneInfo.mComment.Buffer())

    thumbnail = sceneInfo.GetSceneThumbnail()
    if thumbnail:
        print("INFO: Thumbnail = yes")
    else:
        print("INFO: Thumbnail = no")
else:
    print ("WARNING: no model information")

# if node:
#     for i in range(node.GetChildCount()):
#         node.GetChild(i)
#         mesh = node.GetNodeAttribute ()
#         if mesh == None:
#             print("WARNING: NULL Node Attribute\n")
#         else:
#             #lAttributeType = (pNode.GetNodeAttribute().GetAttributeType())
#             #if myNode.GetNodeAttribute().GetAttributeType() == FbxNodeAttribute.eMesh:
#             DisplayControlsPoints(mesh)

# END NEW END NEW

########################################
# render to image
########################################
# create an SVG XML element
doc = et.Element('svg', width='150', height='150', version='1.1', xmlns='http://www.w3.org/2000/svg')
# add a circle (using the SubElement function)
et.SubElement(doc, 'circle', cx='75', cy='75', r='70', fill='rgb(20, 255, 177)')
# add text
text = et.Element('text', x='75', y='75', fill='white', style='font-family:Courier;font-size:18px;text-anchor:middle;dominant-baseline:top')
text.text = 'no image'
doc.append(text)
# ElementTree 1.2 doesn't write the SVG file header errata, so do that manually
f = open('thumbnails/sample.svg', 'w')
f.write('<?xml version=\"1.0\" standalone=\"no\"?>\n')
f.write('<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\"\n')
f.write('\"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\n')
f.write(et.tostring(doc))
f.close()

########################################
#shows up in HTML page reading it from thumbnails directory
########################################
thumbs = glob.glob('thumbnails/*.svg')

with document(title='Thumbnails') as doc:
    h1('Thumbnails')
    for path in thumbs:
        #<svg height="150" version="1.1" width="150" xmlns="http://www.w3.org/2000/svg"><circle cx="75" cy="75" fill="rgb(20, 255, 177)" r="70" /><text fill="white" style="font-family:Courier;font-size:18px;text-anchor:middle;dominant-baseline:top" x="75" y="75">no image</text></svg>
        div(img(src=path), _class='thumbnails')

with open('gallery.html', 'w') as f:
    f.write(doc.render())
