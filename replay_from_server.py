import sys
import os
if len(sys.argv) < 2:
        raise ValueError("Provide a subdirectory of replays as a target directory to replay from")

target = sys.argv[1]
if '/' in target:
    split  = target.split('/')
    if len(split)==2:
        target = target.split('/')[-1]
    elif len(split)==3:
        target = target.split('/')[-2]
    else:
        raise ValueError("Invalid replay path "+target+", target must be a subdirectory of replays/")


os.chdir('replays')
os.system('python3 fetchReplay.py '+target)
os.chdir('..')
os.system('python3 genDockerFile.py '+target)
os.system('docker build . -t arcsim')
os.system("docker run --rm -it  -p 5900:5900/tcp -p 6080:6080/tcp arcsim:latest")
