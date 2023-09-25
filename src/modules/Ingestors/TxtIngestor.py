from typing import List

from .IngestorInterface import IngestorInterface
from ..QuoteEngine import Quote
from .const.Extension import QuoteExtension


class TxtIngestor(IngestorInterface):
    """An ingestor that realize IngestorInterface to ingest TXT file type."""

    allowed_extensions = [QuoteExtension.TXT]

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
