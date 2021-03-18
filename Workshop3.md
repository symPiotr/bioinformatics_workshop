# Workshop 3 (18th March 2021). The Unix environment - advanced topics
&nbsp;  
  
### 3.1. Working on the cluster: logging in, accessing & moving files.

Tools for logging in, copying files, etc. are platform-specific. Hopefully, they work for everybody by now! What tools do you use?  
&nbsp;  
  
### 3.2. Reviewing homework :)

How did you do? What are your solutions?
   * File "OTU_table.txt" contains information on the abundance of various bacterial operational taxonmic units (OTUs) in some 20 insect samples that we have sequenced; the last column contains information about taxonomy. How many OTUs there are that correspond to Gammaproteobacteria other than Sodalis?  
   * File "Phorids_fastq_100_reads.fastq" contains raw sequencing data for phorid flies. How many of the 100 reads contain the sequence "GCCGCGGTAA" corresponding to a conserved portion of one of the amplification files? Save them to a separate file!  
   * "For 100ish \*fastq.gz files in a specified directory, for example /mnt/matrix/symbio/raw_data/20200830_MiSeq/P-\*, copy them to your work directory, gunzip them, and create a file "line_counts.txt" with information on how many lines each file contains, as well as a file "top_reads.fastq" which contains the first read from each of these fastq files."  
&nbsp;  
  
### 3.3. A little test - previously covered material
  
The file "Updated_cicada_collection_data.txt" contains information about some insects that I collected in Chile. Except for the heading line, each subsequent line corresponds info about, among other things, collection_site_ID, genus, species...  
(1) What commands would you use to check how many specimens of Tettigades undata were collected in Lonquimay?  
(2) What commands would you use to create a file containing the heading and lines corresponding to Tettigades undata specimens from Lonquimay?   
  
The folder /mnt/matrix/symbio/workshops/workshop_20210318/data/ contains some of the sequencing reads, in the fastq format, from our latest Oxford Nanopore run!  
(3) How many reads there are, in total, in this folder?  
(4) In your working directory, create a file with the top 10 reads from each of the files in that directory.  
  
&nbsp;  
  
### 3.4. sed - Search and replace

