

FROM thewtex/opengl

RUN apt-get -y update

RUN apt-get -y install g++

RUN apt-get -y install gfortran

RUN apt-get -y install make

RUN apt-get -y install scons

RUN apt-get -y install libpng-dev

RUN apt-get -y install libglu1-mesa-dev

RUN apt-get -y install  mesa-common-dev

RUN apt-get -y install  mesa-utils

RUN apt-get -y install  freeglut3-dev  

RUN apt-get -y install libblas-dev 

RUN apt-get -y install liblapack-dev

RUN apt-get -y install libatlas-base-dev

RUN apt-get -y install libboost-all-dev

RUN apt-get -y install  x11-apps

RUN apt-get -y install xauth

RUN apt-get -y install ctags

COPY ./arcsim /arcsim

WORKDIR /arcsim

RUN make -C dependencies2

RUN make 

#Change the json file to run something else, also, replay should work. 

COPY ./meshes /meshes

COPY ./materials /materials

COPY ./conf /conf

COPY ./replays /replays
ENV APP /arcsim/bin/arcsim replay /replays/rewirte_test