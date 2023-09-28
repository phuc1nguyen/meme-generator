"""An ingestor that inherits IngestorInterface to handle CSV file type."""

import pandas as pd
from typing import List

from .IngestorInterface import IngestorInterface
from ..QuoteEngine import Quote
from .._const.Extension import QuoteExtension


class CsvIngestor(IngestorInterface):
    """A CSV Ingestor."""

    allowed_extensions = [QuoteExtension.CSV.value]

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        """Overwritten classmethod to parse CSV file."""
        if not cls.can_ingest(path):
            raise Exception('Invalid file type!')

        df = pd.read_csv(path)
        body = df['body']
        author = df['author']
        quotes = [Quote(body[i].strip('"'), author[i]) for i in range(2)]

        return quotes
