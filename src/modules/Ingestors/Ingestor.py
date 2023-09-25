from .CsvIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PdfIngestor import PdfIngestor
from .TxtIngestor import TxtIngestor
from .const.Extension import QuoteExtension


class Ingestor():
    ingestors = [CSVIngestor, DocxIngestor, PdfIngestor, TxtIngestor]

    def parse(self, path: str):
        ext = path.split('.')[-1]
        if ext == QuoteExtension.CSV:
            return CSVIngestor.parse(path)
        if ext == QuoteExtension.DOCX:
            return DocxIngestor.parse(path)
        if ext == QuoteExtension.PDF:
            return PdfIngestor.parse(path)
        if ext == QuoteExtension.TXT:
            return TxtIngestor.parse(path)
