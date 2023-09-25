from .IngestorInterface import CSVIngestor, DocxIngestor, IngestorInterface, PdfIngestor, TxtIngestor


class Ingestor(IngestorInterface):
    ingestors = [CSVIngestor, PdfIngestor, DocxIngestor, TxtIngestor]

    @classmethod
    def parse(cls, path: str):
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
