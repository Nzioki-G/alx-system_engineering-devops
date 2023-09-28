# Loops, conditions and parsing

## Topics covered:<br>
<mark>DevOps</mark> <br> <mark>Shell</mark> <br> <mark>Bash</mark> <br> <mark>Scripting</mark>
<br>
<br>

## SSH
To generate an SSH RSA key, run ```blah```
    The ```ssh-keygen``` generates, manages and converts auth keys. If type of key is not specified [```-t OPTION```], an RSA key is generated.

<br>

## Portable scripts
To make a sure a script is <b>portable</b> across different UNIX like OSs you use
```#!/usr/bin/env``` instead of just ```#!/usr/bin```

```
$ man bash
$ man env
```
<br>

## Bash
* The syntax of a ```for``` loop in bash is: <br>
```for var in LIST; do COMMANDS; done```

* The syntax of a ```while``` loop in bash is: <br>
```while CONTROL-CMD; do CONSEQUENT-CMDs; done```

* The syntax of a ```until``` loop in bash is: <br>
```until TEST-COMMAND; do CONSEQUENT-COMMANDS; done```

* The syntax of a ```if``` statement in bash is: <br>
```if / [elif] CONDITION; then ACTIONS; fi```

<br>



## Sources:
* Vivek Gite, <a href=https://www.cyberciti.biz/tips/finding-bash-perl-python-portably-using-env.html>Make Script Portable</a>

* ```man ssh-keygen```
* How to set up SSH auth keys: <a href=https://askubuntu.com/questions/61557/how-do-i-set-up-ssh-authentication-keys>ask Ubuntu</a>
* Machtelt Garrels 2008, Bash Guide for Beginners: <a href=https://tldp.org/LDP/Bash-Beginners-Guide/html/>html</a>