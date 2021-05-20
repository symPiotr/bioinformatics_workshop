# Workshop P2 (20th May 2021). The first Python scripts.
  
### P2.1. Recap of the key concepts
Last week, we have learnt the key building blocks of a Python script:  
* **Variables:**  
  * Integer  
  * Float  
  * String   
  * Boolean  
* **Arrays:**  
  * List  
  * Dictionary  
* **Flow control tools:**
  * *for* loop  
  * *while* loop  
  * *if* statement  
  
&nbsp;  
These few building blocks can be combined into seriously sophisticated workflows!  
Let's see how that works!
&nbsp;  
  
### P2.2. Key components of a script
A Python script needs some essential elements:  
&nbsp;  
1) A way of informing the operating system that the Python3 should be used to interpret the script  
  * We can run the script by specifying `python set_of_instructions.txt` ...   
  * But probably a more universal way is making sure that the script starts with a line informing the operating system that the remainder of the file contents should be directed to and interpreted by Python:  
  `#! /usr/bin/env python`, and making the script executable: `chmod u+x script.py`.  
&nbsp;  
2) A way of accepting input:  
  * Asking the user for input data, for example: `name = input("Enter your name: ")`.  
  * Opening files indicated within the script, or provided as arguments at the time the script is run.
&nbsp;  
3) A way of providing output:  
  * Printing information to standard output (screen): `print("Hello " + name + "!")`.  
  * Creating output files.  

By combining these elements together, we can write our first script --- `Hello.py`
```
#! /usr/bin/env python3
name = input("Enter your name: ")
print("Hello " + name + "!")
```  
&nbsp;  
  
### P2.3. Scripts that are actually useful --- how to structure your workflow?
We are going to work on two scripts today.  
&nbsp;  
The first script will print a reverse-complement of a user-provided sequence.
Let's talk about the necessary steps!  
  
The second step will compute basic sequence statistics: length, count of Ns, and GC% in a user-provided sequence.  
  
