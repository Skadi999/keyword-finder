from enum import Enum


class ComboboxEnum(Enum):
    """Enums created for the scan mode combo box."""
    KEYWORD_IN_FILES = 'Find Keyword in Files'
    OCCURRENCE_IN_FILES = 'Find Every Occurrence of Keyword in Files'
    OCCURRENCE_IN_ALL_FILES = 'Find Every Occurrence of Keyword in All Files'
    ALL_KEYWORDS_IN_ALL_FILES = 'Find All Keywords From File in All Files'
    KEYWORD_IN_ALL_FILES = 'Find Keyword in All Files'
