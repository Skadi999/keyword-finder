import os.path

from PySide6 import QtWidgets
from PySide6.QtWidgets import QFileDialog

from enums import ComboboxEnum
from keyword_finder import KeywordFinder


def get_all_base_names(files):
    """Returns the base names of all files in the \"files\" argument, separated by a whitespace.
    Base names are file names with their extension, but without the full path."""
    files_str = ''
    for filename in files:
        files_str += os.path.basename(filename) + ' '
    return files_str[:-1]


class KeywordFinderWidget(QtWidgets.QWidget):
    """The main window of the Keyword Finder application.
    excluded_files = A variable that stores all filenames that will not be scanned.
    preferred_files = Stores filenames that will be scanned before others (used for performance reasons)
    files_to_scan = Stores selected filenames that will be scanned, if we are not scanning every single file in the
    directory
    Other attributes represent the various widgets in the window."""
    def __init__(self):
        super().__init__()
        self.excluded_files = []
        self.preferred_files = []
        self.files_to_scan = []
        # Define Layouts
        main_layout = QtWidgets.QVBoxLayout()
        mode_layout = QtWidgets.QHBoxLayout()
        directory_browse_layout = QtWidgets.QHBoxLayout()
        file_scan_layout = QtWidgets.QHBoxLayout()
        keyword_file_layout = QtWidgets.QHBoxLayout()
        other_layout = QtWidgets.QHBoxLayout()
        excluded_layout = QtWidgets.QHBoxLayout()
        preferred_layout = QtWidgets.QHBoxLayout()

        # Create Widgets
        label_mode = QtWidgets.QLabel('Mode: ')
        self.combo_mode = QtWidgets.QComboBox()
        self.combo_mode.addItem(ComboboxEnum.KEYWORD_IN_FILES.value)
        self.combo_mode.addItem(ComboboxEnum.OCCURRENCE_IN_FILES.value)
        self.combo_mode.addItem(ComboboxEnum.OCCURRENCE_IN_ALL_FILES.value)
        self.combo_mode.addItem(ComboboxEnum.ALL_KEYWORDS_IN_ALL_FILES.value)
        self.combo_mode.addItem(ComboboxEnum.KEYWORD_IN_ALL_FILES.value)
        self.combo_mode.currentIndexChanged.connect(self.reset_and_disable_widgets_based_on_mode)

        label_path = QtWidgets.QLabel('Directory: ')
        self.textfield_path = QtWidgets.QLineEdit()
        button_path = QtWidgets.QPushButton('Browse')
        button_path.clicked.connect(self.set_path_directory)

        label_scanned_files = QtWidgets.QLabel('Scanned Files: ')
        self.textfield_scanned_files = QtWidgets.QLineEdit()
        self.button_scanned_files = QtWidgets.QPushButton('Browse')
        self.button_scanned_files.clicked.connect(self.set_filenames_to_scan)

        label_keyword_file = QtWidgets.QLabel('File With Keywords: ')
        self.textfield_keyword_file = QtWidgets.QLineEdit()
        self.button_keyword_file = QtWidgets.QPushButton('Browse')
        self.button_keyword_file.clicked.connect(self.set_keyword_file)

        label_keyword = QtWidgets.QLabel('Keyword: ')
        self.textfield_keyword = QtWidgets.QLineEdit()
        self.button_scan = QtWidgets.QPushButton('Scan')
        self.button_scan.clicked.connect(self.scan)

        label_excluded_files = QtWidgets.QLabel('Excluded Files: ')
        self.textfield_excluded_files = QtWidgets.QLineEdit()
        self.button_excluded_files = QtWidgets.QPushButton('Browse')
        self.button_excluded_files.clicked.connect(self.set_excluded_files)

        label_preferred_files = QtWidgets.QLabel('Preferred Files: ')
        self.textfield_preferred_files = QtWidgets.QLineEdit()
        self.button_preferred_files = QtWidgets.QPushButton('Browse')
        self.button_preferred_files.clicked.connect(self.set_preferred_files)

        # Add Widgets to Layouts
        mode_layout.addWidget(label_mode)
        mode_layout.addWidget(self.combo_mode)

        directory_browse_layout.addWidget(label_path)
        directory_browse_layout.addWidget(self.textfield_path)
        directory_browse_layout.addWidget(button_path)

        file_scan_layout.addWidget(label_scanned_files)
        file_scan_layout.addWidget(self.textfield_scanned_files)
        file_scan_layout.addWidget(self.button_scanned_files)

        keyword_file_layout.addWidget(label_keyword_file)
        keyword_file_layout.addWidget(self.textfield_keyword_file)
        keyword_file_layout.addWidget(self.button_keyword_file)

        other_layout.addWidget(label_keyword)
        other_layout.addWidget(self.textfield_keyword)

        excluded_layout.addWidget(label_excluded_files)
        excluded_layout.addWidget(self.textfield_excluded_files)
        excluded_layout.addWidget(self.button_excluded_files)

        preferred_layout.addWidget(label_preferred_files)
        preferred_layout.addWidget(self.textfield_preferred_files)
        preferred_layout.addWidget(self.button_preferred_files)

        # Add Layouts to Main Layout
        main_layout.addLayout(mode_layout)
        main_layout.addLayout(directory_browse_layout)
        main_layout.addLayout(file_scan_layout)
        main_layout.addLayout(keyword_file_layout)
        main_layout.addLayout(other_layout)
        main_layout.addLayout(excluded_layout)
        main_layout.addLayout(preferred_layout)
        main_layout.addWidget(self.button_scan)

        self.setWindowTitle('Keyword Finder')
        self.setLayout(main_layout)
        self.reset_and_disable_widgets_based_on_mode()

    def reset_and_disable_widgets_based_on_mode(self):
        """Responsible for clearing all text fields and disabling certain widgets based on the selected scan mode."""
        self.clear_all_fields()
        self.reset_disabled()
        self.disable_widgets_based_on_mode()

    def clear_all_fields(self):
        """Clears every single text field"""
        self.textfield_scanned_files.clear()
        self.textfield_keyword_file.clear()
        self.textfield_keyword.clear()
        self.textfield_excluded_files.clear()
        self.textfield_preferred_files.clear()

    def reset_disabled(self):
        """Resets the widgets in the app to an initial state"""
        self.textfield_scanned_files.setEnabled(False)
        self.button_scanned_files.setEnabled(True)
        self.textfield_keyword_file.setEnabled(True)
        self.button_keyword_file.setEnabled(True)
        self.textfield_keyword.setEnabled(True)
        self.textfield_excluded_files.setEnabled(False)
        self.button_excluded_files.setEnabled(True)
        self.textfield_preferred_files.setEnabled(False)
        self.button_preferred_files.setEnabled(True)

    def disable_widgets_based_on_mode(self):
        """Disables certain widgets based on the selected scan mode."""
        if self.combo_mode.currentText() == ComboboxEnum.KEYWORD_IN_FILES.value or self.combo_mode.currentText() == \
                ComboboxEnum.OCCURRENCE_IN_FILES.value:
            self.textfield_keyword_file.setEnabled(False)
            self.button_keyword_file.setEnabled(False)
            self.button_excluded_files.setEnabled(False)
            self.button_preferred_files.setEnabled(False)
        elif self.combo_mode.currentText() == ComboboxEnum.OCCURRENCE_IN_ALL_FILES.value:
            self.button_scanned_files.setEnabled(False)
            self.textfield_keyword_file.setEnabled(False)
            self.button_keyword_file.setEnabled(False)
            self.button_preferred_files.setEnabled(False)
        elif self.combo_mode.currentText() == ComboboxEnum.ALL_KEYWORDS_IN_ALL_FILES.value:
            self.button_scanned_files.setEnabled(False)
            self.textfield_keyword.setEnabled(False)
        elif self.combo_mode.currentText() == ComboboxEnum.KEYWORD_IN_ALL_FILES.value:
            self.textfield_keyword_file.setEnabled(False)
            self.button_keyword_file.setEnabled(False)
            self.button_scanned_files.setEnabled(False)
            self.button_preferred_files.setEnabled(False)

    def set_filenames_to_scan(self):
        # todo Path does not have to be a valid path. Fix this in the future.
        if self.textfield_path.text():
            filenames = QFileDialog.getOpenFileNames(self, "Open File", self.textfield_path.text(),
                                                     "Text Files (*.txt)")
        else:
            filenames = QFileDialog.getOpenFileNames(self, "Open File", "C:\\", "Text Files (*.txt)")

        self.files_to_scan = filenames[0]

        files_str = get_all_base_names(self.files_to_scan)
        self.textfield_scanned_files.setText(files_str)

    def set_keyword_file(self):
        if self.textfield_path.text():
            filename = QFileDialog.getOpenFileName(self, "Open File", self.textfield_path.text(), "Text Files (*.txt)")
        else:
            filename = QFileDialog.getOpenFileName(self, "Open File", "C:\\", "Text Files (*.txt)")

        self.textfield_keyword_file.setText(filename[0])

    def set_path_directory(self):
        directory = QFileDialog.getExistingDirectory()
        self.textfield_path.setText(directory + '/')

    def set_excluded_files(self):
        if self.textfield_path.text():
            excluded_files = QFileDialog.getOpenFileNames(self, "Open Files", self.textfield_path.text(),
                                                          "Text Files (*.txt)")
        else:
            excluded_files = QFileDialog.getOpenFileNames(self, "Open Files", "C:\\", "Text Files (*.txt)")

        self.excluded_files = excluded_files[0]

        files_str = get_all_base_names(self.excluded_files)
        self.textfield_excluded_files.setText(files_str)

    def set_preferred_files(self):
        if self.textfield_path.text():
            preferred_files = QFileDialog.getOpenFileNames(self, "Open Files", self.textfield_path.text(),
                                                           "Text Files (*.txt)")
        else:
            preferred_files = QFileDialog.getOpenFileNames(self, "Open Files", "C:\\", "Text Files (*.txt)")

        self.preferred_files = preferred_files[0]

        files_str = get_all_base_names(self.preferred_files)
        self.textfield_preferred_files.setText(files_str)

    def scan(self):
        """Performs a scan for keywords using the KeywordFinder class based on the scan mode."""
        keyword = self.textfield_keyword.text()

        # Creates the output file if it hadn't been created yet and resets its contents.
        with open('output.txt', 'w') as output_file:
            keyword_finder = KeywordFinder(self.textfield_path.text(), output_file)

            if self.combo_mode.currentText() == ComboboxEnum.KEYWORD_IN_FILES.value:
                keyword_finder.find_keyword_in_given_files(keyword, self.files_to_scan)
            elif self.combo_mode.currentText() == ComboboxEnum.OCCURRENCE_IN_FILES.value:
                keyword_finder.find_every_occurrence_of_keyword_in_given_files(self.files_to_scan, keyword)
            elif self.combo_mode.currentText() == ComboboxEnum.OCCURRENCE_IN_ALL_FILES.value:
                keyword_finder.find_every_occurrence_of_keyword_in_all_files(keyword, self.excluded_files)
            elif self.combo_mode.currentText() == ComboboxEnum.ALL_KEYWORDS_IN_ALL_FILES.value:
                keyword_finder.find_all_keywords_from_file_in_all_files(self.textfield_keyword_file.text(),
                                                                        self.excluded_files, self.preferred_files)
            elif self.combo_mode.currentText() == ComboboxEnum.KEYWORD_IN_ALL_FILES.value:
                keyword_finder.find_keyword_in_all_files(keyword, self.excluded_files)
