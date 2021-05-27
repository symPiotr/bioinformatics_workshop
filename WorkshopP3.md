# Workshop P3 (27th May 2021). The first Python scripts.
  
### P3.1. Homework --- how did you do?
"write a script that would compute basic statistics for a user-provided sequence: length, count of Ns, and GC%."
* How would you organize it?  
&nbsp;  
  
### P3.2. Looping through a string --- getting creative?
Last week, we reverse-complemented a nucleotide sequence: reversed it and then read base after base:
> ```
> Reversed_seq = Input_seq[::-1]
>
> for base in Reversed_seq:
>    compl_base = Complements[base]
>    Reverse_complement += compl_base
> ```  

--- or alternatively, we read the input sequence in the reverse order:
> ```
> for base in Input_seq[::-1]: 
>     Reverse_complement += Complements[base]
> ```  

Now, how would you approach the problem of **translating** a nucleotide sequence: reading three nucleotides from a sequence at a time?  


### P3.3. Working with files
Capturing user-typed input is not usually very convenient! Much of the time, we want to work with files.  
> ```
> InputFile = open("InputFile.txt", "w")
> for line in file:
>     #### do something 
> InputFile.close()
>
> 
> OutputFile = open("OutputFile.txt", "r")
> print("Your contents", file = OutputFile)
> OutputFile.close()
> ```  
   
How shall we compute the basic sequence statistics for the whole fasta file?  
   



