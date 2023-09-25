from enum import Enum


class QuoteExtension(Enum):
    CSV = 'csv'
    PDF = 'pdf'
    DOCX = 'docx'
    TXT = 'txt'


class PhotoExtension(Enum):
    PNG = 'png'
    JPG = 'jpg'
    JPEG = 'jpeg'
