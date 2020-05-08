#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 22:46:50 2020

@author: daria_pirogova
"""

# SAMPLE USAGE:
# python3 Bundestag_XML_Parsing.py path_to_a_folder_with_protocols

import xml.etree.ElementTree as ET
import glob
import sys

files = glob.glob(sys.argv[1] + '/*.xml')
outputfile = open("output.txt", "w") #in case we need to write something earlier

i = 1 #to add an id to the file name
for file in sorted(files):
    
    root = ET.parse(file).getroot()
    for child in root.iter():
        if child.find('datum') != None:
            for datum in child.find('datum').attrib.values():
                filename = str(i) +  "-" + str(datum) + ".txt"
    outputfile.close()
    outputfile = open(filename, "w")
    for line in root.iter():
        if line.text != None and line.tag != 'seite' and line.tag != 'seitenbereich':
            if line.tag == 'vorname' or line.tag == 'name' or line.tag == 'vorname' or line.tag == 'titel' or line.tag == 'fraktion':
                outputfile.write(line.text + " ")
            else:
                outputfile.write(line.text + '\n')
    outputfile.close()
    i = i + 1