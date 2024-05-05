# hadoop+python实现中文词频统计
前置准备：ubuntu20.04 + hadoop环境，以及python文件运行必要的包。

step 1：
在input文件夹中放入待处理的文件。
![input文件夹内容](./img/input文件夹内容.png)


step 2：
在script文件夹下启动终端，运行代码：
```
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-version.jar -files mapper.py,reducer.py -mapper "python3 mapper.py" -reducer "python3 reducer.py" -input road_to_repo/input/ -output road_to_repo/output/
```
其中“hadoop-streaming-version.jar”的“version”要改成你的hadoop的实际版本，“road_to_repo”要改成克隆下来的该项目文件夹所在路径。

**most important!：此命令为一次性操作，如果运行失败，必须把生成的output文件夹删掉之后再重新运行该命令。**

代码运行需要一定时间，如果单纯为学习目的可以使用small_input文件夹作为输入。

代码运行结果保存在output文件夹下的part-00000中。
![part-00000内容](./img/part-00000.png)


step 3：
由于MapReduce的作用是统计词频，并不是用来生成词云图，因此还需要将刚才的运行结果拷贝到script文件夹中的output.txt。
在script文件夹下启动终端，运行代码：
```
python3 word_cloud.py
```
即可得到同一目录下保存的word_cloud.png。
![词云图example](./img/wordcloud.png)