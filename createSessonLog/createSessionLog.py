"""
Description : This file implements the Drain algorithm for log parsing
Author      : LogPAI team
License     : MIT
"""
 
import queue  
import re
import os
import numpy as np
import pandas as pd
import hashlib
from datetime import datetime



class LogParser:
    def __init__(self, log_format, indir='./', outdir='./result/', depth=4, st=0.4, 
                 maxChild=100, rex=[], keep_para=True):
        """
        Attributes
        ----------
            rex : regular expressions used in preprocessing (step1)
            path : the input path stores the input log file name
            depth : depth of all leaf nodes
            st : similarity threshold
            maxChild : max number of children of an internal node
            logName : the name of the input file containing raw log messages
            savePath : the output path stores the file containing structured logs
        """
        self.path = indir
        self.depth = depth - 2
        self.st = st
        self.maxChild = maxChild
        self.logName = None
        self.savePath = outdir
        #df_log,轉成dataframe的log
        self.df_log = None
        self.log_format = log_format
        self.rex = rex
        self.keep_para = keep_para

                

    def parse(self, logName):
        print('Parsing file: ' + os.path.join(self.path, logName))
        self.logName = logName
        #logCluL會紀錄每一個Logcluster

        self.load_data()
        #self.df_log.to_csv(os.path.join(self.savePath, self.logName + '_structured.csv'), index=False)
        print(self.df_log)
        self.convertStructureLogToSessionLog()


    def load_data(self):
        headers, regex = self.generate_logformat_regex(self.log_format)
        self.df_log = self.log_to_dataframe(os.path.join(self.path, self.logName), regex, headers, self.log_format)

    def convertStructureLogToSessionLog(self):
        sessionLog = dict()
        for idx, line in self.df_log.iterrows():
            id = line['Id']
            if id not in  sessionLog:
                sessionLog[id] = [line['EventId']]
            else:
                sessionLog[id].append(line['EventId'])
        
        print("sessionlog" ,sessionLog.items())


    #將log轉成dataframe的格式
    def log_to_dataframe(self, log_file, regex, headers, logformat):
        """ Function to transform log file to dataframe 
        根據headers 去把log message 切割
        """
        log_messages = []
        linecount = 0
        with open(log_file, 'r') as fin:
            for line in fin.readlines():
                try:
                    match = regex.search(line.strip())
                    message = [match.group(header) for header in headers]
                    log_messages.append(message)
                    linecount += 1
                except Exception as e:
                    pass
        logdf = pd.DataFrame(log_messages, columns=headers)
        logdf.insert(0, 'LineId', None)
        logdf['LineId'] = [i + 1 for i in range(linecount)]
        return logdf

    # 根據user提供的log_format去產生regular expression,可以把log message前面不是很重要的資訊給
    # 處理調,這樣的目的是切出後面的log content
    def generate_logformat_regex(self, logformat):
        """ Function to generate regular expression to split log messages
        """
        headers = []
        splitters = re.split(r'(<[^<>]+>)', logformat)
        #print("logformat",logformat)
        #print("splitters",splitters)
        regex = ''
        for k in range(len(splitters)):
            #print(" cur plitters",splitters[k])
            if k % 2 == 0:
                splitter = re.sub(' +', '\\\s+', splitters[k])
                regex += splitter
            else:
                header = splitters[k].strip('<').strip('>')
                regex += '(?P<%s>.*?)' % header
                headers.append(header)
            #print("regex",regex)
        regex = re.compile('^' + regex + '$')
        return headers, regex

    def get_parameter_list(self, row):
        template_regex = row["EventTemplate"]
        #print("row[eventtemplate]",template_regex)
        template_regex = re.sub(r"<.{1,5}>", "<*>", row["EventTemplate"])
        #print("template_regex",template_regex)
        if "<*>" not in template_regex: return []
        template_regex = re.sub(r'([^A-Za-z0-9])', r'\\\1', template_regex)
        template_regex = re.sub(r'\\ +', r'\s+', template_regex)
        template_regex = "^" + template_regex.replace("\<\*\>", "(.*?)") + "$"
        parameter_list = re.findall(template_regex, row["Content"])
        parameter_list = parameter_list[0] if parameter_list else ()
        parameter_list = list(parameter_list) if isinstance(parameter_list, tuple) else [parameter_list]
        return parameter_list

