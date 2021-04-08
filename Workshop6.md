# Workshop 6 (8th April 2021). Unix & REGEX in the real world :)

### 6.1. Last week's REGEX exercises: how did you do?

### 6.2. screen
Typically, a Unix session lasts for as long as you have an active connection to the cluster. If your job takes 24h, and you want to go home and bring your laptop with you at some point, you have a problem...   
**screen** software allows you to create and manage virtual Unix sessions. Check out the tutorial at [https://linuxize.com/post/how-to-use-linux-screen/](https://linuxize.com/post/how-to-use-linux-screen/)
&nbsp;   

```
screen --version       # check if the software works!
screen -S MySession    # starts a new virtual session
Ctrl + a,  ?           # lists your various options
Ctrl + a d             # leaves the session
screen -ls             # lists active sessions
screen -r MySession    # rejoins an existing session
screen -rd MySession   # rejoins an existing session, forcing the software to 
exit                   # kills the virtual session
Ctrl + a, :quit        # kills the virtual session
```  
&nbsp;  
### 6.2. $PATH and .bashrc
Where does your shell look for programs?
```
ls                     # starts a program "ls" located somewhere...
whereis ls             # lists all instances of "ls" that the shell can see
which ls               # lists path to the instance of "ls" that it is going to run when you type "ls"!
```  
&nbsp; 
How to list the directories where the software searches?



### 6.3. conda
Conda is a package manager and environment manager that you use within command line environment. 


### 6.4. Help with our latest sequencing data! 
On Tuesday, we have got some 400 Gb of sequencing data... but the file organization is weird. 

