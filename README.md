# WebFBX
## HTML generated thumbnails page from FBX models

### Introduction
Build a webpage that displays thumbnails of a directory full of FBX files.
This project is intended to use Python and FBX SDK.
This project contains two folders thumbnails and files. The first one will hold .svg files and the second one FBX files to be processed.
#### Python
Python is a scripting language widely used in investigation.
Easy to use due its high-level language have a large and comprehensive standard library and puts it emphasis in readability.
#### FBX
FBX file format permits to exchange 3d assets across other Autodesk products as 3D Studio Max, Maya, ...
Nowadays with wide-spreading of this format type more applications are using it.
With FBX SDK is possible to import, modify, export all elements on the scene in your game, databases, web application and others.
#### Isometric projection
Isometric projection is a type of pictorial projection in which the three dimensions of a solid are not only shown in one view, but their actual sizes can be measured directly from it.
#### SVG
Created by the World Wide Web Consortium (W3C), the SVG extension is a two-dimensional vector graphic format file . It is a standard format to display vector graphics on the web, and its internal organization is based on XML text format.

### Preparation
#### Python
Python 2.7 was already installed under Anaconda package.
Some Python libraries were installed to ease some app aspects like webpage generation, folder access and SVG file creation.
###### Glob module
Glob module retrieves pathnames according to a specific pattern matching rules as Unix shell.
This was very useful to obtain all files in files and thumbnails folder.
###### Dominate library
Dominate creates and manipulates a HTML document threw its DOM API easy to use.
This was used to create final html file gallery.html .
###### Element type
Flexible container object, designed to store hierarchical data structures as a list and/or a dictionary.
Provided an useful way to create new sub-elements for a given element when creating SVG file.
#### FBX
After downloading FBX SDK from Autodesk website, downloaded file is installed.
Then is needed to go <your programs folder>/FBX/FBX Python SDK/<your version>/lib/<your Python version> copy three existing files and paste them into <your Python folder>/Lib/site-packages.
#### Text Editor
It was used Atom 1.3.2 for its simplicity.

### Development
#### FBX

#### Files

#### Isometric

#### HTML

### Conclusion

## Internet Resources
- https://docs.python.org/2/library/glob.html
- https://docs.python.org/2/library/xml.etree.elementtree.html
- https://pypi.python.org/pypi/dominate
- http://nick.onetwenty.org/index.php/2010/04/07/creating-svg-files-with-python/
- http://tecfaetu.unige.ch/staf/staf-k/borer/stic3/SVG/TMs-SVG-Codebook.pdf
- https://www.safaribooksonline.com/library/view/programming-python-4th/9781449398712/ch01s08.html
- https://pypi.python.org/pypi/dominate
- https://en.wikipedia.org/wiki/Isometric_projection

**Goncalo Lourenco**  
November/December 2015
