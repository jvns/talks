# Spying on Hadoop with strace

by Julia Evans <br>
[`twitter.com/b0rk`][twitter]  <br>
[`github.com/jvns`][github]  <br>
[`jvns.ca`][website]  <br>

[github]: https://github.com/jvns
[twitter]:  https://twitter.com/b0rk
[website]: http://jvns.ca


# all you need to know about Hadoop

```
$ hadoop fs -ls /user/julia 
file1
file2
````

# Learning about HDFS

+ read documentation
+ Google errors
+ search through logs
+ ask your friends


# strace <br> = <br> wizardry

# System calls: <br> a OS's API

# System calls

+ open
+ write
+ sendto/recvfrom

# How to strace

```
$ strace hadoop fs -ls /penguin
```

</section>
<section data-background="strace-garbage.png">

# open

```
strace -e open hadoop fs -ls /panda
open("/etc/hadoop/mapred-site.xml", O_RDONLY) = 274
open("/etc/hadoop/yarn-site.xml", O_RDONLY) = 274
open("/etc/hadoop/hdfs-site.xml", O_RDONLY) = 274
```

# sendto

```
$ strace snakebite ls /unicorn
connect(8, {sa_family=AF_INET, sin_port=htons(9200),
    sin_addr=inet_addr("10.147.177.170")}, 16) = 0
sendto(8,
    "\nB\n5\n3\n(BP-1019336183-10.165.43.39-1400088409498\20\211\200\200\200\4\30\361\7\22\tsnakebite\20\0\30\200\200\200@",
    75, 0, NULL, 0) = 75
```

# recvfrom

```
strace hadoop fs -get /somefile.xml
recvfrom(8, "ot, it's a painting. Thomas Graeme apparently lived in
the mid-18th century, according to the [[Graeme Park]] article. The
rationale also says that this image is "used on the biography
page about him by USHistory.org of Graeme Park." I cannot quite
figure out what this means, but I am guessing that it means the
uploader took this image from a page hosted on USHistory.org. A
painting of a man who lived in the mid-18th century is likely to be
the public domain, as claimed, but we have no good source", 512, 0,
NULL, NULL) = 512
```

# write

+ spy on log files!

#

<img src="warning.png">

# Next time

* How HDFS works
* architecture: DataNodes! NameNodes!
* MapReduce
* how you could build your own database on top of HDFS if it were a good idea
* BEING A WIZARD

[`twitter.com/b0rk`][twitter]  <br>
[`jvns.ca`][website]  <br>

[twitter]:  https://twitter.com/b0rk
[website]: http://jvns.ca

