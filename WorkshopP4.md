# Workshop P4 (10th June 2021). Modules and output formatting.
  
### P4.1. Homework --- how did you do?

1. The example discussed above works when each sequence is provided as a single line. But in a large proportion of fasta files, the sequence is broken up across multiple lines:
```
>RealWorldSequence1
ACTGTCATGTCATGTTGTCATGTCATGAT
TCGATAATGACATGTCATGATTGTCAT
```  
But we can deal with that! Write a script that converts fasta files with sequences broken up across multiple lines into files where each sequence is in a single line.
  
&nbsp;  
2. Last week, we wrote a script that computes basic statistics (length, count of Ns, GC%) for a single user-provided nucleotide sequence. Rewrite the script so that it summarizes all sequences in a multifasta file.  
  
&nbsp;  
3. Write a script that converts sequences in the `fastq` format to `fasta` format.  
  
&nbsp; 
  
### P4.2. Modules

Python3 in its basic mode provides lots of tools and options... But sometimes you'll want to use a bit more!
You can substantially increase the functionality by importing `modules` - additional sets of tools.  
&nbsp;
Some of them are provided essentially by default with python3. Three such modules I use often:  
* [**sys** - System-specific parameters and functions](https://docs.python.org/3/library/sys.html)   
* [**os** - Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html)  
* [**re** - Regular expression operations](https://docs.python.org/3/library/re.html)  

&nbsp; 
Others need to be installed, which can be a bit of a pain as they may require permissions, various dependencies, etc.  
Examples that I have used: `biopython`, `pysam`.   

&nbsp; 
##### Example: sys - working with file names provided as arguments 
```
import sys     # imports module - the tools within sys become available!

   ### This statement allows you to use arguments provided at the time the program is run
   ### as variables within your script! In this example, there are two of them.
if len(sys.argv) != 3:
    sys.exit('\nThis script imports an input_file and exports an output_file. Please provide file names.\n'
	           'Usage: ./script.py <input_file> <output_file>\n')   
Script, path_to_input_file, path_to_output_file = sys.argv

INPUT = open(path_to_input_file, "r")
OUTPUT = open(path_to_output_file, "w")
  
```  
&nbsp;  





##### Example: sys - stopping the script when encountering unexpected characters
```
for base in nucleotide_sequence:
    if base not in 'ACGTN':
        sys.exit('\nError! Encountered an incorrect character %s in sequence %s. Exiting...' % (base, nucleotide_sequence))
```    
  
##### Let's now edit our Homework scripts following the examples above so that they work with input files provided by the user!  
  
&nbsp;  
&nbsp;  
##### Example: os - working with folders and files
```
>>> import os
>>> os.system("ls -l")
total 140
-rw-rw-rw- 1 piotr.lukasik users 62826 Jun 10 05:34 Army_ant_COI_seqs.fasta
drwxr-xr-x 2 piotr.lukasik users  4096 Jun 10 05:53 test_dir
0
>>> os.system("mv test_dir test_dir2")
0
>>> os.path.exists("test_dir")
False
>>> os.path.exists("test_dir2")
True
>>> if not os.path.exists("test_dir"):
...     os.system("mkdir test_dir")
... 
0
>>> os.system("ls -l")
total 144
-rw-rw-rw- 1 piotr.lukasik users 62826 Jun 10 05:34 Army_ant_COI_seqs.fasta
drwxr-xr-x 2 piotr.lukasik users  4096 Jun 10 05:57 test_dir
drwxr-xr-x 2 piotr.lukasik users  4096 Jun 10 05:53 test_dir2
```
&nbsp;  
&nbsp;  
### P4.3. Formatting output

How to make your text pretty --- or just organized in a way it needs to be? Let's look at alternative ways:

```
>>> FIRST_NAME = "John"
>>> AGE = 25
>>> 
>>> 
>>> print("Your name is", FIRST_NAME, ", you are", AGE, "years old.")
Your name is John , you are 25 years old.
>>>
>>> print("Your name is ", FIRST_NAME, ", you are ", AGE, " years old.", sep = "", end = "\n") # changing the separator from default
Your name is John, you are 25 years old.
>>>
>>> print("Your name is %s, you are %s years old" % (FIRST_NAME, AGE))
Your name is John, you are 25 years old
>>>
>>> print("Your name is {}, you are {} years old".format(FIRST_NAME, AGE))
Your name is John, you are 25 years old
>>>
>>> print(f"Your name is {FIRST_NAME}, you are {AGE} years old.")
Your name is John, you are 25 years old.
```
You can find more info about these methods online, for example at [https://realpython.com/python-string-formatting/#4-template-strings-standard-library](https://realpython.com/python-string-formatting/#4-template-strings-standard-library).  
Personally, I tend to use the "legacy" method #2, using "%" characters. The most straightforward method #4 is only available from Python 3.6 onwards, which may or may not be a problem for you!
 
These methods do allow you to format values, which can be a handy way of making your output more pretty :)  
  
```
>>> My_value = 0.12345
>>> 
>>> print("%f" % My_value)
0.123450
>>> print("%.2f" % My_value)   # Two digits after the dot!
0.12
>>> print("%8.2f" % My_value)   # Two digits after the dot, the number should occupy eight spaces in total!
    0.12
```

Text formatting can be very helpful when managing file/sample names for many different purposes. For example, when using the `os.system()` function to feed information directly to shell!
  
&nbsp;  
&nbsp;  
### P4.4. Scripts to write!

##### Option 1: Writing a script that only outputs selected bases from a sequence in a fasta file.  
  
##### Option 2: Writing a script that works on tables - computes and check totals
  
##### Option 3: Your idea?  
  


