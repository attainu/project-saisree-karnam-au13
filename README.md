# Junk File Organizer

## Overview
The aim of this project is to build a python program that runs as a command-line tool. Basically, as a lazy programmer,  Due to a large number of files, it is a daunting task to sit and organize each file. To make that task easy, we need a Python script that comes in handy and returns a folder where all the files are organized in a well-manner within seconds. 

## Concepts Used

```
. File handling in python
. OS module provides functions for interacting with operating system
. Recursion
. shutil(or shell utilites) module has functions to let you copy, move,
  rename files in python 
. date time module is to work with dates as date objects

```
## Steps Involved
-> Import all the library functions required like os,shutil and datetime.

-> Create different folders based on type of files users can divided into different 
  folders using dictionaries

-> Each folder will represent the name of the files present inside it

>Organize by extension :  

- Create a function to filter file types into their respective folders
- Use os module of python to recursively list out all the files that are present 
  in the folder into the newly created folder.
- users can organize files by file extension in a given folder, folder will be 
   created according to file extension and finally all files will be moved to a 
   created folder.
 >Organize by Size : 

- create a function to get the folder path from users and create a dictionary with 
  file size and sort the dictionary 
- users can organize files by size of file in a given folder
- Sort the dictionary by size and prints file names and size  
 >Organize by Date : 

- Create a function to sort files by date  into their respective folders
- Use os module of python to recursively list out all the files that are present in 
  the folder into the newly created folder.
- Users can organize files by date of file created in a given folder, folder will be created according to dates of files present and all files are moved to created folder 
