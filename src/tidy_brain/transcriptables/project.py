from transcription import Entry, Transcriptable, Transcriptor

class Project(Transcriptable):
    """Represents a project."""
    def __init__(self, name: str):
        self.name = name
        self.sections = {}

    def register(self, transcriptor: Transcriptor) -> None:
        pass

    def accept(self, entry: Entry) -> None:
        pass

class Section(Transcriptable):
    """Represents a section within a project."""
    def __init__(self, name: str):
        self.name = name
        self.transcriptors = []

    def register(self, transcriptor: Transcriptor) -> None:
        pass

    def accept(self, entry: Entry) -> None:
        pass
