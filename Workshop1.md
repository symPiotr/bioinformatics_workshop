# Workshop 1. (2nd March 2021). Introduction to computational biology, command line, Linux.

### 1.1. The workshop
   * Piotr - background, interests, and bioinformatics experience
   * Workshop participants - background, interests, experience, expectations
   * What the workshop is about
       - Unofficial, informal - but a bit of a pilot for a future more systematic Comp Biol training at INoŚ
       - Goal: teach you something useful. I assume you want to learn.
       - Contents and pace flexible, I'll adjust to your needs and interests. 
       - You don't need to attend individual classes. Drop any time. No grades or evaluations.
       - When teaching new stuff I assume you are comfortable with the previously taught stuff. Make sure you are!
 &nbsp;  
   
 ### 1.2. Bioinformatics and command line
   * Bioinformatics vs. computational biology
       - Either way, we want to learn tools that are applicable to many data types, allow to simplify time-intensive tasks, and enable tackling projects on an otherwise-implausible scale
       - Mastering a set of relatively simple tools that we will be able to combine, mix-and-match --- to achieve exactly what you want with the data.
       - Learning it takes effort - but once you have it, you will have a set of scaleable, highly replicable tools that you will be able to reuse and modify for an ever-increasing set of tasks.
       - Understanding your data and knowing what you want is going to be the key, but once we have that, we should be able to do whatever :)
   * Why use command line?
       - Less intuitive than pointing and clicking (GUI), takes dedicated effort to learn
       - But applicable to , replicable, 
   * Getting set up!
       - This is platform-specific: Windows vs Mac vs Linux
       - Installing useful tools (Appendix 1 in the Book!): powerful text editor (Notepad++, BBEdit, or some of the alternatives!) and access to Unix/Linux command line
       - Setting up accounts on the cluster, connecting

### 1.3. Unix/Linux - intro to the environment
   * **pwd** --- where are you?
   * The Linux file system: root, directories, files. Home directory (~)
   * **ls** --- listing directory contents
       - pointing at directories that you want listed!
       - arguments: -l, -h, -a ...
   * getting help about commands!
       - **man**
       - **--help**, **-h**
       - Google :)
   * **cd** --- changing directories
   ```
   cd Project1
   cd ..
   cd ./Project1/Dataset1
   cd /home/username/Project1/Dataset1
   cd ../Dataset2
   cd  / cd ~
   ```
   * **mkdir** --- making directories
   * **rmdir** --- removing EMPTY directories
   * **touch** --- as a way of making empty files
   * **mv** --- change name or move
       - path as an extension of a filename!
       - keep attention to syntax!
       - relative vs. absolute path
   ```
   mv OldName.txt NewName.txt
   mv OldName.txt ../NewLocationAndName.txt
   mv OldPath/OldName.txt ~/NewName.txt
   ```
   * **cp** --- copy file to a new location. Perhaps under a new name!
   ```
   cp MyFile.txt ~/Project1/
   cp Project1/MyFile.txt FileRenamed.txt
   ```
       - **cp -r** --- copy recursively, the whole directory/file structure
       - what are the other options?
   * Wildcards: "*"* for any string of characters, "?" a single character
   ```
   cp ./* NewDirectory/
   cp Sample123_R?.fastq ~/Project1/ReadsForSample123/
   
   ```
   * **rm** --- removing files. Dangerous - there is no "Undo", no "Trash"!
   * 
