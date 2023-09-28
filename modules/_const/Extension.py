from enum import Enum


class QuoteExtension(Enum):
    """Enum class for centralizing quote file extensions."""

    CSV = 'csv'
    PDF = 'pdf'
    DOCX = 'docx'
    TXT = 'txt'


class PhotoExtension(Enum):
    """Enum class for centralizing image file extensions."""

    PNG = 'png'
    JPG = 'jpg'
    JPEG = 'jpeg'
