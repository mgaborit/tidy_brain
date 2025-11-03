from datetime import datetime

class Entry:
    def __init__(self, content: str):
        self.timestamp = datetime.now()
        self.content = content
