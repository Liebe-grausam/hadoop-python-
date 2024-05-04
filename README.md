# hadoop+python实现中文词频统计
step 1：
在input文件夹中放入待处理的文件

step 2：
在script文件夹下启动终端，运行代码
```
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/your_hadoop-streaming_jar -files mapper.py,reducer.py -mapper "python3 mapper.py" -reducer "python3 reducer.py" -input road_to_posts/small_input/ -output road_to_posts/f_output/
```

step 3：
将输出文件夹中的part-00000中的运行结果拷贝到script文件夹中的output.txt
在script文件夹下启动终端，运行代码
```
python3 word_cloud.py
```
即可得到同一目录下保存的word_cloud.png