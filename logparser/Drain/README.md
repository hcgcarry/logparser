# Drain

Drain is an online log parser that can parse logs into structured events in a streaming and timely manner. It employs
a parse tree with fixed depth to guide the log group search process, which effectively avoids constructing a very deep and unbalanced tree. 

Read more information about Drain from the following papers:

+ Pinjia He, Jieming Zhu, Zibin Zheng, and Michael R. Lyu. [Drain: An Online Log Parsing Approach with Fixed Depth Tree](http://jiemingzhu.github.io/pub/pjhe_icws2017.pdf), *Proceedings of the 24th International Conference on Web Services (ICWS)*, 2017.

Researchers from IBM made an upgrade version of Drain in Python 3.6 with additional features: [https://github.com/IBM/Drain3](https://github.com/IBM/Drain3)

# tree
depth:len的識別


# accuracy
  accuracy = accurate_events / log大小
  accurate_events:同一個events全部對應到才會算近來,比如說log events :receive * from *
在parse完的結果要剛剛好跟ground true一一對應,就會把對應到的數量加到accurate_events上,否則+0

