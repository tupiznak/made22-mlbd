hadoop fs -put . /1
mapred streaming -input /1/data/data.csv -output /result_mean -mapper "/opt/python/Python-3.10.8/python /usr/src/app/1/mapper_mean.py" -reducer "/opt/python/Python-3.10.8/python /usr/src/app/1/reducer_mean.py"
mapred streaming -input /1/data/data.csv -output /result_var -mapper "/opt/python/Python-3.10.8/python /usr/src/app/1/mapper_var.py" -reducer "/opt/python/Python-3.10.8/python /usr/src/app/1/reducer_var.py"
hadoop fs -cat /result_mean/*
hadoop fs -cat /result_var/*
