# Workshop 2. (11th March 2021). Working with text files in the Linux environment

### 2.1. Working on the cluster: logging in, copying files. htop.



htop

### 2.2. Brief recap of basic commands: pwd / ls / cd / mkdir / touch / cp / mv / rm

* 1. In your home directory on the cluster, make directory "workshop".
* 2. In this directory, make directory "workshop_20210311"
* 3. In this directory, make directory "files"
* 4. In /mnt/matrix/symbio/bioinfo_workshops/workshop_20210311/, there are some files. What are they? Copy them to your own "workshop_20210311" directory.
* 5. Sorry, I meant to "files". Move them to "files"!
* 6. Sorry, the extension of one of the files is wrong. Change the extension of "Army_ant_COI_seqs.txt" to "fasta"!
* 7. Ooops, the files with the name starting with "SPH" shouldn't have been there at all. Remove them! 
* 8. How many files are there in your "files" folder? Which one is the largest?
&nbsp;  
  
### 2.3. Folder and file permissions. chmod.

*ls* command lists directory contents, *ls -l* (often called via alias *ll*) provides details about files. Let's took at them!  
&nbsp;  
```
(base) piotr.lukasik@azor:~$ ll
total 684
drwxr-xr-x  3 piotr.lukasik users   4096 Dec 25 19:15 splitting/
lrwxrwxrwx  1 piotr.lukasik users     18 May 14  2020 symbio -> /mnt/matrix/symbio/
-rw-r--r--  1 piotr.lukasik users 123326 Feb  5 15:03 temp.1407573.fsa
...
```  
&nbsp;  
the first column contains info about permissions. You may want them changed!  
[https://www.tutorialspoint.com/unix/unix-file-permission.htm](https://www.tutorialspoint.com/unix/unix-file-permission.htm)  







### 2.4. Displaying file contents in an interactive mode: less, nano.
*less* is a convenient, interactive file text browser, included in most Unix/Linux distributions.
Info and many keybord shortcuts are at https://pl.wikipedia.org/wiki/Less_(Unix)
When you're ready, type
```
less your_file.name
```  
&nbsp;  
*nano* is 

### 2.5. Streaming text - cat. Top and bottom lines: head, tail. Redirecting output. Getting basic stats: wc

### 2.6. Searching text files - grep

### 2.7. Pipes

### 2.8. Modifying text - sed

Practical examples and exercises  