We have previously covered grep - a powerful tool for searching text files.
**sed** - "**s**tream **ed**itor" - is a powerful tool for editing text. It has a challenging syntax, the learning curve is steep, and you want to know regular expressions (which we'll cover during the next classes) to take the full advantage of it. Here, we'll just learn the basics. Check out this tutorial - [https://www.grymoire.com/Unix/Sed.html#uh-0](https://www.grymoire.com/Unix/Sed.html#uh-0) to get a sense of its functionality!  
  
Basic syntax:
```
sed 's/old/new/g' input_file > output_file
```  
  
Applications:
```
sed 's/Eciton/Some_other_name/g' Army_ant_COI_seqs.fasta   # replaces the genus name of an army ant with sth else  

grep ">" Army_ant_COI_seqs.fasta | sed 's/; mitochondrial//g' #removes the last portion of fasta sequence names
  
head -20 Phorids_fastq_100_reads.fastq | sed 's/M01530:53:000000000-J8H3B/Phorid/g' # replaces sequencer/flow cell name in read names in fastq files with the selected words

sed 's/\t/,/g' OTU_table.txt > OTU_table.csv #converts a tab-delimited table into a coma-delimited table
  
sed -i.bak 's/,/;/g' OTU_table.csv # edits "in place"; makes change to a file while creating a backup ".bak" file
```
&nbsp;  

### 3.5. Editing tables - cut, sort, uniq

The command **cut** is most often use for getting selected columns of data from a table - with column numbers specified after the -f flag:  
```  
head OTU_table.txt # a tab-delimited file, with rows corresponding to bacterial "species", columns - samples...
head OTU_table.txt | cut -f 1-3 # let's extract only the first three columns
head OTU_table.txt | cut -f 1-3,5,8-10 # ... or to a more complicated selection!
```  
  
You can specify your delimiter (-d), or display only characters with specific numbers (-c)
Another command, **sort**, sorts lines
```  
head OTU_table.txt
head OTU_table.txt | sort
```  

I have often used it for sorting informatively named sequence headings in my genome assembly files
```
grep ">" /mnt/matrix/symbio/workshops/workshop_20210318/data/scaffolds.fasta | head  # That's how they look 
grep ">" /mnt/matrix/symbio/workshops/workshop_20210318/data/scaffolds.fasta | wc -l # Lots of them!

grep ">" /mnt/matrix/symbio/workshops/workshop_20210318/data/scaffolds.fasta | sort -t "_" -k 6 -r -n | head # Let's find those with the highest coverage!

grep ">" /mnt/matrix/symbio/workshops/workshop_20210318/data/scaffolds.fasta | sort -t "_" -k 6 -r -n | head -1000 | sort -t "_" -k 4 -r -n | head # Let's find 10 longest among the 1000 with highest coverage!
```  
  
The command **uniq** retains only unique values from a SORTED! file.  
For which *Eciton* species we have data in Army_ant_COI_seqs.fasta?

```
grep "Eciton" Army_ant_COI_seqs.fasta
grep "Eciton" Army_ant_COI_seqs.fasta | cut -f 2-3 -d " " | sort | uniq
```  
&nbsp;  
  
### 3.6. Loops

Unix allows you to write short scripts, and loops are an important part of it! We'll talk more about loops when discussing Python, but I wanted to introduce the Unix *for* loop that I use quite often!

Basic syntax:  
```
for variable in [list of variables]; do task1; task2...; done
```
  
Examples:
```
for number in 1 2 3 4; do echo $number; done
for fastq_file in /mnt/matrix/symbio/workshops/workshop_20210318/data/FAP34702*; do echo $fastq_file; done
for fastq_file in /mnt/matrix/symbio/workshops/workshop_20210318/data/FAP34702*fastq; do echo $fastq_file; head -4 $fastq_file; done
```
&nbsp;  
  
### 3.7. Where are the programs we are using? $PATH. .bashrc

The command we have used, like **ls** and others, are little programs that reside somewhere. Where?
```
whereis ls
which ls
```

But often, you will want to use other programs. For example, program **pear** assembles forward and reverse fastq reads
```
cp /mnt/matrix/symbio/raw_data/20200830_MiSeq/P-SZF2Y9-5_S476_L001_R* .
pear -f P-SZF2Y9-5_S476_L001_R1_001.fastq.gz -r P-SZF2Y9-5_S476_L001_R2_001.fastq.gz -o P_SZF2Y9_5
```  
  
But you probably won't be able to do this... your bash doesn't know where to find the program! I can tell you that it resides at /mnt/matrix/symbio/bin/pear, though. Try providing the full path to the program!  

Where is bash searching? Environment variable PATH contains information on all the directories where the program is searching.  

```
echo $PATH
echo $PATH | sed 's/:/\n/g'
```
Consider adding /mnt/matrix/symbio/bin/ to your path!

```
less ~/.bashrc # the system file containing all the critical information!
export "PATH=/mnt/matrix/symbio/bin:$PATH" # that would work for the duration of the session

echo "export PATH=/mnt/matrix/symbio/bin:$PATH" >> ~/.bashrc # this would permanently add the directory to your PATH
source ~/.bashrc
```

**.bashrc** contains many other useful portions. You may not want to mess with most of them, but perhaps, explore aliases!  
  
&nbsp;  
  

### 3.8. Shell scripts




&nbsp;  
  
### 3.9. HOMEWORK!  
  
* The Phorid_fastq_100_reads.fastq file contains some amplicon reads from one of the phorid libraries, in a FASTQ format. Can you convert it to a FASTA format?
* Think of possible applications of Unix in your own research. I'd love to learn how this could have (or will!) saved you some work!
* Re-read chapters focused on Linux/Unix. Follow their exercises.
* Next week, we are getting started on Regular Expressions. Read Chapter 2 of the book!
