# -*- coding: utf-8 -*-

###
### This file is generated automatically by SALOME v7.8.0 with dump python functionality
###

import os
import sys
import salome
theStudy = salome.myStudy

import salome_notebook
notebook = salome_notebook.NoteBook(theStudy)

dirPath = r'/home/joseph/dropbox/ME/caldera/vesselHerman/'
sys.path.insert( 0, dirPath)
dirPathCase = dirPath + 'case000/'
if not os.path.exists(dirPathCase):
    os.makedirs(dirPathCase)

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS

### Inputs
hVessel = 10.0
dVessel = 6.0
dBlastTube = .300
dVent = 0.508
dSlurry = 0.4
hSlurry = 3.5
dBlock = 0.812

### Calculated
hBlastTube = dVessel/4.0 + 0.3
rSlurry = dSlurry/2.0
rVessel = dVessel/2.0
rVent = dVent/2.0
rBlastTube = dBlastTube/2.0
lengthSlurryExit = dVessel/2.0 + dSlurry
hVent = dVessel/4.0*1.2
boxSide = dVessel*1.5
boxTranslate = -boxSide/2.0
rBlock = dBlock/2.0

geompy = geomBuilder.New(theStudy)

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
vesselCylinder = geompy.MakeCylinderRH(rVessel, hVessel)
Sphere_1 = geompy.MakeSphereR(rVessel)
Scale_1 = geompy.MakeScaleAlongAxes(Sphere_1, None, 1, 1, 0.5)
Box_1 = geompy.MakeBoxDXDYDZ(boxSide,boxSide,boxSide)
geompy.TranslateDXDYDZ(Box_1, boxTranslate, boxTranslate, 0)
vesselBottom = geompy.MakeCutList(Scale_1, [Box_1], True)
[vesssleBottomCap,Face_14] = geompy.ExtractShapes(vesselBottom, geompy.ShapeType["FACE"], True)
vesselTop = geompy.MakeMirrorByPoint(vesselBottom, O)
geompy.TranslateDXDYDZ(vesselTop, 0, 0, hVessel)
slurryOutlet = geompy.MakeCylinderRH(rSlurry, lengthSlurryExit)
geompy.TranslateDXDYDZ(slurryOutlet, 0, 0, hSlurry)
geompy.TranslateDXDYDZ(slurryOutlet, 0, 0, -hSlurry)
geompy.Rotate(slurryOutlet, OY, -90*math.pi/180.0)
geompy.TranslateDXDYDZ(OY, 0, 0, hSlurry)
geompy.TranslateDXDYDZ(slurryOutlet, 0, 0, hSlurry)
geompy.TranslateDXDYDZ(O, 0, 0, -hSlurry)
Cylinder_1 = geompy.MakeCylinderRH(rVent, hVent)
geompy.TranslateDXDYDZ(OX, 0, 0, -hSlurry)
geompy.TranslateDXDYDZ(OY, 0, 0, -hSlurry)
geompy.TranslateDXDYDZ(OZ, 0, 0, -hSlurry)
Rotation_1 = geompy.MakeRotation(Cylinder_1, OY, -25*math.pi/180.0)
geompy.TranslateDXDYDZ(O, 0, 0, hSlurry)
geompy.TranslateDXDYDZ(OX, 0, 0, hSlurry)
geompy.TranslateDXDYDZ(OZ, 0, 0, hSlurry)
geompy.Rotate(Rotation_1, OY, 5*math.pi/180.0)
geompy.Rotate(Rotation_1, OY, 5*math.pi/180.0)
geompy.Rotate(Rotation_1, OY, -3*math.pi/180.0)
geompy.Rotate(Rotation_1, OY, -2*math.pi/180.0)
geompy.TranslateDXDYDZ(Rotation_1, -dVessel/4.0, 0, hVessel)
Cut_1slurry = geompy.MakeCutList(slurryOutlet, [vesselCylinder], True)
[slurryExit,slurryExitWall,Face_15] = geompy.ExtractShapes(Cut_1slurry, geompy.ShapeType["FACE"], True)
Cut_1vent = geompy.MakeCutList(Rotation_1, [vesselTop], True)
[vent,ventSideWall,Face_7,Face_8,Face_9,Face_10,Face_11] = geompy.ExtractShapes(Cut_1vent, geompy.ShapeType["FACE"], True)
Cut_1 = geompy.MakeCutList(vesselTop, [Cut_1vent], True)
[geomObj_1,geomObj_2,geomObj_3,geomObj_4,geomObj_5] = geompy.ExtractShapes(Cut_1, geompy.ShapeType["FACE"], True)
[Face_1,Face_2,Face_3,Face_4,vesseltopFace] = geompy.ExtractShapes(Cut_1, geompy.ShapeType["FACE"], True)
cylindervessle = geompy.MakeCutList(vesselCylinder, [Cut_1slurry], True)
[Face_5,Face_6,vesselCylinderWall,Face_13] = geompy.ExtractShapes(cylindervessle, geompy.ShapeType["FACE"], True)
Cylinder_2 = geompy.MakeCylinderRH(rBlock,rBlock)
geompy.TranslateDXDYDZ(Cylinder_2, 0, 0, -dVessel/4.0)
Cut_2 = geompy.MakeCutList(Cylinder_2, [vesselBottom], True)
block = geompy.MakeCutList(Cylinder_2, [Cut_2], True)
vessel = geompy.MakePartition([vesssleBottomCap, slurryExitWall, ventSideWall, vesseltopFace, vesselCylinderWall], [], [], [], geompy.ShapeType["FACE"], 0, [], 0)
Cylinder_3 = geompy.MakeCylinderRH(rBlastTube, hBlastTube)
geompy.TranslateDXDYDZ(Cylinder_3, 0, 0, hVessel-0.300)
[inlet,inletPipe,Face_17] = geompy.ExtractShapes(Cylinder_3, geompy.ShapeType["FACE"], True)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( vesselCylinder, 'vesselCylinder' )
geompy.addToStudy( Sphere_1, 'Sphere_1' )
geompy.addToStudy( Scale_1, 'Scale_1' )
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudy( vesselBottom, 'vesselBottom' )
geompy.addToStudyInFather( vesselBottom, vesssleBottomCap, 'vesssleBottomCap' )
geompy.addToStudyInFather( vesselBottom, Face_14, 'Face_14' )
geompy.addToStudy( vesselTop, 'vesselTop' )
geompy.addToStudy( slurryOutlet, 'slurryOutlet' )
geompy.addToStudy( Cylinder_1, 'Cylinder_1' )
geompy.addToStudy( Rotation_1, 'Rotation_1' )
geompy.addToStudy( Cut_1slurry, 'Cut_1slurry' )
geompy.addToStudyInFather( Cut_1slurry, slurryExit, 'slurryExit' )
geompy.addToStudyInFather( Cut_1slurry, slurryExitWall, 'slurryExitWall' )
geompy.addToStudyInFather( Cut_1slurry, Face_15, 'Face_15' )
geompy.addToStudy( Cut_1vent, 'Cut_1vent' )
geompy.addToStudyInFather( Cut_1vent, vent, 'vent' )
geompy.addToStudyInFather( Cut_1vent, ventSideWall, 'ventSideWall' )
geompy.addToStudyInFather( Cut_1vent, Face_7, 'Face_7' )
geompy.addToStudyInFather( Cut_1vent, Face_8, 'Face_8' )
geompy.addToStudyInFather( Cut_1vent, Face_9, 'Face_9' )
geompy.addToStudyInFather( Cut_1vent, Face_10, 'Face_10' )
geompy.addToStudyInFather( Cut_1vent, Face_11, 'Face_11' )
geompy.addToStudy( Cut_1, 'Cut_1' )
geompy.addToStudyInFather( Cut_1, Face_1, 'Face_1' )
geompy.addToStudyInFather( Cut_1, Face_2, 'Face_2' )
geompy.addToStudyInFather( Cut_1, Face_3, 'Face_3' )
geompy.addToStudyInFather( Cut_1, Face_4, 'Face_4' )
geompy.addToStudyInFather( Cut_1, vesseltopFace, 'vesseltopFace' )
geompy.addToStudy( cylindervessle, 'cylindervessle' )
geompy.addToStudyInFather( cylindervessle, Face_5, 'Face_5' )
geompy.addToStudyInFather( cylindervessle, Face_6, 'Face_6' )
geompy.addToStudyInFather( cylindervessle, vesselCylinderWall, 'vesselCylinderWall' )
geompy.addToStudyInFather( cylindervessle, Face_13, 'Face_13' )
geompy.addToStudy( Cylinder_2, 'Cylinder_2' )
geompy.addToStudy( Cut_2, 'Cut_2' )
geompy.addToStudy( block, 'block' )
geompy.addToStudy( vessel, 'vessel' )
geompy.addToStudy( inlet, 'inlet')
geompy.addToStudy( inletPipe, 'inletPipe')

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New(theStudy)
vesselMesh = smesh.Mesh(vessel)
NETGEN_2D = vesselMesh.Triangle(algo=smeshBuilder.NETGEN_1D2D)
NETGEN_2D_Parameters_1 = NETGEN_2D.Parameters()
NETGEN_2D_Parameters_1.SetMaxSize( 0.045 )
NETGEN_2D_Parameters_1.SetSecondOrder( 0 )
NETGEN_2D_Parameters_1.SetOptimize( 1 )
NETGEN_2D_Parameters_1.SetFineness( 2 )
NETGEN_2D_Parameters_1.SetMinSize( 0.005 )
NETGEN_2D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_1.SetFuseEdges( 1 )
NETGEN_2D_Parameters_1.SetQuadAllowed( 0 )
isDone = vesselMesh.Compute()
try:
  vesselMesh.ExportSTL(dirPathCase + 'vessel_.stl', 1 )
