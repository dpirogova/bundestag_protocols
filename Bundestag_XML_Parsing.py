#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: daria_pirogova
"""

# SAMPLE USAGE:
# python3 Bundestag_XML_Parsing.py path_to_a_folder_with_protocols

import xml.etree.ElementTree as ET
import glob
import sys

files = glob.glob(sys.argv[1] + '/*.xml')
#print(sys.argv[1] + '/*.xml')
outputfile = open("output.txt", "w") #in case we need to write something earlier

i = 1 #adding an id to the filename
for file in sorted(files):

    root = ET.parse(file).getroot()
    datum = root.find('DATUM') #adding the date to the filename
    filename = str(i) + "-" + datum.text + ".txt"
    #print(filename)
    outputfile.close()
    outputfile = open(filename, "w")
    #extracting all information
    for line in root.iter():
        outputfile.write(line.text + '\n')
    outputfile.close()
    i = i + 1
