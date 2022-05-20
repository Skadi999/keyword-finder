# keyword-finder
Small GUI program for finding specified keywords in a set of specified files.

This desktop app was made with Python and the PySide Qt framework.
It is used to scan text files for specified keywords.
It works exclusively with tab-separated .txt files.

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