except:
  print 'ExportSTL() vessel failed. Invalid file name?'

smesh = smeshBuilder.New(theStudy)
ventMesh = smesh.Mesh(vent)
NETGEN_2D = ventMesh.Triangle(algo=smeshBuilder.NETGEN_1D2D)
NETGEN_2D_Parameters_1 = NETGEN_2D.Parameters()
NETGEN_2D_Parameters_1.SetMaxSize( 0.005 )
NETGEN_2D_Parameters_1.SetSecondOrder( 0 )
NETGEN_2D_Parameters_1.SetOptimize( 1 )
NETGEN_2D_Parameters_1.SetFineness( 2 )
NETGEN_2D_Parameters_1.SetMinSize( 0.002 )
NETGEN_2D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_1.SetFuseEdges( 1 )
NETGEN_2D_Parameters_1.SetQuadAllowed( 0 )
isDone = ventMesh.Compute()
try:
  ventMesh.ExportSTL(dirPathCase + 'outlet_.stl', 1 )
except:
  print 'ExportSTL() outlet failed. Invalid file name?'

smesh = smeshBuilder.New(theStudy)
slurryExitMesh = smesh.Mesh(slurryExit)
NETGEN_2D = slurryExitMesh.Triangle(algo=smeshBuilder.NETGEN_1D2D)
NETGEN_2D_Parameters_1 = NETGEN_2D.Parameters()
NETGEN_2D_Parameters_1.SetMaxSize( 0.005 )
NETGEN_2D_Parameters_1.SetSecondOrder( 0 )
NETGEN_2D_Parameters_1.SetOptimize( 1 )
NETGEN_2D_Parameters_1.SetFineness( 2 )
NETGEN_2D_Parameters_1.SetMinSize( 0.002 )
NETGEN_2D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_1.SetFuseEdges( 1 )
NETGEN_2D_Parameters_1.SetQuadAllowed( 0 )
isDone = slurryExitMesh.Compute()
try:
  slurryExitMesh.ExportSTL( dirPathCase + 'outletSlurry_.stl', 1 )
