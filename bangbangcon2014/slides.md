# Spying on your programs with strace

by Julia Evans <br>
[`twitter.com/b0rk`][twitter]  <br>
[`github.com/jvns`][github]  <br>
[`jvns.ca`][website]  <br>

[github]: https://github.com/jvns
[twitter]:  https://twitter.com/b0rk
[website]: http://jvns.ca


# Disclaimer: <br>Linux-only

# Debugging:

+ look at the source code
+ add print statements
+ know the programming language

# strace <br> = <br> wizardry

# System calls: <br> a OS's API

# System calls

+ execve
+ open
+ write
+ sendto/recvfrom

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
$ strace -etrace=open google-chrome
open("/home/bork/.cache/dconf/user", O_RDWR|O_CREAT, 0600) = 10
open("/home/bork/.config/dconf/user", O_RDONLY) = 10
open("/home/bork/.config/google-chrome/Consent To Send Stats", O_RDONLY) = 34
open("/home/bork/.config/google-chrome/Local State", O_RDONLY) = 34
open("/home/bork/.gtkrc-2.0", O_RDONLY) = 15
open("/home/bork/.pulse/client.conf", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
open("/home/bork/.pulse-cookie", O_RDWR|O_CREAT|O_NOCTTY|O_CLOEXEC, 0600) = 32
open("/home/bork/.Xauthority", O_RDONLY) = 12
open("/home/bork/.Xdefaults-kiwi", O_RDONLY) = -1 ENOENT (No such file or directory)
```

# 
