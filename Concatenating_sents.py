#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# SAMPLE USAGE:
# python3 Concatenating_sents.py path_to_a_folder_with_protocols

import glob
import sys

files = glob.glob(sys.argv[1] + '/*.txt')

def concatenating_sents(filename):
    res = []
    prevLine = ""
    with open(filename) as fn:
        lines = fn.readlines()
        for i in range(0, len(lines)):
            if i < len(lines)-1 and len(lines[i]) > 1 and not lines[i].endswith(" -") and lines[i][-1] == '\n' and lines[i][-2] == '-' and lines[i+1][0].islower():
                prevLine = prevLine + lines[i][:-2]
            elif i < len(lines)-1 and len(lines[i]) > 1 and not lines[i].endswith(" -") and lines[i][-1] == '\n' and lines[i][-2] == '-' and lines[i+1][0].isupper():
                prevLine = prevLine + lines[i][:-1]
            elif i < len(lines)-2 and len(lines[i]) > 1 and not lines[i].endswith(" -") and lines[i][-1] == '\n' and lines[i][-2] == '-' and lines[i+1][0].islower() and lines[i+2][0].islower():
                prevLine = prevLine + lines[i][:-2]
            elif i < len(lines)-2 and len(lines[i]) > 1 and not lines[i].endswith(" -") and lines[i][-1] == '\n' and lines[i][-2] == '-' and lines[i+1].startswith('\n') and lines[i+2][0].islower():
                prevLine = prevLine + lines[i][:-2]
            elif lines[i].startswith('\n'):
                res.append("")
            else:
                res.append(prevLine)
                res.append(lines[i])
                prevLine = ""
    return "".join(res)
    
output = open("output.txt", "w") #in case we need to write something earlier

i = 1 #to add an id to the file name
for file in sorted(files):
    filename = str(i) + '_sents.txt'
    print(file)
    doc = open(file, 'rt')
    #tokenizing sentences
    resulting = concatenating_sents(file)
    output.close()
    output = open(filename, 'w')
    output.write(resulting)
    output.close()
    i = i + 1
