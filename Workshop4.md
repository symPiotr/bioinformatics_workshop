


### Getting the right text editor
* Mac: TextWrangler / BBedit, ...
* Windows: Notepad++, .....
* Linux: ?

### What is a text file?
* Wikipedia: "a kind of computer file that is structured as a sequence of lines of electronic text"
* File containing text organized in a human-readable way
* All lines carry information
* Compare TXT vs DOCX vs GZ!


### The organization of data within a text file
* In most cases, data is organized as character-delimited text.
    - Lines typically correspond to distinct observations/measurements
    - Within each line, sections correspond to different types of information
    - Delimiter: comma, space, tab...
    - Blocks of text are enclosed within quotation marks
    - Header
* Special formats: FASTA, FASTQ... suggestions of others?

### Terms and challenges
* Character types: word, numeric, whitespace, special...
* End-of-line (EOL) --- there is a character/characters for that! Represented by different character combinations on different platforms!
    - Linux: LF (line feed) "\n"
    - some older Macs: CR (carriage return) "\r"
    - Windows: LF followed by CR "\n\r"
    - Be aware of that!

### REGEX - Regular Expressions: a widespread language for search and replace
Permit complex text manipulations across a wide range of environments using one skill set!  
Easiest to get started in your REGEX-compatible text editor :)  

Basic search-replace that you can do in almost any editing software:
  * Find: A     ---> Replace: B  
  * Find: Word1 ---> Replace: Word2  
    
But you can go beyond once you learn how to use wildcards!  
  * **\w** --- any letter (A-z) or digit (0-9) and the underscore character (_).  
  * **\d** --- any digit (0-9).  
  * **\t**, **\r**, **\n** --- whitespace characters
  * **\s** --- any whitespace character (space, tab, end-of-line)   

The letters used to form wildcards are case sensitive: \W, \D, \S mean just the opposite!  

  * **.** --- any character
  * **[CGTAcgta]**, **[A-Z]**  --- one of the specified characters, or characters in the range  
  * **[^CGTAcgta]**, **[^A-Z]** --- anything OTHER than characters in the range  
  * **\*** ---  used to escape special (punctuation) characters  
  * **\*\*** --- escaped escape :)  
  
We often want to search for multiple characters of the same type, like, multiple "A" characters!  
  * **A** --- searching for one A :)
  * **\d+** --- searching for one or more digits  
  * **\w\*** --- searching for zero or more word characters  
  * **[AT]{10,20}** --- searching for a series of A or T characters of the length between 10 and 20  
  * **[A-Z]{3,}** --- searching for a series of at least three capital letters  
  
REGEX is greedy --- by default, the match is as long as possible. You can change it ---
  * **?** --- modifies greediness so that the match is as short as possible  
   
It can be helpful to nest your search term to the beginning or end of line:  
  * **^** --- beginning of line
  * **$** --- end of line

Capturing the search term and using it in replacements!
  * **()** --- captures the search term, making it available for use in replacements!
  * **\1**, **\2**...  --- when replacing, insert the first, second, (...) captured term








