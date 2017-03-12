#!/usr/bin/env python
"""
@file    test.py
@author  Pablo Alvarez Lopez
@date    2016-11-25
@version $Id$

python script used by sikulix for testing netedit

SUMO, Simulation of Urban MObility; see http://sumo.dlr.de/
Copyright (C) 2009-2017 DLR/TS, Germany

This file is part of SUMO.
SUMO is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.
"""
# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit

# Open netedit
neteditProcess, match = netedit.setupAndStart(neteditTestRoot, False)

# apply zoom
netedit.zoomIn(match.getTarget().offset(325, 200), 10)

# go to additional mode
netedit.additionalMode()

# select E3
netedit.changeAdditional("e3Detector")

# create E3 with default parameters (will not be writed)
netedit.leftClick(match, 100, 100)

# create E3 with default parameters
netedit.leftClick(match, 200, 100)

# Change frequency
netedit.modifyAdditionalDefaultValue(2, "150")

# create E3 with different frequency
netedit.leftClick(match, 300, 100)

# Change timeTreshold
netedit.modifyAdditionalDefaultValue(3, "5")

# create E3 with different timeTreshold
netedit.leftClick(match, 400, 100)

# Change speedTreshold
netedit.modifyAdditionalDefaultValue(4, "2.51")

# create E3 with different speedTreshold
netedit.leftClick(match, 500, 100)

# select entry detector
netedit.changeAdditional("detEntry")

# Create Entry detectors for all E3 detectors except for the first
netedit.selectAdditionalChild(4, 1)
netedit.leftClick(match, 50, 250)
netedit.selectAdditionalChild(4, 1)
netedit.leftClick(match, 200, 250)
netedit.selectAdditionalChild(4, 1)
netedit.leftClick(match, 350, 250)
netedit.selectAdditionalChild(4, 1)
netedit.leftClick(match, 500, 250)

# Check undo redo
netedit.undo(match, 9)
netedit.redo(match, 9)

# save additionals
netedit.saveAdditionals()

# save newtork
netedit.saveNetwork()

# quit netedit
netedit.quit(neteditProcess, False, False)
