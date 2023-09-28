"""An ingestor that inherits IngestorInterface to handle PDF file type."""

import os
import subprocess
from datetime import datetime
from typing import List

from .IngestorInterface import IngestorInterface
from ..QuoteEngine import Quote
from .._const.Extension import QuoteExtension


class PdfIngestor(IngestorInterface):
    """A PDF Ingestor."""

    allowed_extensions = [QuoteExtension.PDF.value]

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        """Overwritten classmethod to parse PDF file."""
        if not cls.can_ingest(path):
            raise Exception('Invalid file type!')

        tmp = f"./tmp/{round(datetime.now().timestamp())}.txt"
        subprocess.run(['pdftotext', path, tmp])
        with open(tmp, 'r') as f:
            for line in f.readlines():
                pdf_quotes = line.strip('\x0c\n').split(' "')
                quotes = [Quote(quote[0].strip('"'), quote[1])
                          for quote in pdf_quotes]
                # because all quotes result one first line in text file
                break
        os.remove(tmp)

        return quotes
