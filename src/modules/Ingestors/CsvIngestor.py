import pandas as pd
from typing import List

from .IngestorInterface import IngestorInterface
from ..QuoteEngine import Quote
from .const.Extension import QuoteExtension


class CSVIngestor(IngestorInterface):
    """An ingestor that realize IngestorInterface to handle CSV file type."""

    allowed_extensions = [QuoteExtension.CSV]

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
