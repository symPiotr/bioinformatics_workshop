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
   * Why use command line?
 
   * Connecting to your terminal

### 1.3. Linux - intro to the environment
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
   * **cp** --- copy file to a new location
       - **cp -r** --- copy recursively, the whole file structure
   * Wildcards: "*"* for any string of characters, "?" a single character
   * **rm** --- removing files. Dangerous!
   * 
