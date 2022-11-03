cd hadoop/base || exit
docker build -t made22t4/hadoop-base:1.0 . || exit
cd ../namenode || exit
docker build -t made22t4/hadoop-namenode:1.0 . || exit
cd ../datanode || exit
docker build -t made22t4/hadoop-datanode:1.0 . || exit
cd ../resourcemanager || exit
docker build -t made22t4/hadoop-resourcemanager:1.0 . || exit
