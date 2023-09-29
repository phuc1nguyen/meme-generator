"""An ingestor that inherits IngestorInterface to handle PDF file type."""

import os
import subprocess
from datetime import datetime
from typing import List

from .IngestorInterface import IngestorInterface
from .TxtIngestor import TxtIngestor
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
        subprocess.run(['pdftotext', '-simple', path, tmp])
        quotes = TxtIngestor.parse(tmp)
        os.remove(tmp)

        return quotes
