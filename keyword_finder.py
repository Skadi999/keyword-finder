import csv
import glob
import os.path


def get_first_cell_of_all_rows(filename):
    """Returns the first cell of every row from a given file as a list, excluding the row 0 cell (column name)"""
    keywords = []

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')

        for row in csv_reader:
            keywords.append(row[0])

    return keywords[1:]


class KeywordFinder:
    """Finds a keyword or keywords in the specified files.\n
    The files are always tab-separated .txt files.\n
    A keyword may either be input manually (only one keyword allowed) or read from a file. If read from a file, it will
    take the first column of every single row, except for the header row, and use that as the keyword.\n
    Files may be specified manually, or you may choose to scan every single file in the path attribute directory.\n
    You may also specify excluded files (files that will not be scanned), or preferred files, which are files that will
    be scanned before the other files, making the program finish faster.\n
    You may also specify whether you wish to know if a keyword exists in the files or whether you need to find every
    single occurrence of said keyword.\n
    Results are output to the console and written to the specified file.\n
    path = The directory that contains the scanned files.\n
    output_file = The file that will contain the results of the scan.
    """
    def __init__(self, path, output_file):
        self.path = path
        self.f = output_file

    def find_all_keywords_from_file_in_all_files(self, keyword_filename, excluded_files=None, preferred_files=()):
        """Gets all keywords in a given file, then searches for all those keywords in all files.\n
        filename = Name of the txt file whose contents (keywords) we try to find, given WITH its full path,
        but with the extension. Example: 'armor.txt'\n
        excluded_files = These files will not be searched for the keywords.\n
        preferred_files = Used for performance, allows you to set some files to be searched before other files."""
        # The first cell of each row in the file will be used as a keyword
        all_keywords = get_first_cell_of_all_rows(keyword_filename)

        # https://docs.python-guide.org/writing/gotchas/
        if excluded_files is None:
            excluded_files = []

        # We don't want to search the file where we got the keywords from.
        excluded_files.append(keyword_filename)

        self.find_given_keywords_in_all_files(all_keywords, excluded_files, preferred_files)

    def find_given_keywords_in_all_files(self, keywords, excluded_files, preferred_files=()):
        """Searches for all given keywords in all files.
        Do not call outside KeywordFinder class."""
        new_keywords = []
        # First we go through the preferred files
        for keyword in keywords:
            if not self.find_keyword_in_given_files(keyword, preferred_files):
                new_keywords.append(keyword)

        # We then exclude each of the preferred files, as we've already went through them
        for pref_file in preferred_files:
            excluded_files.append(pref_file)

        # After we went through preferred files, we go through the remaining files
        for keyword in new_keywords:
            if not self.find_keyword_in_all_files(keyword, excluded_files):
                print(f'***Did not find {keyword}***')
                self.f.write(f'***Did not find {keyword}***\n')

    def find_keyword_in_all_files(self, keyword, excluded_files):
        """Finds the given keyword in every txt file in the specified path"""

        # Gets all the txt files that are located in our path
        all_files = glob.glob(f'{self.path}*.txt')

        for file in all_files:
            is_continue = False
            for excluded_file in excluded_files:
                if os.path.abspath(file) == os.path.abspath(excluded_file):
                    is_continue = True
            if is_continue:
                continue
            if self.find_keyword_in_file(file, keyword):
                return True
        return False

    def find_keyword_in_given_files(self, keyword, files):
        """Finds the given keyword in the given txt files"""
        for file in files:
            if self.find_keyword_in_file(file, keyword):
                return True
        return False

    def find_keyword_in_file(self, filename, keyword):
        """Finds a given keyword in file."""
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='\t')
            # If the keyword appears in the row, prints it.
            for row in csv_reader:
                if keyword in row:
                    print(f'Found keyword: {keyword} in {filename}')
                    self.f.write(f'Found keyword: {keyword} in {filename}\n')
                    return True
            return False

    def find_every_occurrence_of_keyword_in_all_files(self, keyword, excluded_files):
        """Finds every occurrence of the given keyword in every txt file in the specified path"""

        # Gets all the txt files that are located in our path
        all_files = glob.glob(f'{self.path}*.txt')

        count = 0
        for file in all_files:
            is_continue = False
            for excluded_file in excluded_files:
                if os.path.abspath(file) == os.path.abspath(excluded_file):
                    is_continue = True
            if is_continue:
                continue
            count += self.find_every_occurrence_of_keyword_in_file(file, keyword)
        print(f'Total occurrences found: {count}')
        self.f.write(f'Total occurrences found: {count}\n')

    def find_every_occurrence_of_keyword_in_given_files(self, files, keyword):
        """Finds every occurrence of the given keyword in the given files"""
        count = 0
        for file in files:
            count += self.find_every_occurrence_of_keyword_in_file(file, keyword)
        print(f'Total occurrences of {keyword} in given files: {count}')
        self.f.write(f'Total occurrences of {keyword} in given files: {count}\n')
        return count

    def find_every_occurrence_of_keyword_in_file(self, filename, keyword):
        """Finds every occurrence of the given keyword in the given file"""
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='\t')
            # If the keyword appears in the row, prints it.
            count = 0
            for row_idx, row in enumerate(csv_reader):
                if keyword in row:
                    count += 1
                    print(f'Found keyword: {keyword} in {filename}: \'{row[0]}\', line {row_idx}')
                    self.f.write(f'Found keyword: {keyword} in {filename}: \'{row[0]}\', line {row_idx}\n')
            print(f'Total occurrences of {keyword} in {filename}: {count}')
            self.f.write(f'Total occurrences of {keyword} in {filename}: {count}\n')
            return count
