



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



## Functions!

def RevCompl(seq):
   RC_dict = {'A':'T', 'T':'A', 'G':'C', 'C': 'G'}
   RCseq = ""
   for base in seq[::-1]
       RCseq += RC_dict[base]
   return(RCseq)


def ImportFasta(input_file):
    input = open(input_file, "r")
    sequence = ""
    heading = ""
    SeqDict = {}
    for line in input:
        if line.startswith(">"):
            if len(heading)>0:
                SeqDict[heading] = sequence
            heading = line.strip().strip(">")
            sequence = ""
        else:
            sequence = sequence + line.strip().upper()
    SeqDict[heading] = sequence
    input.close()
    return(SeqDict)


#### Homeworks/scripts recently.....
1) write a script that exports selected regions of a selected sequence from a multifasta file
``` fasta_regions.py input.fasta requested_seq start_pos end_pos ```
2) if start_pos > end_pos, provide reverse complement!
3) rather than reading name/coords of a single requested sentence, read in a list of multiple!
4) modify the scripts above so that they use functions!

5) use lists or dictionaries, or whatever approach, to write a script that filters an OTU table and only keeps rows and/or columns with total above a certain cutoff

