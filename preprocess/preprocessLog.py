#!/usr/bin/env python
import sys
import os
sys.path.append('../')
from shutil import copyfile

#### 因為mysql log前面幾行不是log ,所以把它除掉
'''

output file name: _afterPreProcess"
'''
def preprocess(input_filePath,output_filePath):
    count =0
    with open(input_filePath,'r') as inputFile:
        with open(output_filePath,'w') as outputFile:
            count+=1 
            line= inputFile.readline()
            while line:
                if(count >3):
                    outputFile.write(line)
                count+=1 
                line= inputFile.readline()


if __name__ == "__main__":
    #inputfilename = sys.argv[1]
    curIndex = 0
    input_dir_list  = ['../logs/mysql/query.log']
    print("path:",os.path.split(input_dir_list[curIndex]))
    input_dir ,log_file= os.path.split(input_dir_list[curIndex])

    preprocess_input_fileName = input_dir+'/'+log_file
    preprocess_output_fileName = input_dir+'/'+log_file +"_afterPreProcess"
    preprocess(preprocess_input_fileName,preprocess_output_fileName)
