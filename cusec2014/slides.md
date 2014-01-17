# You can be a <br>kernel hacker

by Julia Evans <br>
[twitter.com/b0rk][twitter]  <br>
[github.com/jvns][github]  <br>
[jvns.ca][website]  <br>

[twitter]: https://github.com/jvns
[github]:  https://twitter.com/b0rk
[website]: http://jvns.ca

# 

<img src="hackerschool_logo.png" id="hackerschool">

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

TODO FIX THIS AND MAKE IT PRETTY

```c
static int chmod_common(struct path *path, umode_t mode)
{
    struct inode *inode = path->dentry->d_inode;
    struct iattr newattrs;
    int error;

    error = mnt_want_write(path->mnt);
    if (error)
        return error;

    mutex_lock(&inode->i_mutex); // Lock to prevent a race condition!

    error = security_path_chmod(path, mode); // Make sure we're allowed to do this
    if (error)
        goto out_unlock;
    newattrs.ia_mode = (mode & S_IALLUGO) | (inode->i_mode & ~S_IALLUGO);
    newattrs.ia_valid = ATTR_MODE | ATTR_CTIME;
    error = notify_change(path->dentry, &newattrs);
out_unlock:
    mutex_unlock(&inode->i_mutex); // We're done, so the mutex is over!
    mnt_drop_write(path->mnt); // ???
    return error;
}
```

# Strategy 2: <br> Write a <br> kernel module

DEMO DEMO DEMO

# 

```
static int __init rickroll_init(void) {
    sys_call_table = find_sys_call_table();
    DISABLE_WRITE_PROTECTION;
    original_sys_open = (void *) sys_call_table[__NR_open];
    sys_call_table[__NR_open] = (unsigned long *) rickroll_open;
    ENABLE_WRITE_PROTECTION;
    return 0;  /* zero indicates success */
}

static void __exit rickroll_cleanup(void)
{
    printk(KERN_INFO "Ok, now we're gonna give you up. Sorry.\n");

    /* Restore the original sys_open in the table */
    DISABLE_WRITE_PROTECTION;
    sys_call_table[__NR_open] = (unsigned long *) original_sys_open;
    ENABLE_WRITE_PROTECTION;
}
```

#

```
static char *rickroll_filename = "/home/bork/media/music/Rick Astley - Never Gonna Give You Up.mp3";

asmlinkage long rickroll_open(const char __user *filename, int flags, umode_t mode)
{
    int len = strlen(filename);

    if(strcmp(filename + len - 4, ".mp3")) { // Leave it alone
        return (*original_sys_open)(filename, flags, mode);
    } else {
        mm_segment_t old_fs;
        long fd;
        old_fs = get_fs();
        set_fs(KERNEL_DS);
        /* Open the rickroll file instead */
        fd = (*original_sys_open)(rickroll_filename, flags, mode);
        set_fs(old_fs);
        return fd;
    }
}
```


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

<img src="apple-email.png" id="apple">

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
