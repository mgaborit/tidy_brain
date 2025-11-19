"""Module for tag transcriptables in Tidy Brain application."""
from ..transcription import Entry, Transcriptable

PERSON_PREFIX = "@"

class Person(Transcriptable):
    """Represents a section within a project."""
    def __init__(self, short_name: str, full_name: str = "", email: str = ""):
        super().__init__()
        self.short_name = short_name
        self.full_name = full_name
        self.email = email

    def accept(self, entry: Entry) -> None:
        if self.transcriptors and f"{PERSON_PREFIX}{self.short_name}" in entry.content:
            for transcriptor in self.transcriptors:
                transcriptor.write(entry)
