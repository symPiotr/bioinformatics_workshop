#### regular expressions ######

[ACGTacgt], [0-9], [A\n] - match to either of the characters within square brackets;
[AT]{6,} - a series of not less than six characters listed within brackets; in this case, "AATATATT" or "AAAAATTTT" would both match!
[^XYZ] - a series of any characters other than those listed within the bracket after the ^ character;
 
I - "or" character: 

[A]{6,}|[T]{6,} - a series of not less than six As or of not less than six Ts

[A\n]{6,}|[T\n]{6,} - a series of not less than six (A or \n) or of not less than six (T or \n)... potentially helpful when our sequence is broken across lines!

 

(AT){3,} - a series of not less than three "AT" repeats: "ATATAT" would work, "AATTAATT" wouldn't!

 

######  grep ######

grep is a command-line utility for searching plain-text data sets for lines that match a regular expression. Its name comes from the ed command g/re/p (globally search for a regular expression and print matching lines), which has the same effect.

Good tutorial --- https://www.cyberciti.biz/faq/howto-use-grep-command-in-linux-unix/

Standard help --- type "man grep"


I will skip the basic syntax. Read the tutorial!
Let's move to more exciting stuff - REGEX. The command-line version of grep uses slightly different

syntax than the regular expressions available in TextWrangler. For instance, most versions of grep don't understand
\d, so you will need to specify the range [0-9] instead. The man file for grep explains some of the
command-specific syntax, and you can consult it if something doesn't work as expected.
 
# To use full regular expressions, use:


grep -E = egrep

 

egrep "PL\d{3}" Piotr_army_ant_COI_sequences.fasta --- identifies labels such as PL123; works on my Mac, but not on our cluster

egrep "PL[0-9]{3}" Piotr_army_ant_COI_sequences.fasta --- works on my Mac as well as clusters
 
# Remember that you can grep/egrep within pipelines --- use | to pipe the output of one command to another command, including head, tail, wc, grep...


grep "Eciton" Piotr_army_ant_COI_sequences.fasta | wc -l


egrep "Eciton|Labidus" Piotr_army_ant_COI_sequences.fasta | egrep "PL[0-9]+"
   # ---> This uses egrep to extract lines containing search term "Eciton" or "Labidus", and the output is directed to egrep to extract lines with strain label starting with PL [followed by digits].
 
##############
 
grep is not useful for text replacement in the command line, though. There are other programs that can do that using a variant of REGEX, but both have complicated syntax
sed is simpler. Example usage ---
 
egrep "Eciton|Labidus" Piotr_army_ant_COI_sequences.fasta | sed 's/Eciton/Macrosteles/g'
   # egrep extracts all lines containing the word "Eciton" or "Labidus", and then sed replaces all instances of "Eciton" into "Macrosteles"
 
sed -i 's/Eciton/Macrosteles/g' Piotr_army_ant_COI_sequences.fasta
   # in the file, replaces all instances of "Eciton" into "Macrosteles".

More examples at https://linuxconfig.org/learning-linux-commands-sed !
awk is another, powerful text editing tool, but with much more complicated syntax. Read about it at your own risk!
 
There are other useful tools for working with text files:
cut extracts selected columns from the line. Particularly useful when working with tables!
cut -f 1,3 --- would extract columns #1 and #3 from lines in the text. By default, it assumes that line is tab-delimited.
cut -f 2 -d " " --- would extract column #2 from lines in the text delimited by spaces.
 
sort sorts lines of text
sort -k 2  -t " " --- would sort lines of text based on the second column (lines delimited by spaces)
sort -k 6  -t "_" -n -r --- I often used this to sort fasta headings in Spades assembler output, such as "NODE_2_length_54722_cov_10.053_ID_5528". In this case, based on the sixth column following delimitation by underscores [=coverage], assuming that this is a numeric value rather than text, and sorting in the descending order.
 
uniq selects unique lines in a sorted file.
 
Example usage of these three commands:
grep ">" Piotr_army_ant_COI_sequences.fasta | cut -f 2,3 -d " " | sort | uniq --- lists species for which COI sequences are available in this file.... assuming the genus+species name is always represented by the 2nd and 3rd column in space-delimited lines (="words")
 
However, this ignores the fact that some species are labelled like this --- "Neivamyrmex sp. 2 PL-2016", so with the name split across four words (numbered 2-5). But in other sequences, words 2-5 look like this --- "Labidus praedator isolate PL039" ... Fortunately, we can use sed to remove the word "isolate" and any subsequent stuff from all lines!

grep ">" Piotr_army_ant_COI_headings.txt | sed 's/isolate.*//g' | cut -f 2- -d " " | sort | uniq

That should provide the full list of species in the fasta file!
