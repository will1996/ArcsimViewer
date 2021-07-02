cd replays
rm -rf $1
python fetchReplay.py $1
cd ..

python genDockerFile.py $1

docker build . -t arcsim

docker run --rm -it  -p 5900:5900/tcp -p 6080:6080/tcp arcsim:latest