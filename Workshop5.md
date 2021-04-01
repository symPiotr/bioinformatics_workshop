# Workshop 5 (1st April 2021). Getting deeper into regular expressions!

### 5.1 Last week's REGEX exercises: how did you do?

### 5.2 regular expressions: recap of some more complicated options, and some new ones :)

[ACGTacgt], [0-9], [A\n] - match to either of the characters within square brackets;  
  
[AT]{6,} - a series of not less than six characters listed within brackets; in this case, "AATATATT" or "AAAAATTTT" would both match!  
  
[^XYZ] - a series of any characters other than those listed within the bracket after the ^ character;  
  
**| - "or" character:**  
[A]{6,}|[T]{6,} - a series of not less than six As OR of not less than six Ts.  

[A\n]{6,}|[T\n]{6,} - a series of not less than six (A or \n) or of not less than six (T or \n)... potentially helpful when our sequence is broken across lines!  
  
(AT){3,} - a series of not less than three "AT" repeats: "ATATAT" would work, "AATTAATT" wouldn't!  
  
&nbsp;  
  
### 5.3 Using REGEX within grep

As you remember, grep is a command-line utility for searching plain-text data sets for lines that match a regular expression. Its name comes from the ed command g/re/p (globally search for a regular expression and print matching lines), which has the same effect.
Standard help --- type "man grep". But you know the basic syntax already!  
Good tutorial --- https://www.cyberciti.biz/faq/howto-use-grep-command-in-linux-unix/ 
  
But let's move to more exciting stuff - REGEX.  
The command-line version of grep uses slightly different syntax than the regular expressions available in TextWrangler. For instance, most versions of grep don't understand \d, so you will need to specify the range [0-9] instead. The man file for grep explains some of the command-specific syntax, and you can consult it if something doesn't work as expected.  

**grep** understand with three different versions of regular expressions:
   * basic (BRE) - default
   * extended (ERE)
   * perl (PCRE)

In **BRE**, special characters that we have learnt about: *?, +, {, |, (,* and *)* lose their special meaning; instead use the backslashed versions \?, \+, \{, \|, \(, and \).  
**PCRE** contains some additional options and different rules relative to what we have learnt.
**ERE** is the closest to what we have learnt. To avoid confusion, I recommend defaulting to ERE!  

To use extended regular expressions, use:
`grep -E` or `egrep`

How to identify labels such as PL123 in the collection of army ant COI sequences?
`
egrep PL\d+" Piotr_army_ant_COI_sequences.fasta
`    
--- this works on my Mac, but not on our cluster! Remember that \d is not routinely recognized, use [0-9] instead!      
`
egrep "PL[0-9]+" Piotr_army_ant_COI_sequences.fasta
`  
--- now it works on the cluster! If we used BRE (grep), it wouldn't have.  
   
Remember that you can grep/egrep within pipelines --- use | to pipe the output of one command to another command, including head, tail, wc, grep...  
`
  grep "Eciton" Piotr_army_ant_COI_sequences.fasta | wc -l
  egrep "Eciton|Labidus" Piotr_army_ant_COI_sequences.fasta | egrep "PL[0-9]+"  
`  
  
  &nbsp;  
    
### 5.4 Using REGEX within sed
 
**grep** is not useful for text replacement in the command line, though. There are other programs that can do that using a variant of REGEX, but the two most powerful have somewhat complicated syntax.  
  
`tr`  is a relatively simple text-edit tool.  
`awk` is yet another, powerful text editing tool, but with much more complicated syntax. Read about it at your own risk!  
  
**sed with the "s" command** may be a good balance between simplicity and utiity! And you know it already :) Again, basic syntax ---  
`sed 's/old_term/new_term/g' old_file.txt > new_file.txt`
  
Examples ---  

`egrep "Eciton|Labidus" Army_ant_COI_seqs.fasta | sed 's/Eciton/Macrosteles/g'`
   -> egrep extracts all lines containing the word "Eciton" or "Labidus", and then sed replaces all instances of "Eciton" into "Macrosteles"

`sed 's/Eciton/Macrosteles/g' Army_ant_COI_seqs.fasta > seq_names_make_no_sense.fasta`
   -> sed replaces all instances of "Eciton" into "Macrosteles", saves the contents with new name

`sed -i.bak 's/Eciton/Macrosteles/g' Army_ant_COI_seqs.fasta`
   -> sed with the parameter "-i" does the replacements in the file, keeping the original version of the file as a backup, with the extension specified (here: bak).  
  
More examples at https://linuxconfig.org/learning-linux-commands-sed !  
  
&nbsp;  
  
To use extended regular expressions with sed, use the parameter -r or -E. Examples:  
  
`grep ">" Army_ant_COI_seqs.fasta | sed -r "s/(KX[0-9]+).*/\1/g"` should only keep the first portion of the heading, corresponding to KX followed by digits. All other parts of the heading are removed.  
  
Unfortunately, sed does not detect end-of-line characters. If needed, we can always look for a workarounds, for example removing them using `tr -d '\n'`, or temporarily replacing them into something else as a part of the pipe `tr '\n' '@'` :D Your search engine is your friend :)  
  
### 5.5 Exercises --- REGEX in command line! 

Basically, I would like you to redo last week's exercises, but not in your text editor but in command line, using grep+sed. 
  
**How do we replace headings in the Army_ant_COI_seqs.fasta** from something like this:  
*>KX983305.1 Eciton burchellii isolate PL041 cytochrome oxidase subunit I (COI) gene, partial cds; mitochondrial*  
to something like this:  
*>KX983305_Eciton_burchellii_PL041*   
using grep/sed alone?  
   
How do we convert **Phorids_fastq_100_reads.fastq** to fasta format using sed/grep?  

From the resulting fasta file, **how do we only export reads containing the primer sequence** GTGYCAGCMGCCGCGGTAA (preceded by up to three other nucleotides) **AND at the same time, trim the primer**?  
  
And so on... Last week's homework had five tasks, and you should be able to do all of them in the command line.  
  
Good luck, and have fun! :) 

