
import queue  
import re
import sys
import os
from datetime import datetime




def buildHashToNumFile(templates_file_list,hasdToNumber_maps_file):
    IdCount = 0
    hashIdToNumberIdDict = {}
    for i in range(len(templates_file_list)):
        with open(templates_file_list[i], 'r') as fin:
            fin.readline()
            for line in fin.readlines():
                tmpLine =line.split(',')
                if tmpLine[0] not in hashIdToNumberIdDict:
                    IdCount+=1
                    hashIdToNumberIdDict[tmpLine[0]] = str(IdCount)
    with open(hashToNumber_maps_file,'w') as fou:
        for key in hashIdToNumberIdDict:
            line = "{} {}\n".format(key,hashIdToNumberIdDict[key])
            fou.write(line)


def convert(input_log_file_list,hashToNumber_maps_file):
    # read hash to number maps
    hashIdToNumberIdDict = {}
    with open(hashToNumber_maps_file,"r") as fin:
        for line in fin.readlines():
            tmpLine =line.split()
            hashIdToNumberIdDict[tmpLine[0]] = tmpLine[1]
    print("hashIdTonumberIdDict",hashIdToNumberIdDict)
    print("class num",len(hashIdToNumberIdDict))

    for input_log_file in input_log_file_list:
        sessionIdList = []
        with open(input_log_file, 'r') as fin:
            for line in fin.readlines():
                perLineNumberIdList=[]
                tmpLine =line.split( )
                for index,hashId in enumerate(tmpLine):
                    perLineNumberIdList.append(hashIdToNumberIdDict[hashId])
                sessionIdList.append(perLineNumberIdList)

        with open(input_log_file+"_numberID","w") as file:
            for index,sessionIds in enumerate(sessionIdList):
                seq = " ".join(sessionIds)
                file.write(seq+'\n')
                
            

if __name__ == "__main__":
    #input_log_file = "../demo/Drain_result_mysql/query.log_normal_afterPreProcess_session"
    #input_log_file = "../demo/Drain_result_openstack/openstack_normal2.log_preprocess_session"
    templates_file_list= ["../demo/Drain_result_openstack/openstack_normal1.log_preprocess_templates.csv","../demo/Drain_result_openstack/openstack_normal2.log_preprocess_templates.csv", "../demo/Drain_result_openstack/openstack_abnormal.log_preprocess_templates.csv"]
    input_log_file_list = ["../demo/Drain_result_openstack/openstack_abnormal.log_preprocess_session","../demo/Drain_result_openstack/openstack_normal1.log_preprocess_session", "../demo/Drain_result_openstack/openstack_normal2.log_preprocess_session"]
    hashToNumber_maps_file = "../demo/Drain_result_openstack/hash_number_maps"
    if len(sys.argv) < 2:
        print("usage : python convertHashToNumber_openstack.py {build|convert}")
    elif sys.argv[1] == "build":
        buildHashToNumFile(templates_file_list,hashToNumber_maps_file)
    else:
        convert(input_log_file_list,hashToNumber_maps_file)