import os
from datetime import datetime
import subprocess
import pandas as pd
from docx import Document
from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import Quote


class IngestorInterface(ABC):
    """Interface class for other ingestors."""

    allowed_extensions = []

    @classmethod
    @abstractmethod
    def can_ingest(cls, path: str) -> bool:
        """Class abstract method to check if file ingestable."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[Quote]:
        """Class abstract method to parse the given file."""
        pass


class CSVIngestor(IngestorInterface):
    """An ingestor that realize IngestorInterface to handle CSV file type."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        """Overwritten classmethod to parse CSV file."""
        if not cls.can_ingest(path):
            raise Exception('Invalid file type!')

        quotes = []
        df = pd.read_csv(path)
        body = df['body']
        author = df['author']
        for i in range(2):
            new_quote = Quote(body[i].strip('"'), author[i])
            quotes.append(new_quote)

        return quotes


class PdfIngestor(IngestorInterface):
    """An ingestor that realize IngestorInterface to handle PDF file type."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        """Overwritten classmethod to parse PDF file."""
        if not cls.can_ingest(path):
            raise Exception('Invalid file type!')

        tmp = f"./tmp/{round(datetime.now().timestamp())}.txt"
        subprocess.run(['pdftotext', path, tmp])
        quotes = []
        with open(tmp, 'r') as f:
            for index, line in enumerate(f.readlines()):
                if index != 0:
                    # because all quotes result one first line in text file
                    break
                quotes = line.strip('\x0c\n').split(' "')
                for quote in quotes:
                    quote = quote.split(' - ')
                    new_quote = Quote(line[0].strip('"'), line[1])
                    quotes.append(new_quote)
        os.remove(tmp)

        return quotes


class DocxIngestor(IngestorInterface):
    """An ingestor that realize IngestorInterface to handle Docx file type."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        """Overwritten classmethod to parse TXT file."""
        if not cls.can_ingest(path):
            raise Exception('Invalid file type!')

        document = Document(path)
        quotes = []
        for para in document.paragraphs:
            line = para.text.split(' - ')
            if len(line) > 1:
                new_quote = Quote(line[0].strip('"'), line[1])
                quotes.append(new_quote)

        return quotes


class TxtIngestor(IngestorInterface):
    """An ingestor that realize IngestorInterface to ingest TXT file type."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        if not cls.can_ingest(path):
            raise Exception('Invalid file type!')

        quotes = []
        with open(path, 'r') as f:
            for line in f.readlines():
                line = line.split(' - ')
                if len(line) > 1:
                    new_quote = Quote(line[0].strip('"'), line[1])
                    quotes.append(new_quote)

        return quotes
