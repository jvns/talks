# You can be a <br>kernel hacker

by Julia Evans <br>
[twitter.com/b0rk][twitter]  <br>
[github.com/jvns][github]  <br>
[jvns.ca][website]  <br>

[twitter]: https://github.com/jvns
[github]:  https://twitter.com/b0rk
[website]: http://jvns.ca

# 

<img src="hackerschool_logo.png" class="image">

# Where we're going

1. WTF is a kernel?
2. Why should you care?
3. Strategies for getting started with kernel programming
    a. Read some kernel code!
    b. Write a kernel module!
    c. Write your own operating system
    d. Do an internship

# 1. WTF is a kernel?

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

# System calls: <br> a kernel's API

* open a file! (`open`)
* start a program! (`execve`)
* change a file's permissions! (`chmod`)

# What we've learned 

+ Your kernel does tons of stuff
+ Programs tell it what to do using system calls

# 2. Why should you care?

+ People will think you're a badass
+ You'll become a better programmer

# 3. Strategies for getting started

# Strategy 1: <br> Read some <br> kernel code

# BUT THAT'S TERRIFYING!!!!!

Pick one system call and try to understand one thing about it

# 

Linux kernel: LXR, [http://livegrep.com](http://livegrep.com)

OS X kernel: TODO FIND THIS IT IS IMPORTANT

# 

<img src="chmod-code.png" class="image">

# 

<img src="chmod-code-crossed-out.png" class="image">

# Strategy 2: <br> Write a <br> kernel module

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

# Strategy 3: <br> Write your own OS

# Strategy 4: <br> Do a kernel internship

# Internships

+ Google Summer of Code
+ GNOME Outreach Program for Women

# Blogging = awesome

While at Hacker School:

+ I wrote 50 blog posts
+ 7 of them were on Hacker News
+ 1200 people followed me on Twitter
+ 100,000 people visited my blog
+ Lots of those blog posts are bad. Nobody cares about the bad posts.

#

<img src="apple-email.png" class="image">

# Talk to me!

+ Hacker School
+ All-Girl Hack Night / PyLadies
+ Data science
+ Interviewing
+ Promoting yourself

# Questions?

`http://github.com/jvns` <br>
`http://twitter.com/b0rk` <br>
`julia@jvns.ca`


Resources:

`http://bit.ly/kernelfun`
