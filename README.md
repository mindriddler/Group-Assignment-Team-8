# **Group Assignment, Group 8** #
## **Authors:** ##

#### Fredrik Magnusson [fredrik.magnusson2@yh.nackademin.se] ####
#### Timmy Elf ####
#### Martin Alfredson ####
#### Hugo Göransson ####
---
This is our version of the group assignment for the course "Programmering & Systemering" in the DevOps22 class at Nackademin.

# **Setup** 
To use the game you will need python 3.10 installed on your computer

For how to install python 3.10, see instructions at the bottom

## **Basic program functions:** ##
- The program will create a database inside the db folder
- The program will load a json file on demand and create a table called 'persons'
- You can delete a entry in the database
- The program can create a second table called 'vehicle' and you can add entrys to it
- The program can find correlations betwqeen the two tables and if there is any show it to you 

## **How to run** ##
- Navigate to the folder where you cloned the repository to in the terminal
- Start the program
```
python Run_File.py 
```
-----



## **Windows** ##
You can either download python by clicking **_[here](https://www.python.org/downloads/)_**

you can use also use winget by typing the line below into powershell
```powershell
winget install python --accept-package-agreements
```
<sup>read more about winget [here](https://learn.microsoft.com/en-us/windows/package-manager/winget/)</sup>

## **Linux** ##
First check if python3.10 is already installed
```
python3 -v
```
if you get no return from that input, follow below
```
sudo apt update
sudo apt-get install python3
```
