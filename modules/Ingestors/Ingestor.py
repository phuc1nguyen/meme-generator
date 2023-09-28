"""Class to encapsulate our Ingestors (Strategy Objects)."""

from typing import List

from .IngestorInterface import IngestorInterface
from .CsvIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PdfIngestor import PdfIngestor
from .TxtIngestor import TxtIngestor
from ..QuoteEngine import Quote


class Ingestor(IngestorInterface):
    """Main ingestor class that has smart parser."""

    ingestors = [CSVIngestor, DocxIngestor, PdfIngestor, TxtIngestor]

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        """Overwritten method to choose correct parser for given file."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
