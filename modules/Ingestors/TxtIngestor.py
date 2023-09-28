"""An ingestor that inherits IngestorInterface to handle TXT file type."""

from typing import List

from .IngestorInterface import IngestorInterface
from ..QuoteEngine import Quote
from .._const.Extension import QuoteExtension


class TxtIngestor(IngestorInterface):
    """A TXT Ingestor."""

    allowed_extensions = [QuoteExtension.TXT.value]

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        """Overwritten classmethod to parse TXT file."""
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