except:
  print 'ExportSTL() outletSlurry failed. Invalid file name?'

smesh = smeshBuilder.New(theStudy)
inletMesh = smesh.Mesh(inlet)
NETGEN_2D = inletMesh.Triangle(algo=smeshBuilder.NETGEN_1D2D)
NETGEN_2D_Parameters_1 = NETGEN_2D.Parameters()
NETGEN_2D_Parameters_1.SetMaxSize( 0.005 )
NETGEN_2D_Parameters_1.SetSecondOrder( 0 )
NETGEN_2D_Parameters_1.SetOptimize( 1 )
NETGEN_2D_Parameters_1.SetFineness( 2 )
NETGEN_2D_Parameters_1.SetMinSize( 0.002 )
NETGEN_2D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_1.SetFuseEdges( 1 )
NETGEN_2D_Parameters_1.SetQuadAllowed( 0 )
isDone = inletMesh.Compute()
try:
  inletMesh.ExportSTL(dirPathCase + 'inlet_.stl', 1 )
except:
  print 'ExportSTL() inlet failed. Invalid file name?'

smesh = smeshBuilder.New(theStudy)
inletPipeMesh = smesh.Mesh(inletPipe)
NETGEN_2D = inletPipeMesh.Triangle(algo=smeshBuilder.NETGEN_1D2D)
NETGEN_2D_Parameters_1 = NETGEN_2D.Parameters()
NETGEN_2D_Parameters_1.SetMaxSize( 0.015 )
NETGEN_2D_Parameters_1.SetSecondOrder( 0 )
NETGEN_2D_Parameters_1.SetOptimize( 1 )
NETGEN_2D_Parameters_1.SetFineness( 2 )
NETGEN_2D_Parameters_1.SetMinSize( 0.005 )
NETGEN_2D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_1.SetFuseEdges( 1 )
NETGEN_2D_Parameters_1.SetQuadAllowed( 0 )
isDone = inletPipeMesh.Compute()
try:
  inletPipeMesh.ExportSTL( dirPathCase + 'inletPipe_.stl', 1 )
