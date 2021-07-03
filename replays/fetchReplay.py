import os
import sys
#targetPath ="/nfshomes/will1996/ClothSimulatorMPI/out"

outputName = sys.argv[1]

targetPath =  "/nfshomes/will1996/ClothSimulatorGPU/benchmarks/bridson"
#outputName = "unconstrained_state_smoothing"
os.system("rm -rf ./"+outputName)
os.system("ssh will1996@lrvrwks09 -X 'tar -czvf outbound.tar.gz "+targetPath+"'")

os.system("scp will1996@lrvrwks09:~/outbound.tar.gz ./inbound.tar.gz")

os.system("tar -xzvf ./inbound.tar.gz")

os.system("mv ./"+targetPath+" ./"+outputName)
os.system("rm -r ./nfshomes")

os.system("python3 formatReplays.py "+outputName)


