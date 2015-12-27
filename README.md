# WebFBX
##### HTML generated thumbnails page from FBX models

### 1. Introduction
Build a webpage that displays thumbnails of a directory full of FBX files.
This project is intended to use Python and FBX SDK.
This project contains two folders thumbnails and files. The first one will hold .svg files and the second one FBX files to be processed.
#### 1.i) Python
Python is a scripting language widely used in investigation.
Easy to use due its high-level language have a large and comprehensive standard library and puts it emphasis in readability.
#### 1.ii) FBX
FBX file format permits to exchange 3d assets across other Autodesk products as 3D Studio Max, Maya, ...
Nowadays with wide-spreading of this format type more applications are using it.
With FBX SDK is possible to import, modify, export all elements on the scene in your game, databases, web application and others.
#### 1.iii) Isometric projection
Isometric projection is a type of pictorial projection in which the three dimensions of a solid are not only shown in one view, but their actual sizes can be measured directly from it.
#### 1.iv) SVG
Created by the World Wide Web Consortium (W3C), the SVG extension is a two-dimensional vector graphic format file . It is a standard format to display vector graphics on the web, and its internal organization is based on XML text format.

### 2. Preparation
#### 2.i) Python
Python 2.7 was already installed under Anaconda package.
Some Python libraries were installed to ease some app aspects like webpage generation, folder access and SVG file creation.
###### 2.i.1) Glob module
Glob module retrieves pathnames according to a specific pattern matching rules as Unix shell.
This was very useful to obtain all files in files and thumbnails folder.
###### 2.i.2) Dominate library
Dominate creates and manipulates a HTML document threw its DOM API easy to use.
This was used to create final html file gallery.html .
###### 2.i.3) Element type
Flexible container object, designed to store hierarchical data structures as a list and/or a dictionary.
Provided an useful way to create new sub-elements for a given element when creating SVG file.
#### 2.ii) FBX
After downloading FBX SDK from Autodesk website, downloaded file is installed.
Then is needed to go <your programs folder>/FBX/FBX Python SDK/<your version>/lib/<your Python version> copy three existing files and paste them into <your Python folder>/Lib/site-packages.
#### 2.iii) Text Editor
It was used Atom 1.3.2 for its simplicity.

### 3. Development
#### 3.i) Files
First thing is to read files from folder. Because just FBX files are valid for later import they are automatically filtered with Glob module.
#### 3.ii) FBX
As each file is loaded from folder is created an instance with a custom name.
During the process is checked if file is a valid FBX file. If not a SVG file saying "no image" with a green circle will be attributed to that invalid FBX file.
For valid formats is possible to get some useful general file information like title, subject, author, keywords,... But for this project purpose just get the node.
That node represents the first model in the scene from which will be an image displayed.
To retrieve all coordinates we access GetControlPoints function from FBX SDK.
At same time theses points are being converted into SVG lines after isometric transformation.
#### 3.iii) Isometric
To obtain an isometric view of the model is needed to perform a rotation in Euclidean space so it reflects same scale along each projection axis.
Actually isometric projection is a result from two rotations: first rotate on x for 45 degrees and second rotate on y for arctan(1/sqrt(2)).
This operations is achievable by RotatingMatrix function that performs all math calculus. MatrixDotMatrix function helps doing the cross product between matrices.
Only after this transformation is possible to convert our 3d coordinates into a 2D image.
All data retrieved from FBX file are 3d coordinates and is needed to plot it into a 2D image.
The easiest way to plot 3D Points onto a 2D image is by following formula screen.x = x / z and screen.y = y / z . This will produce the image coordinates of the 3D point.
Zoom is a way to hack size of model but because models are from different sizes a constant number cannot achieve good results for every models.
Center was another naif way to hack negative values that was drawing lines outside visible image square. This solution is not working properly due its simple implementation and complex difference between models.
#### 3.iv) SVG
All 2d points obtained are processed in a single SVG line using polygon attribute.
Remaining tags are standard for a SVG file.
In case of an invalid FBX file or by some reason it can not be read DrawEmptySVG function will create an alternative SVG image.
#### 3.v) HTML
To create HTML Glob module is used once more for this time read all SVG files previously created.
After reading all files Dominate library is used to generate a HTML page.
Thumbnails HTML page composition is quite simple, using a table with three columns, then each row will display name, file path and correspondent model image.

### 4. Conclusion
Python allowed a fast implementation of different application aspects like reading folders and creating webpage.
But FBX SDK is very poorly studied and even Autodesk own information about it is very scarce.
Isometric approach need be different in the way to capture all model to fit in image. Could be used a way to verify maximum/minimum XY points on top, left, right and bottom, and from there scale it to image dimensions.
Also application is running locally, mainly because Virtual Machine evaluation on Google Developers Console was expired already since it was setup on early term.
Never the less this type of applications are very useful in a game development process because give a lot of flexibility and future ideas to transform models via programming and afterwards upload them into game.

### 5. Internet Resources
- http://docs.autodesk.com/FBX/2014/ENU/FBX-SDK-Documentation/index.html
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
