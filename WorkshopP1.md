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
* **Program**: A collection of instructions that can be executed by a computer to perform a specific task.   
* **Script**: A sequence of instructions that is interpreted or carried out by another program (interpreter).  
* **Code**: *Noun*: A program or a line of a program, sometimes called source code; *Verb*: The act of writing a program.   
* **Execute/Run**: To begin and carry out the operation of a program, or a portion of a program. 
* **Variable**: A component of a program, used to store information to be referenced and manipulated. Name matters!   
* **Array**: A data structure that contains a group of elements, used to organize data to facilitate sorting or searching.  
* **Arguments**: Values that are sent to a program at the time it is run.  
* **Statement** A line of a program or script which can assign a value, do a comparison, or perform another operation.  
* **Function**: A subprogram that can be called repeatedly to perform the same task within a program.   
* **Parameters**: Values that are sent to a function when it is called.  
* **Return**: The act of sending back a value by a function.  
* **Parse**: To extract particular data elements from a larger block of text.  
&nbsp;  
  
### P1.3. Variables

Each variable has several attributes. First attribute - **the name**, usually a p]ain word that gives some indication of the variable content. This needs to be informative!
&nbsp;  
  
Second variable attiribute - "the type":  
```
**Integer**                        0, 1, 2, 123456, -4321  
**Floating point (Float)**         0.12, 1.000, -123.56  
**Boolean**                        True, False == 1, 0  
**String**                        "Piotr", ">Seq123_456", "ACGTGTT", "123"  
```
&nbsp;   
  
Third variable attiribute - "the value".  
&nbsp;   
    
In some programming languages, you need to define the type when setting the variable. But Python 3 recognizes data type automatically, based on the value.
``
Var1 = 0
Var2 = 1.234
Var3 = "ABC"
Var4 = True
``
&nbsp;  
  
You can check the variable type using the *type()* function:
```
type(Var1)
<class 'int'>
type(Var2)
<class 'str'>
```
&nbsp;  
  
You can also enforce the variable type:
```
Var4 = float(1)
Var5 = int(Var4)
Var6 = str(Var4)
```
&nbsp;  

Variables, or directly input objects can be used for various types of operations - as listed in a table 7.3 in Practical Computing for Biologists book:  
<img width="458" alt="Screenshot 2021-05-13 at 07 45 53" src="https://user-images.githubusercontent.com/12505600/118083569-73ed7780-b3bf-11eb-9d86-61f7bb4550f0.png">
&nbsp;  
  
### P1.4. Arrays
  
***Two primary types:***  
1. **List** ---- of variables, or arrays!
    List of Lists!
  
2. **Dictionary**  {Key: Value}   for example, {'Seq1': 'ACGT', 'Seq2': "ACCATG'}
    Dictionary of lists!
&nbsp;  
  
Calling arrays in Python3:
```
List1 = []   # empty dictionary
NuclList = ['C', 'G', 'T', 'A']         # a list of nucleotides

NuclList                                # displays the list

type(List1) 
dir(List1)       # dir() function returns all properties and methods of the specified object
```

Objects in a list are numbered - each has an index position

```
NuclList[0]  # returns object with index no. 0 as a variable... remember they are indexed 0, 1, 2 ...
NuclList[1:]  # returns objects from the indicated position onwards, as a list!
&nbsp;  
  
List_of_seqs = [['Seq1', 'ACGTT'], ['Seq2', 'CCTTT']] # List of lists!
List_of_seqs[0][1]  # from list with index no. 0, return item with index no. 1
NuclList.append("N")  
```  
&nbsp;  

Note that string can be interpreted as a list of characters!  
  
&nbsp;  
  
```
Dict1 = {}  
Dict2 = {'G': 'Guanine', 'C': 'Cytosine'}  
  
type(Dict2)
dir(Dict2)
  
Dict2['G']               # Extracting value correspondiong to key "G".
Dict2['A'] = 'Adenine'   # Adding a new key: value combination
```
&nbsp;  
  
### P1.5. Flow control

##### Decisions with the *if* statement
***if*** *statement* is the most widely used building block for decision making in the script - a sign at a fork in the road. ***if - elif - else*** construction will likely form an important part of your scripts!  
  
```
if Value == 2:
    print("Couple")
elif Value in range(3,6):
    print("Few")
elif Value in range(6,10):
    print("Several")
else:
    print("Many")
```

##### Looping with *for* and *while*
The *for* loop iterates through a pre-defined list of objects:   
```
for item in NucleotideList:
    print(item)

Sum = 0
for no in range(0,10):
    Sum += no
    print(no, Sum)
```  
&nbsp;  
  
The *while* loop keeps iterating as long as the pre-defined condition is fulfilled:  
```
Sum = 0
no = 0
while Sum < 100:
    Sum += no
    no += 1
    print(no, Sum)
```
