import os
import csv
import pypff
import argparse

#pstStripper.py by inurdata
#This program strips elements out of a pst file based on keywords
#if you don't specify output it saves it as output.pst

#USAGE INFO
def msg(name=None):
    return '''
     ________________________                                       
    |       |          |           |                             
    | _____/ \____     |     ______|_______*____________________ 
    |              \   |    \_____ |  |/   ||/  \|/  \/__\|/     
    |       ______ /   |_________/ |  |    ||\__/|\__/\__ |         
                                            |    |
     __                                     |    |                                    
    /  \      ____________________________________________________________________________
    |  |     | pstStripper deletes elements from a pst file based on key terms.            \ 
    @  @    / Usage: pstStripper.py -h -i INPUT -o OUTPUT -k KEYFILE -K KEYWORDS -g -G      \ 
    |  |   /  >>>>if you don't specify an output file the output will be saved as output.pst/  
    || |/ /_ ------------------------------------------------------------------------------*
    || ||
    |\_/|
    \___/                                    
    '''


#GLOBAL VARS
inFile = ""
outFile = ""
keyFile = ""
keywordInput = ""
keys = []
parser = argparse.ArgumentParser(usage=msg())

#COMMAND LINE ARGS
parser.add_argument('-i', '--input', type=str, help="input file location: C:\Path\input.pst")
parser.add_argument('-o', '--output', type=str, help="output file location: C:\Path\output.pst")
parser.add_argument('-k', '--keyfile', type=str, help="keyword text or csv file: C:\Path\keys.txt")
parser.add_argument('-K', '--keywords', type=str, help="comma separated keywords: key0, key1, keyN")
parser.add_argument('-g', '--guided', help="use by itself for guided command line mode", action="store_true")
parser.add_argument('-G', '--gui', help="use by itself for graphical user interface (GUI) mode", action="store_true")
args = parser.parse_args()

#FUNCTIONS
def setOutFile(inputFile):
    from os.path import basename
    file = basename(inputFile)
    path = inputFile.replace(file,'')
    out = path+"output.pst"
    return out;

#MODES__________________________________________________________________________________________________________________
#GUIDED MODE
if args.guided:
    while inFile is "":
            inFile = raw_input("Input your pst file, ie C:\Path\File.pst: ")
            if inFile == "":
                    print "Please enter a file location!"
            outFile = raw_input("Input your output file, ie C:\Path\File.pst: ")
            while keyFile or keywordInput is "":
                keyFile = raw_input("Input your keyword file, ie C:\Path\keys.txt or press enter to skip: ")
                keywordInput = raw_input("Input your keywords separated by a comma, ie key1, key2, keyN or press enter to skip: ")
                if keyFile and keywordInput is "":
                    print "Please enter a keyword file or input keywords."
#GUI MODE
elif args.gui:
    print "coming soon"
    exit()

#CMD LINE MODE
elif args.input:
    inFile = args.input
    if args.output:
        outFile = args.output
    if args.keyfile:
        keyFile = args.keyfile
    if args.keywords:
        keywordInput = args.keywords

#HELP
else:
    parser.print_help()
    exit()



#ERROR HANDLING & WORK__________________________________________________________________________________________________
if inFile is "":
    print "ERROR: no input file"
    exit()
if keys is []:
    print "ERROR: no keyword input"
    exit()

#HANDLE EMPTY OUTPUT FILE VAR
if outFile is "":
    outFile = setOutFile(inFile)

#DO WORK ON PST FILE
pst = pypff.file(inFile)
pst.open(inFile)
pst.close()