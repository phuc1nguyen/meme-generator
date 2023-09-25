from docx import Document
from typing import List

from .IngestorInterface import IngestorInterface
from ..QuoteEngine import Quote
from .const.Extension import QuoteExtension


class DocxIngestor(IngestorInterface):
    """An ingestor that realize IngestorInterface to handle Docx file type."""

    allowed_extensions = [QuoteExtension.DOCX]

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
