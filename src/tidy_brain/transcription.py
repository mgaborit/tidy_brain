import abc
from datetime import datetime

class Entry:
    """Class representing a transcription entry."""
    def __init__(self, content: str, context: dict = None):
        self.timestamp = datetime.now()
        self.content = content
        self.context = context

class Transcriptor(metaclass=abc.ABCMeta):
    """Base class for transcription handlers."""
    
    @abc.abstractmethod
    def write(self, entry: Entry) -> None:
        """Write a transcription entry to the appropriate location."""
        raise NotImplementedError("Subclasses must implement this method.")
    

class Transcriptable(metaclass=abc.ABCMeta):
    """Interface for objects that can be transcribed."""

    @abc.abstractmethod
    def register(self, transcriptor: Transcriptor) -> None:
        """Register a transcriptor to handle transcriptions."""
        raise NotImplementedError("Subclasses must implement this method.")

    @abc.abstractmethod
    def accept(self, entry: Entry) -> None:
        """Transcribe the entry if it matches certain criteria."""
        raise NotImplementedError("Subclasses must implement this method.")