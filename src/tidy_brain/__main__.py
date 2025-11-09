from transcriptors.file_transcriptors import DailyFileTranscriptor
from console import Interpreter

WORKSPACE_DIR = "/home/martin/dev/sandbox/tidy_brain"

daily = DailyFileTranscriptor(WORKSPACE_DIR)

interpreter = Interpreter()
interpreter.add_transcriptor(daily)
interpreter.run()
