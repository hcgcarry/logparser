
import queue  
import re
import os
from datetime import datetime



def convert(input_log_file,output_log_file):
    IdCount = 0
    sessionIdList = []
    hashIdToNumberIdDict = {}
    with open(input_log_file, 'r') as fin:
        for line in fin.readlines():
            perLineNumberIdList=[]
            tmpLine =line.split( )
            for index,hashId in enumerate(tmpLine):
                if hashId not in  hashIdToNumberIdDict:
                    IdCount +=1
                    hashIdToNumberIdDict[hashId] = str(IdCount)
                perLineNumberIdList.append(hashIdToNumberIdDict[hashId])
            sessionIdList.append(perLineNumberIdList)
                
            
    #print("sessionIDLIST",sessionIdList)
    with open(output_log_file,"w") as file:
        for index,sessionIds in enumerate(sessionIdList):
            seq = " ".join(sessionIds)
            file.write(seq+'\n')

if __name__ == "__main__":
    input_log_file = "../demo/Drain_result_mysql/session.log"
    output_log_file = input_log_file + "_numberID"
    convert(input_log_file,output_log_file)