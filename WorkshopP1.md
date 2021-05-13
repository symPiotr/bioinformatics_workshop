# Workshop P1 (13th May 2021). Intro to programming and Python. 
  
### P1.1. Programming - basic concepts
* Programming as a way of combining simple building blocks to achieve exactly what you need!
* Diversity of programming languages, optimized for different tasks
* Compiled vs interpreted programming languages
* Python as a popular, powerful programming language with straightforward syntax and that we will use :)
* Key challenge in programming is developing the way of thinking about the task, rather than about syntax!  
&nbsp;  
  
* I am not a formally trained bioinformatician. I do not know many sophisticated tools.
* I learnt how to combine very simple tools into larger workflows effectively - and that has changed my research!  
&nbsp;  
  
### P1.2. Vocabulary (largely following Chapter 7!)
**Program**: A collection of instructions that can be executed by a computer to perform a specific task.   
**Script**: A sequence of instructions that is interpreted or carried out by another program (interpreter).  
**Code**: *Noun*: A program or a line of a program, sometimes called source code; *Verb*: The act of writing a program.   
**Execute/Run**: To begin and carry out the operation of a program, or a portion of a program. 
**Variable**: A component of a program, used to store information to be referenced and manipulated. Name matters!   
**Array**: A data structure that contains a group of elements, used to organize data to facilitate sorting or searching.
**Arguments**: Values that are sent to a program at the time it is run.  
**Statement** A line of a program or script which can assign a value, do a comparison, or perform another operation.  
**Function**: A subprogram that can be called repeatedly to perform the same task within a program.   
**Parameters**: Values that are sent to a function when it is called.  
**Return**: The act of sending back a value by a function.  
**Parse**: To extract particular data elements from a larger block of text.  

### P1.3. Variables

Variable types:
**Integer**                        0, 1, 2, 123456, -4321  
**Floating point (Float)**         0.12, 1.000, -123.56  
**Boolean**                        True, False == 1, 0  
**String**                        "Piotr", ">Seq123_456", "ACGTGTT", "123"  
&nbsp;   
In some languages you need to define it when setting. But Python 3 recognizes data type automatically!

 

Var1 = 0
Var2 = "ABC"
Var3 = True

 

You can enforce the variable type:

 

Var4 = float(1)
Var5 = int(Var3)
Var6 = str(Var3)

 

You can check variable type using the type() function:

 

type(Var1)
<class 'int'>
type(Var2)
<class 'str'>



####### Arrays:

 

Types:
List ---- of variables, or arrays!
    List of Lists!

 

Dictionary  {Key: Value}   for example, {'Seq1': 'ACGT', 'Seq2': "ACCATG'}
    Dictionary of lists!

 


Calling arrays in Python3:
List1 = []   # empty dictionary
List2 = ['A', 'B', 1, 2]   # simple list

 

type(List1)
dir(List1)

 

List2[0]  # returns object with index no. 0 as a variable... remember they are indexed 0, 1, 2 ...
List[1:]  # returns objects from the indicated position onwards, as a list!

 

List_of_seqs = [['Seq1', 'ACGTT'], ['Seq2', 'CCTTT']]  # List of lists!
List_of_seqs[0][1] # from list with index no. 0, return item with index no. 1

 

List2.append("C")

 

dir(List1)

 


Dict1 = {}
Dict2 = {1: 'A', 2: 'B'}

 

Dict2[1]
Dict2[3] = 'C'


