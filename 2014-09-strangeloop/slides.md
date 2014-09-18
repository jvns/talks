# You can be a <br>kernel hacker

by Julia Evans <br>
[`twitter.com/b0rk`][twitter]  <br>
[`github.com/jvns`][github]  <br>
[`jvns.ca`][website]  <br>

[twitter]: https://github.com/jvns
[github]:  https://twitter.com/b0rk
[website]: http://jvns.ca

# 

<img src="hackerschool_logo.png" class="image">

# Where we're going

+ WTF is a kernel?
+ Why should you care?
+ Strategies for getting started with kernel programming
    a. Strace all the things!
    a. Read some kernel code!
    a. Write a kernel module!
    a. Do the Eudalypta challenge
    a. Write your own operating system
    a. Do an internship

# WTF is a kernel?

# Kernels are <br> just code!

#

When I go to http://google.com, kernel code runs for:

+ Typing in the address
+ Handling every network packet
+ Writing history files to disk
+ Allocating memory
+ Communicating with the graphics card

# How to call <br> kernel code

System calls!!!

# System calls: <br> an OS's API

* open a file! (`open`)
* start a program! (`execve`)
* change a file's permissions! (`chmod`)

# What we've learned 

+ Your kernel does tons of stuff
+ Programs tell it what to do using system calls

# Why should you care?

+ People will think you're a badass
+ It's fun
+ **You'll become a better programmer**

# Using systems knowledge to debug

# strace

# Normal debugging:

+ look at the source code
+ add print statements
+ know the programming language

# strace <br> = <br> wizardry

# System calls: <br> a OS's API

* open a file! (`open`)
* start a program! (`execve`)
* change a file's permissions! (`chmod`)
* networking! (sendto/recvfrom)

# How to strace

```
$ strace google-chrome
execve("/usr/bin/google-chrome", ["google-chrome"], [/* 51 vars */]) = 0
brk(0)                                  = 0x124f000
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
```

</section>
<section data-background="strace-garbage.png">

# open

```
strace -etrace=open google-chrome
```
<img src="consent-to-send-stats.png">

# open

```
strace -etrace=open google-chrome
```
<img src="consent-to-send-stats-censored.png">

# open

```
$ cat ~/.config/google-chrome/Consent\ To\ Send\ Stats
6795275A1128269862CB7A471F5E0228% 
```

# execve

```
$ strace -f -etrace=execve google-chrome
6116  execve("/opt/google/chrome/chrome", ["/usr/bin/google-chrome"], 
[/* 52 vars */]) = 0
6123  execve("/opt/google/chrome/chrome-sandbox", 
    ["/opt/google/chrome/chrome-sandbox", 
    "/opt/google/chrome/chrome", 
    "--type=zygote", 
    "--enable-crash-reporter=6795275A1128269862CB7A471F5E0228,Ubuntu 12.04.4 LTS"], 
    [/* 55 vars */]) = 0
```

# sendto

```
connect(8, {sa_family=AF_INET, sin_port=htons(9200),
    sin_addr=inet_addr("10.147.177.170")}, 16) = 0
sendto(8,
    "\nB\n5\n3\n(BP-1019336183-10.165.43.39-1400088409498\20\211\200\200\200\4\30\361\7\22\tsnakebite\20\0\30\200\200\200@",
    75, 0, NULL, 0) = 75
```

# recvfrom

```
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

# ftrace: <br> tracing kernel functions


# `/proc`

# `/proc`

* run a program
* delete the executable
* YOU CAN STILL RECOVER IT 

# Understanding your operating system makes you a better programmer

# OKAY AWESOME LET'S LEARN

# Usual strategies

* Read LKML
* Submit patches
* Linus yells at you for being dumb
* Cry

# Our strategies

1. Strace all the things!
1. Read some kernel code!
1. Write a kernel module!
1. Do the Eudalypta challenge
1. Write your own operating system
1. Do an internship

# Strategies for getting started

# Strategy 1: <br> strace all the things!

# Strategy 2: <br> Read some <br> kernel code

# BUT THAT'S TERRIFYING!!!!!

Pick one system call and try to understand one thing about it

# 

Linux kernel: LXR, [`http://livegrep.com`](http://livegrep.com)

OS X kernel: [`http://opensource.apple.com`](http://opensource.apple.com)

# 

<img src="chmod-code.png" class="image">

# 

<img src="chmod-code-crossed-out.png" class="image">

# Strategy 3: <br> Write a <br> Linux kernel module

DEMO DEMO DEMO

# 

<img src="rickroll-init.png" class="image">

# 

<img src="rickroll-init-cleaned-up.png" class="image">

# 

<img src="rickroll-open.png" class="image">

# 

<img src="rickroll-open-cleaned-up.png" class="image">



# Okay no more <br> code I promise

# Strategy 4: <br> Write your own OS

Not as scary as it sounds. I promise!

# Strategy 5: <br> Do the Eudalypta challenge

# Strategy 6: <br> Do a Linux kernel <br> internship

# Linux Internships

+ Google Summer of Code
+ GNOME Outreach Program for Women

# Questions?

`http://github.com/jvns` <br>
`http://twitter.com/b0rk` <br>
`julia@jvns.ca`


Resources:

`http://bit.ly/kernelfun`
