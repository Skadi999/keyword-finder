# keyword-finder
A GUI program for finding specified keywords in a set of specified files.

This desktop app was made with Python and the PySide Qt framework.
It is used to scan text files for specified keywords.
It works exclusively with tab-separated .txt files.

The need for this app arose while I was making a modification for the game Diablo II. Modifying items, attributes, monsters, and other data in the game involves
editing tab-separated .txt files. One such file, itemstatcost.txt, stores all the attributes/stats in the game. I needed to add some attributes, but the problem is that
itemstatcost.txt is, unfortunately, limited to 512 rows and it had reached its limit. There is no feasible way to remove this limitation, so the only thing I could've done
was to remove some rows. I knew for a fact there were some unused rows in the file, but I didn't know which ones, and checking manually is a painful task, because I would have
to check the 91 other files for each of the 512 rows to see which ones are unused. That's when the idea to make this app came to be. The fourth mode of this app (see below)
does exactly what I needed to, it takes each row from a file (more specifically, the first column of each row - the name column) and checks all the other files in the same
directory to see whether the scanned entry is used in any of the other files.

It has five modes of operation:
1. Find Keyword in Files: The simplest mode, you specify a keyword (only one is allowed) and files to scan. 
It then scans the files and tells you whether the keyword was found or not.
2. Find Every Occurrence of Keyword in Files: Same as the first one, but outputs every occurrence of the keyword in the specified files, telling the exact file name, 
    line number, and the first column of the row where the keyword was found.
3. Find Every Occurrence of Keyword in All Files: In this mode, you do not specify files to scan. Instead, it will scan every .txt file in the specified directory.
    Like mode #2, it will find every occurrence of the keyword in the files. You may also specify excluded files - those files will not be scanned.
4. Find All Keywords From File in All Files: Instead of specifying a keyword, you specify a .txt file (File with Keywords).
    The FIRST COLUMN of EACH ROW (except the header row) in the file will be used as a keyword. After that, the program will scan each keyword in every file in the directory.
    It will not scan for every occurrence of the keyword (similar scan to #1)
    You may specify excluded files and preferred files. Preferred files are files that will be scanned first, before the other files. If you know some files that contain
    many keywords, you should specify them as preferred files. This will make the scan finish much faster!
5.  Find Keyword in All Files. Like #1, but scans all files in the directory.


In modes where it's possible to specify excluded and preferred files, they are always optional.

Results are printed to an output file (by default, output.txt) and also written to the console.

## How to run

It is nice to use python virtual environment not to pollute global one.

## Python version

Python version used to built the program: **Python 3.10.4**

### Generate virtual environment

1. Go to the project directory `keyword-finder`
2. Make sure you are in the root
3. Run `python -m venv env`.

### Use the python virtual environment

Windows: `env\Scripts\activate.bat`

Unix or MacOS: `source env/bin/activate`

### Install required packages

Inside virtual environment run: `pip install -r requirements.txt`

### Run the program

Inside virtual environment: `python main.py`
