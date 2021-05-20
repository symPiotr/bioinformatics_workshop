#! /usr/bin/env python3

### This script takes user-provided input nucleotide sequence, for example "ACCCTG", and outputs its reverse complement, for example, "CAGGGT".

# 1. Ask user for input sequence, convert it to upper case, and save it as a string variable.
Input_seq = input("Type your sequence: ").upper()

# 2. Provide a dictionary of complementary nucleotides
Complements = {'G': 'C', 'C': 'G', 'A': 'T', 'T': 'A', 'N': 'N'}

# Read sequence from the end, and for each base obtain a complementary base, and add it to the new "Reverse complement" string.
Reverse_complement = ""  
Seq_correct = 1          # The value will be changed to 0 if any illegal characters, other than ACGTN, are discovered in the sequence

for base in Input_seq[::-1]:                      # Reading the sequence from the end to the beginning, for each base,
    if base in 'ACGTN':                           # If base is "legal", 
        Reverse_complement += Complements[base]   # Add its complement to "Reverse_complement" string.    
    else:                                         # Otherwise set the "Seq_correct" value to 0 -> no output will be provided.
        Seq_correct = 0
    
# Print the reverse complementary sequence to standard output
if Seq_correct == 1:
    print("Reverse complement: " + Reverse_complement)
else:
    print("Sequence contains illegal characters!")

