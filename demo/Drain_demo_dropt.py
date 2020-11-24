#!/usr/bin/env python
import sys
import os
sys.path.append('../')
from logparser import Drain
from shutil import copyfile
inputfilename = sys.argv[1]
if inputfilename == "advisor":
    curIndex = 0
elif  inputfilename == "tomcat":
    curIndex = 1
    

output_dir = 'Drain_result_dropt/'  # The output directory of parsing results
input_dir_list  = ['../logs/dropt/advisor/advisor.log', '../logs/dropt/service_kernel_logs/tomcat.log'] # The input directory of log file
print("path:",os.path.split(input_dir_list[curIndex]))
input_dir ,log_file= os.path.split(input_dir_list[curIndex])
#log_file   = 'advisor.log'  # The input log file name
copyfile(input_dir_list[curIndex], output_dir+log_file)

log_format_list = ['<Date> <Time> <Level> <dash> <Content>','<Date> <Time> <Level> <dash> <usr> <prj> <Content>']  # HDFS log format
log_format = log_format_list[curIndex]
# Regular expression list for optional preprocessing (default: [])
regex      = [
    r'(/|)([0-9]+\.){3}[0-9]+(:[0-9]+|)(:|)', # IP
    r'(?<=[^A-Za-z0-9])(\-?\+?\d+)(?=[^A-Za-z0-9])|[0-9]+$' # Numbers
]
st         = 0.5  # Similarity threshold
depth      = 4  # Depth of all leaf nodes


parser = Drain.LogParser(log_format, indir=input_dir, outdir=output_dir,  depth=depth, st=st, rex=regex,keep_para=False)
parser.parse(log_file)