except:
  print 'ExportSTL() inletPipe failed. Invalid file name?'

smesh = smeshBuilder.New(theStudy)
blockMesh = smesh.Mesh(block)
NETGEN_2D = blockMesh.Triangle(algo=smeshBuilder.NETGEN_1D2D)
NETGEN_2D_Parameters_1 = NETGEN_2D.Parameters()
NETGEN_2D_Parameters_1.SetMaxSize( 0.015 )
NETGEN_2D_Parameters_1.SetSecondOrder( 0 )
NETGEN_2D_Parameters_1.SetOptimize( 1 )
NETGEN_2D_Parameters_1.SetFineness( 2 )
NETGEN_2D_Parameters_1.SetMinSize( 0.005 )
NETGEN_2D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_1.SetFuseEdges( 1 )
NETGEN_2D_Parameters_1.SetQuadAllowed( 0 )
isDone = blockMesh.Compute()
try:
  blockMesh.ExportSTL( dirPathCase + 'block_.stl', 1 )
except:
  print 'ExportSTL() block failed. Invalid file name?'

## Set names of Mesh objects
smesh.SetName(NETGEN_2D.GetAlgorithm(), 'NETGEN_2D')
smesh.SetName(NETGEN_2D_Parameters_1, 'NETGEN 2D Parameters_1')
smesh.SetName(vesselMesh.GetMesh(), 'vesselMesh')
smesh.SetName(ventMesh.GetMesh(), 'ventMesh')
smesh.SetName(slurryExitMesh.GetMesh(), 'slurryExitMesh')
smesh.SetName(inletPipeMesh.GetMesh(), 'inletPipeMesh')
smesh.SetName(inletMesh.GetMesh(), 'inletMesh')
smesh.SetName(blockMesh.GetMesh(), 'blockMesh')

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)

for file in os.listdir(dirPathCase):
    if file.endswith(".stl"):
        fileName = os.path.join(dirPathCase,file)
        sourceFile = open(fileName,'r')
        targetFile = open(fileName[:-5] + fileName[-4:],'w')
        first_row = True
        for row in sourceFile:
            if first_row:
                row = 'solid ' + file[:-5] + '\n'
                first_row = False
            targetFile.write(row)
        sourceFile.close()
        targetFile.close()
        os.remove(fileName)

