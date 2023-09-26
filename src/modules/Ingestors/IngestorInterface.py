from abc import ABC, abstractmethod
from typing import List

from ..QuoteEngine import Quote


class IngestorInterface(ABC):
    """Interface class for other ingestors."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Class abstract method to check if file ingestable."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[Quote]:
        """Class abstract method to parse the given file."""
        pass
