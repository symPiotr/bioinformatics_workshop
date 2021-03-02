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
       - Less intuitive than pointing and clicking (Graphical User Interface - GUI), takes dedicated effort to learn
       - But more versatile, less platform-specific
       - Makes it easy to save and replicate sequences of operations
       - Makes it easy to keep the log of operations and repeat them, perhaps on new files
       - Makes it easy to run operations on many files at once
       - Many useful tools only exists in command-line mode
       - It's much easier to write your own scripts with a command-line-only interface
       - Computing clusters usually use command line... you need to know it if you work with big dats!
   * Getting set up!
       - Software is platform-specific: Windows vs Mac vs Linux
       - Installing useful tools (Appendix 1 in the Book!): powerful text editor (Notepad++, BBEdit, or some of the alternatives!) and access to Unix/Linux command line
       - Setting up accounts on the cluster, connecting
 &nbsp;  
   
### 1.3. Unix/Linux - intro to the environment
   * Basic vocab:
       - Shell - command interpretor in your Unix/Linux operating system. Allows you to interact with the computer.
       - Kernel - the central part of a Unix operating system, the core interface between a computer's hardware and the processes
       - Bash - a Unix shell and command language, default login shell for most Linux distributions
       - Terminal - that's where shell runs!
       - Shell session is the current state/environment in the shell/terminal, delimited by login/logout.
       - Prompt - the active line where you type commands. Often includes useful info - user name, current directory
   * **pwd** --- where are you?
   * The Linux file system - more vocab:
       - root - the superuser account, but also, the very bottom of the file structure
       - Directories, files
       - Path
       - Current/working directory
       - Home directory (~)
   * **ls** --- listing directory contents
       - pointing at directories that you want listed!
       - arguments: -l, -h, -a ...
   * getting help about commands!
       - **man**
       - **--help**, **-h**
       - Google :)
   * **cd** --- changing directories
       - absolute vs relative path!
   ```
   cd Project1
   cd ..
   cd ./Project1/Dataset1
   cd /home/username/Project1/Dataset1
   cd ../Dataset2
   cd  / cd ~
   cd -
   ```
   * Effective navigation 
       - up and down arrows move you to previously applied commands that you can now edit
       - command **history** lists previously
       - Ctrl+A, Ctrl+E - jump to the beginning/end of the edited command
       - Tab - autocompletes the command being typed
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
       - **cp -r** --- copy recursively, the whole directory/file structure
       - what are other possible arguments?
   ```
   cp MyFile.txt ~/Project1/
   cp Project1/MyFile.txt MyFileRenamed.txt
   cp -r Project1 Project1_copy
   ```
   * **rm** --- removing files. Dangerous - there is no "Undo", no "Trash"!
   * Wildcards: "*" for any string of characters, "?" for a single character. Great for moving/coping multiple files
   ```
   cp ./* NewDirectory/
   mv Sample123_R?.fastq ~/Project1/ReadsForSample123/
   ```
   * Comments - text after #!
   ```
   ls     # This command lists the contents of the directory!
   rm *   # Be very careful! Are you sure this is what you want to do?
   ```  
   * **exit** - exiting your session!
&nbsp;  
  
### 1.4. The HOMEWORK :)
   * Read Chapter 1 and Chapter 4 in the book - recap what we have covered today!
   * Practice! Follow the exercises in the book, make sure you are comfortable with all material covered.
   * Make sure that you have accounts on one of the INoŚ clusters! I recommend *azor*.
   * Read Chapter 5 in the book. During the next session, we will mostly be covering its contents.
