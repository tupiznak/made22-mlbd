Для запуска используется следующая команда `docker run --rm -u $(id -u) -p8080:8080 -p 4040:4040 -p6789:6789 -v $(pwd)/spark:/opt/spark -eSPARK_HOME=/opt/spark -eZEPPELIN_LOCAL_IP=0.0.0.0 -v $(pwd)/data:/opt/data --name zeppelin apache/zeppelin:0.10.1`

Где в папке `data` должны лежать распакованные файлы из kaggle, а в папке spark должен лежать spark версии 3.1.3

Т.к. ни ноутбук, ни zpln не отображается в github, для удобства, сделал скрины по всем ячейкам

![](https://github.com/tupiznak/made22-mldb/blob/homework4/4/screenshots/read_data.png)

![](https://github.com/tupiznak/made22-mldb/blob/homework4/4/screenshots/transform.png)

![](https://github.com/tupiznak/made22-mldb/blob/homework4/4/screenshots/schema.png)

![](https://github.com/tupiznak/made22-mldb/blob/homework4/4/screenshots/split.png)

![](https://github.com/tupiznak/made22-mldb/blob/homework4/4/screenshots/num_features.png)

![](https://github.com/tupiznak/made22-mldb/blob/homework4/4/screenshots/htf-idf.png)

![](https://github.com/tupiznak/made22-mldb/blob/homework4/4/screenshots/word2vec.png)
