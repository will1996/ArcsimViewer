import os
import sys
import shutil
import json

def getNewFilename(oldfilename):
    if oldfilename.startswith("1"):
        components = oldfilename.split("_")
        newFileName = components[1]+"_"+components[-1]
        return newFileName
    else:
        return oldfilename
        
def getNewPathNames(target_dir):
    conf = {}
    with open(os.path.join(target_dir,"conf.json")) as ConfFile:
        conf = json.load(ConfFile)
        for obstacle in conf["obstacles"]:
            obstacle["mesh"] = os.path.join("/",obstacle["mesh"])
        for cloth in conf["cloths"]:
            cloth["mesh"] = os.path.join("/",cloth["mesh"])
            for material in cloth["materials"]:
                material["data"] = os.path.join("/",material["data"])

    with open(os.path.join(target_dir,"conf.json"),'w') as ConfFile:
        json.dump(conf,ConfFile,indent=2)

#Main
target = sys.argv[1]
target_dir = os.path.abspath(target)

for filename in os.listdir(target):
    print(filename,"->",getNewFilename(filename))
    os.rename(os.path.join(target_dir,filename),os.path.join(target_dir,getNewFilename(filename)))
    if filename.startswith("0_"):
        os.remove(os.path.join(target_dir,filename))
#reformat Conf.json   with new path names for material lookups
getNewPathNames(target_dir)
