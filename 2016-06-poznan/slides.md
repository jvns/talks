# what's systems <br>programming?

programming where you get a little closer to the metal

# this talk:

1. programming experiments
2. debugging like a wizard

# rules of programming experiments 

1. it doesn't have to work
1. you don't have to finish it
1. you have to learn something


# experiment 1: write an operating system

remember it doesn't have to work

# what I learned

* 


# experiment 2: <br> database surgery

# how does SQLite work?

# fun.sqlite

<pre>
id | word
1 | greedy
2 | greediness
3 | greener
</pre>

# 

<pre>
$ hexdump fun.sqlite
|.............{.n|
|.a.R.D.4.%......|
|................|
|...y.n._.N.>.,.$|
|................|
|..............F.|
|..EAcevedo.E...D|
|Accra's.D...CAcc|
|ra.C..#BAccentur|
|e's.B...AAccentu|
|re.A..!@Acapulco|
|'s.@...?Acapulco|
</pre>

# a database is a _tree_

# 

```
static MemPage *btreePageFromDbPage(DbPage *pDbPage, Pgno pgno, BtShared *pBt){
    // actual code
  printf("Read a btree page, page number %d\n", pgno); // added by me!
   // actual code
}
```


# 

<pre>
sqlite> select * from fun where id = 1;
Read a btree page, page number 1
Read a btree page, page number 5
Read a btree page, page number 828
Read a btree page, page number 10
Read a btree page, page number 2
Read a btree page, page number 76
Read a btree page, page number 6
1|A's
</pre>


# 

<pre>
sqlite> select * from fun where id = 20;
Read a btree page, page number 1
Read a btree page, page number 5
Read a btree page, page number 828
Read a btree page, page number 10
Read a btree page, page number 2
Read a btree page, page number 76
Read a btree page, page number 6
20|Aaliyah
</pre>

# 

<pre>
sqlite> select * from fun where id = 80000;
Read a btree page, page number 1
Read a btree page, page number 5
Read a btree page, page number 1198
Read a btree page, page number 992
Read a btree page, page number 2
Read a btree page, page number 1813
Read a btree page, page number 449
80000|scarfs
</pre>


# what I learned

* databases tables are trees
* databases are made of pages
* i can read some of the SQLite source code!

# experiment 3: <br> write a TCP stack

# experiment 3: <br> write a TCP stack <br> in python

# 

<pre>
ip_header = IP(dst=dest_ip, src=src_ip)
syn = TCP(dport=80, sport=59333, 
          ack=0, flags="S")
# Send the SYN packet to Google
response = srp(ip_header + syn)
</pre>



http://jvns.ca

# what I learned

* how TCP packets are put together!
* you can write a 10% working TCP from scratch in 2 weeks
* python can't keep up

# experiment 4: <br> concurrency

<!-- story about interview -->

# 

```

int counter;

void *AddThings(void *threadid) {
   for (int i = 0; i < 10000; i++)
        counter += 1;
   pthread_exit(NULL);
}
```

# wrong answer

# mutex

<pre>
pthread_mutex_lock(&mutex);
counter += 1;
</pre>
```

# "atom"

```
 __sync_add_and_fetch(&counter, 1);
```

# what I learned

* atoms are faster than mutexes

# i blog my experiments

# 

"can you discuss the pros and cons of using a lock-free approach for implementing a thread-safe hashmap?"

# do enough <br>experiments <br><br> end up with actual knowledge