# Workshop 2. (11th March 2021). Working with text files in the Linux environment
&nbsp;  
  
### 2.1. Working on the cluster: accessing t, copying files. htop.

Tools for logging in, copying files, etc. are platform-specific. Hopefully, everybody has managed to get them to work :)  
  
Cluster etiquette... if you are planning any substantial jobs, requiring many cores or lots of memory, make sure to book your slot! Piotr Zieliński (piotr.zielinski@uj.edu.pl) manages the *molecol_cluster* Google group that provides access to the calendar. If you're planning to work there, make sure you get added!   
&nbsp;  
  
Before working on the cluster, you want to check what is going on. *htop* is the tool that allows you to do that.  

&nbsp;  
  
### 2.2. Brief recap of basic commands: pwd / ls / cd / mkdir / touch / cp / mv / rm
  
OK, so here are some jobs for you!  
* In your home directory on the cluster, make directory "workshops".
* In this directory, make directory "workshop_20210311"
* In this directory, make directory "files"
* In /mnt/matrix/symbio/workshops/workshop_20210311/, there are some files. What are they? How big they are? In megabases?
* Copy the files to your own "workshop_20210311" directory.
* Sorry, I meant to "files". Now move them to "files"!
* Sorry, the extension of one of the files is wrong. Change the extension of "Army_ant_COI_seqs.txt" to "fasta"!
* Ooops, files with the name starting with "SPH0121" shouldn't have been there at all. Remove them! 
* How many files are there in your "files" folder now? Which one is the largest?  
* Files with the name starting with "SPH0120" are compressed using gzip. You can uncompress them by typing "gunzip file_name". How big is the largest file now?
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
*chmod* is the tool that you want to use.
[https://www.tutorialspoint.com/unix/unix-file-permission.htm](https://www.tutorialspoint.com/unix/unix-file-permission.htm)  
&nbsp;  
  

### 2.4. Displaying file contents in an interactive mode: less, nano.
*less* is a convenient, interactive file text browser, included in most Unix/Linux distributions.
Info and many keybord shortcuts are at https://pl.wikipedia.org/wiki/Less_(Unix)
When you're ready, type:  
```
less your_file_name
```  
&nbsp;  
*nano* is a command-line text editor that can be really helpful for quick on-site edits, but also bigger jobs.
Type:  
```
nano your_file_name
```  
... to create an empty file or open an existing file, and use keystrokes to navigate [https://www.nano-editor.org/dist/latest/cheatsheet.html](https://www.nano-editor.org/dist/latest/cheatsheet.html)  
&nbsp;  
  
### 2.5. Redirecting output. 

Rather than creating empty files and then filling them with stuff, we can easily direct stuff to a file! We can use the character "greater than" --- ">" for that.  
In your working directory, type:  
```
ls -l > dir_contents.txt
history > current_history.txt
```  
Now, have a look at the output!  
  
Note that ">" creates a file and may **overwrite** file with the same name that was there before!  
Alternatively, in some cases, you may want to use ">>", or "append" instead, which appends contents to the end of the file if one exists.  
&nbsp;  
  
### 2.6. Displaying and joining files - cat. Top and bottom lines - head, tail. Getting basic stats: wc

   * **cat** --- dumps the whole file contents into terminal
   ```
   cat Army_ant_COI_seqs.txt
   cat file1 file2 file3
   ```  
   * **head** --- displays the top lines of the file only. 10 by default.
       - but you can use it with arguments to change the default. How?
   ```
   head Army_ant_COI_seqs.fasta
   head -1 Army_ant_COI_seqs.fasta
   ```  
   * **tail** --- displays the last lines of the file only. 10 by default.
   ```
   tail -20 Phorids_fastq_100_reads.fastq
   ```  
   * **wc** --- "word count" - counts lines, words, bites for selected files
       - you'll often want to display only one of these values, and there is an argument for that!
   ```
   wc Phorids_fastq_100_reads.fastq
   wc -l Phorids_fastq_100_reads.fastq
   ```  
&nbsp;  
  
### 2.7. Searching text files using grep. Pipes.

**grep** is a powerful, versatile and extremely helpful tool for processing text files. It comes in many flavors - but we will start with fairly basic syntax: "grep SearchTerm SearchedFile".  
   ```
   grep "Eciton" Army_ant_COI_seqs.fasta
   grep ">" Army_ant_COI_seqs.fasta   # quotation marks quite critical!
   grep "@M01530" Phorids_fastq_100_reads.fastq > fastq_headings.txt
   ```  
   - there are multiple arguments that you can be very helpful! What are they?  
   ```
   grep -A 1 "Eciton" Army_ant_COI_seqs.fasta    # lists also N lines after each identified text string!  
   grep -B 2 "Eciton" Army_ant_COI_seqs.fasta    # lists also N lines before those identified
   grep -v "Eciton" Army_ant_COI_seqs.fasta      # lists lines WITHOUT the specified string
   ```     
&nbsp;   
But what makes it all really useful is the ability to "pipe" commands, directing output of one as input for another. Use the "|" character to separate commands
   ```
   grep "Eciton" Army_ant_COI_seqs.fasta | wc -l
   grep "Eciton" Army_ant_COI_seqs.txt | grep -v "burchellii"
   ```  
... and uncountable other options. Let's try some of them!  
&nbsp;  
  
### 2.8. Homework!
   * File "OTU_table.txt" contains information on the abundance of various bacterial operational taxonmic units (OTUs) in some 20 insect samples that we have sequenced; the last column contains information about taxonomy. How many OTUs there are that correspond to Gammaproteobacteria other than Sodalis?
   * File "Phorids_fastq_100_reads.fastq" some raw sequencing data for phorid flies. How many of the 100 reads contain the sequence "GCCGCGGTAA" corresponding to a conserved portion of one of the amplification files? Save them to a separate file!
   * Read Chapter 6 of the book!
   * Remember to send me your data examples if you want us to work on them :)
