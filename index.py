import glob
from dominate import document
from dominate.tags import *

from xml.etree import ElementTree as et

import fbx
import FbxCommon
from PIL import Image
import sys

########################################
# isolate name of the file without extension and folder
########################################
def SliceFileName(s1):
    s2 = "\\"
    return s1[s1.index(s2) + len(s2):len(s1)-4]

########################################
# render to image
# create an empty SVG XML element
########################################
def DrawEmptySVG(fileName):
    # create an empty SVG XML element
    doc = et.Element('svg', width='150', height='150', version='1.1', xmlns='http://www.w3.org/2000/svg')
    # add a circle (using the SubElement function)
    et.SubElement(doc, 'circle', cx='75', cy='75', r='70', fill='rgb(20, 255, 177)')
    # add text
    text = et.Element('text', x='75', y='75', fill='white', style='font-family:Courier;font-size:18px;text-anchor:middle;dominant-baseline:top')
    text.text = 'no image'
    doc.append(text)
    # ElementTree 1.2 doesn't write the SVG file header errata, so do that manually
    f = open('thumbnails/'+fileName+'.svg', 'w')
    f.write('<?xml version=\"1.0\" standalone=\"no\"?>\n')
    f.write('<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\"\n')
    f.write('\"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\n')
    f.write(et.tostring(doc))
    f.close()

########################################
# render to image
# create an SVG XML element
########################################
def DrawSVG(SVGline, fileName):
    f = open('thumbnails/'+fileName+'.svg', 'w')
    f.write('<?xml version=\"1.0\" standalone=\"no\"?>\n')
    f.write('<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\"\n')
    f.write('\"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\n')
    f.write('<svg height=\"150\" version=\"1.1\" width=\"150\" xmlns=\"http://www.w3.org/2000/svg\">\n')
    f.write('<polygon points=\"'+SVGline+'\" style=\"fill:none; stroke:#00C; stroke-width:1.5px\"/>\n')
    f.write('</svg>')
    f.close()

########################################
# extract vectors
########################################
def DisplayControlsPoints(pMesh):
    lControlPointsCount = pMesh.GetControlPointsCount()
    lControlPoints = pMesh.GetControlPoints()
    zoom = 0.5
    #print ("    Control Points")
    SVGline = ""
    for i in range(lControlPointsCount):
        #print("        Control Point %i" % i)
        #print("            Coordinates X: %s" % lControlPoints[i][0])
        #print("            Coordinates Y: %s" % lControlPoints[i][1])
        #print("            Coordinates Z: %s" % lControlPoints[i][2])
        if i < lControlPointsCount-1 :
            #SVGline = SVGline + str(lControlPoints[i][0]/lControlPoints[i][2]) + "," + str(lControlPoints[i][1]/lControlPoints[i][3]) + ","
            if lControlPoints[i][3] > 0:
                SVGline = SVGline + str(lControlPoints[i][0]/lControlPoints[i][2]*zoom) + "," + str(lControlPoints[i][1]/lControlPoints[i][3]*zoom) + ","
            else:
                SVGline = SVGline + str(lControlPoints[i][0]*zoom) + "," + str(lControlPoints[i][1]*zoom) + ","

    return SVGline[:-1]

########################################
# just doing one file to see how it goes, later will put it on function
########################################
def ImportModel(filePath):
    #creating instance (acess to C++ SDK) with a custom name
    manager = fbx.FbxManager.Create()
    importer = fbx.FbxImporter.Create(manager, "myImporter")
    status = importer.Initialize(filePath)

    #check if file is ok for load
    if status == False:
        print "WARNING: FbxImporter intialization failed"
        DrawEmptySVG(SliceFileName(filePath))
        return 0
        #sys.exit()

    #import scene
    scene = fbx.FbxScene.Create(manager, "myScene")
    importer.Import(scene)
    importer.Destroy()
    print "model OK"
    #extract first node
    node = scene.GetRootNode()
    #print("INFO: number of nodes = %i" % scene.GetNodeCount())
    #print("INFO: number of geometries = %i" % scene.GetGeometryCount())

    for i in range(node.GetChildCount()):
        #print("INFO: number of child from node = %i" % node.GetChildCount())
        child = node.GetChild(i)

        if child.GetNodeAttribute().GetAttributeType() == fbx.FbxNodeAttribute.eMesh:
            #print("INFO: child = %s" % child)
            mesh = child.GetNodeAttribute()
            SVGline = DisplayControlsPoints(mesh)

    # General file information
    sceneInfo = scene.GetSceneInfo()
    if sceneInfo:
        #print("INFO: Title = %s" % sceneInfo.mTitle.Buffer())
        #print("INFO: Subject = %s" % sceneInfo.mSubject.Buffer())
        #print("INFO: Author = %s" % sceneInfo.mAuthor.Buffer())
        #print("INFO: Keywords = %s" % sceneInfo.mKeywords.Buffer())
        #print("INFO: Revision = %s" % sceneInfo.mRevision.Buffer())
        #print("INFO: Comment = %s" % sceneInfo.mComment.Buffer())

        thumbnail = sceneInfo.GetSceneThumbnail()
        if thumbnail:
            print("INFO: Thumbnail = yes")
        else:
            print("INFO: Thumbnail = no")
    else:
        print ("WARNING: no model information")

    #render to image
    DrawSVG(SVGline, SliceFileName(filePath))
    return 1

########################################
#shows up in HTML page reading it from thumbnails directory
########################################
def CreateHTML():
    thumbs = glob.glob('thumbnails/*.svg')
    with document(title='Web Fbx Thumbnails') as doc:
        h1('Thumbnails')
        with table().add(tbody()):
            lh = tr()
            lh.add(td('Title', style="width:20%"))
            lh.add(td('File Name', style="width:40%"))
            lh.add(td('Image', style="width:40%"))
            i = 0
            for path in thumbs:
                l = tr()
                with l:
                    l.add(td(SliceFileName(path)))
                    l.add(td(path))
                    l.add(td(img(src=path)))
                i=i+1

    with open('gallery.html', 'w') as f:
        f.write(doc.render())

#temporary variables
#path = "C:\Python27\Scripts\WebFbx"
#/C:/Python27/Scripts/WebFbx/thumbnails/sample.svg
#tmp_file_path = "files\cube.FBX";
#tmp_file_path = "files\bat.fbx";
#end temporary variables

#process each FBX file in FILES directory
found_files = glob.glob("files/*.fbx")
for found_file in found_files:
    print "%s" % found_file
    ImportModel(found_file) #process each file in FBX SDK

#shows up in HTML page reading it from thumbnails directory
CreateHTML()
