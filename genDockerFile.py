import os
import sys
import pdb

lines = None
with open("_DockerfileTemplate",'r') as f:
    lines = f.readlines()

env_line = "ENV APP /arcsim/bin/arcsim replay /replays/"+sys.argv[1]

lines.append(env_line)
with open("Dockerfile","w") as f:
    f.write("\n".join(lines))
