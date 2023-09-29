"""Represent model for a quote."""


class Quote:
    """A quote that contains a body and an author."""

    def __init__(self, body: str, author: str):
        """Create a new quote."""
        self.body = body
        self.author = author

    def __eq__(self, other: object) -> bool:
        """Customized equality between two quotes."""
        return self.body == other.body and self.author == other.author

    def __repr__(self) -> str:
        """Return a computer readable string of this object."""
        return f"\"{self.body}\" - {self.author}"
