#!/usr/bin/env python
import sys
import os
sys.path.append('../')
from logparser import Drain
from createSessonLog.createSessionLog  import LogParser
from shutil import copyfile
from preprocess.preprocessLog import preprocess
#inputfilename = sys.argv[1]
curIndex = 0


output_dir = 'Drain_result_mysql/'  # The output directory of parsing results
input_dir_list  = ['../logs/mysql/query.log_afterPreProcess']
print("path:",os.path.split(input_dir_list[curIndex]))
input_dir ,log_file= os.path.split(input_dir_list[curIndex])
copyfile(input_dir_list[curIndex], output_dir+log_file)



 #log format
log_format_list = ['<Time> <Id> <Content>']
log_format = log_format_list[curIndex]

# Regular expression list for optional preprocessing (default: [])
regex      = [
    r'(?<=[^A-Za-z0-9])(\-?\+?\d+)(?=[^A-Za-z0-9])|[0-9]+$' # Numbers
]
st         = 0.5  # Similarity threshold
depth      = 4  # Depth of all leaf nodes


parser = Drain.LogParser(log_format, indir=input_dir, outdir=output_dir,  depth=depth, st=st, rex=regex,keep_para=False)
parser.parse(log_file)
print("output_dir:",output_dir)


'''
log_format_list = ['<LineId> <Time> <Id> <Command> <Content> <EventId> <EventTemplate>']
logfilePath = output_dir 
createSessionLogparser = LogParser(log_format, indir=output_dir, outdir=output_dir,  depth=depth, st=st, rex=regex,keep_para=False)
createSessionLogparser.parse(log_file+'_structured.csv')
'''

