#!/usr/bin/env python
import sys
import os
sys.path.append('../')
from logparser import Drain
from createSessonLog.createSessionLog  import LogParser
from shutil import copyfile
from preprocess.preprocessLog import preprocess
type = sys.argv[1]
if len(sys.argv) < 2:
    print("usage:python Drain_openstack.py {normal|abnormal}")
if type == "normal":
    curIndex = 0
else:
    curIndex = 1


output_dir = 'Drain_result_openstack/'  # The output directory of parsing results
input_path_list  = ['../logs/openstack_label/openstack_normal1.log_preprocess', '../logs/openstack_label/openstack_abnormal.log_preprocess']


print("path:",os.path.split(input_path_list[curIndex]))
input_dir ,log_file= os.path.split(input_path_list[curIndex])
copyfile(input_path_list[curIndex], output_dir+log_file)


 #log format
log_format = '<Logrecord> <Date> <Time> <Pid> <Level> <Component> \[<ADDR>\] <Instance> <Content>'


# Regular expression list for optional preprocessing (default: [])
regex      = [
        r'((\d+\.){3}\d+,?)+', r'/.+?\s', r'\d+' , r'\d'
]
#instance: 0f079bdd-4117-4f6a-8b49-f3fb720b483c]
st         = 0.5  # Similarity threshold
depth      = 5  # Depth of all leaf nodes


parser = Drain.LogParser(log_format, indir=input_dir, outdir=output_dir,  depth=depth, st=st, rex=regex,keep_para=False)
parser.parse(log_file)
print("output_dir:",output_dir)


'''
log_format_list = ['<LineId> <Time> <Id> <Command> <Content> <EventId> <EventTemplate>']
logfilePath = output_dir 
createSessionLogparser = LogParser(log_format, indir=output_dir, outdir=output_dir,  depth=depth, st=st, rex=regex,keep_para=False)
createSessionLogparser.parse(log_file+'_structured.csv')
'''

