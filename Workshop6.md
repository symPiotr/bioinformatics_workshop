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
How to list the directories where the software searches for programs?
```
echo $PATH             
```    
&nbsp;  
You can edit the $PATH.
```
export PATH=$PATH:/your/new/path/here
```   
... will add the new directory for the duration of the session. Or you can add it to your ~/.bashrc file to make it permanent!  
&nbsp;  
  
### 6.3. conda
Conda is a package manager and environment manager that you use within command line environment. 
Check [https://conda.io/projects/conda/en/latest/user-guide/getting-started.html](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html) for a tutorial!
  
Follow the instructions in the command prompt on how to install!

```
conda info --envs         # lists available environments
conda activate bio        # starts bio environment
conda deactivate          # deactivates environments
```
&nbsp;
  
### 6.4. Help with our latest sequencing data! 
On Tuesday, we have got some 400 Gb of sequencing data, ~10,000 files... but the file organization makes it hard to work with! You can find a subset at */mnt/matrix/symbio/workshops/workshop_20210408/*.   

*00_sample_info.txt* contains the list of our desired sample names, e.g., WPA0001, and the IDs that the sequencing facility provided, e.g., P20259_1001.  
For each of the samples, we have got an LST file (listing file names), MD5 file (listing MD5 accessions), and a series of folders at the end of which are **two** sets of fastq.gz files corresponding to raw data.  
MD5 files can be used to check data integrity:
```
md5sum -c P20259_1099.md5
```  
   
1. You want to check the integrity of all files.
2. You then want to concatenate R1 files and R2 files for each sample, and put the resulting fastq files for all samples to a single folder, under the name that corresponds to the one **we** had assigned, e.g., WPA0001_R1.fastq.gz & WPA0001_R2.fastq.gz
  
&nbsp;  
  
