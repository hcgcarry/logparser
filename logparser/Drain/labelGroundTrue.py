
import re
def labelGroundTrue():
    templateList= ["Normal exit <*> <*> run)"]
    searchList= ["Normal exit (fjdsk12 1 run)"]
    for index, line in enumerate(templateList):
        # if re.fullmatch(item, filename):
        searchList= ["Normal exit (fjdsk12 1 run)"]
        print("origin log message: ")
        print(searchList[0])
        line = "Normal exit <*> <*> run)"
        print("log template: ")
        print(line)
        line = re.escape(line)
        #print(list(':?\\+'))
        print("re.escape: ")
        print(line)
        line= re.sub(r'\\<\\\*\\>\\','.*?' ,line)
        #print("test",r'\\<\\\*\\>\\')
        print("regex used to label groundtrue: ")
        print(line)
        #line = re.compile(line)
        #print(line)
        matchObj = re.match(line,searchList[index])
        if matchObj:
            print(matchObj)
            print("match log message: ")
            print(matchObj.group())
        else:
            print ("No match!!")
        

        


labelGroundTrue()
