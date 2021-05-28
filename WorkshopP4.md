



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
