import os
import subprocess
from datetime import datetime
from typing import List

from .IngestorInterface import IngestorInterface
from ..QuoteEngine import Quote
from .const.Extension import QuoteExtension


class PdfIngestor(IngestorInterface):
    """An ingestor that realize IngestorInterface to handle PDF file type."""

    allowed_extensions = [QuoteExtension.PDF]

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
