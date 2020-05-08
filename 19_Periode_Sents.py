#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 23:19:17 2020

@author: daria_pirogova
"""
import nltk
import glob
import os
import sys

# SAMPLE USAGE:
# python3 19_Periode_Sents.py path_to_a_folder_with_protocols

files = glob.glob(sys.argv[1] + '/*.txt')

def creating_lst(filename):
    res = []
    with open(filename) as fn:
        for line in fn.readlines():
            res.append(line)
    return res

def removing_newlines(lst):
    result = []        
    for el in lst:
        if len(el) > 0 and el[-1] == '\n':
            result.append(el[:-1] + " ")
        else:
            result.append(el)          
    return result

output = open("output.txt", "w") #in case we need to write something earlier

i = 1 #to add an id to the file name
for file in sorted(files):
    filename = os.path.basename(file)
    print(filename)
    doc = open(file, 'rt')
    #tokenizing sentences
    with open(file) as fl:
        sents = nltk.sent_tokenize(fl.read(), language='german')
    output.close()
    output = open(filename, 'w')
    for sent in sents:
        output.write(sent + '\n')
    output.close()
    i = i + 1
