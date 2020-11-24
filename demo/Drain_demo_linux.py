#!/usr/bin/env python
import sys
sys.path.append('../')
from logparser import Drain

input_dir  = '../logs/my_linux/'  # The input directory of log file
output_dir = 'Drain_result/'  # The output directory of parsing results
log_file   = 'syslog'  # The input log file name
log_format = '<Month> <Date> <Time> <Level> <Component>(\[<PID>\])?: <Content>'
# Regular expression list for optional preprocessing (default: [])
regex      = [
    r'(\d+\.){3}\d+', r'\d{2}:\d{2}:\d{2}'
]
st         = 0.39  # Similarity threshold
depth      = 6  # Depth of all leaf nodes


parser = Drain.LogParser(log_format, indir=input_dir, outdir=output_dir,  depth=depth, st=st, rex=regex)
parser.parse(log_file)

