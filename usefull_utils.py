import os
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split('(\d+)', text) ]
    
#Return full path to files, mask should be in format '.jpg'
def GetAllFilesInDir(path, mask):
    filenames=[]
    for filename in os.listdir(path):
        if filename.endswith(mask):
            filenames.append(os.path.join(path,filename))
    
    #Human sort
    filenames.sort(key=natural_keys)
    
    for i in range(0, len(filenames)):
        filenames[i]= os.path.join(path,filenames[i])
    
    return filenames
