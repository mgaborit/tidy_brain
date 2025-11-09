import readline # needed for input history and editing

from transcription import Entry, Transcriptor

COMMAND_PREFIX = '\\'
DEFAULT_PROJECT = 'Misc'

class Interpreter:
    """REPL interpreter."""

    def __init__(self):
        self.transcriptors = []
        self.commands = {
            'quit': self._exit,
            'q': self._exit,
            'help': self._help,
            'h': self._help,
            'project': self._set_project,
            'p': self._set_project,
        }
        self.context = {'project': DEFAULT_PROJECT}

    def add_transcriptor(self, transcriptor: Transcriptor) -> None:
        """Add a transcription writer."""
        self.transcriptors.append(transcriptor)

    def run(self) -> None:
        """Start the interactive REPL loop."""
        while True:
            try:
                input_entry = input(self._format_prompt()).strip()
                
                if not input_entry:
                    continue
                    
                if input_entry.startswith(COMMAND_PREFIX):
                    self._process_command(input_entry)
                else:
                    self._process_entry(input_entry)
                
            except (KeyboardInterrupt, EOFError):
                self._exit()
            except ValueError:
                self._help()
            except Exception as e:
                print(e)

    def _process_command(self, input_entry: str) -> None:
        """Process a command."""
        command_name, *arguments = input_entry[len(COMMAND_PREFIX):].strip().lower().split()
        if command_name in self.commands:
            self.commands[command_name](arguments)
        else:
            raise ValueError

    def _process_entry(self, input_entry: str) -> None:
        """Process a transcription entry."""
        entry = Entry(content=input_entry, context=self.context)
        for transcriptor in self.transcriptors:
            transcriptor.write(entry)

    def _exit(self, arguments: list[str]) -> None:
        """Exit the application."""
        exit(0)
    
    def _help(self, arguments: list[str]) -> None:
        """Display help information."""
        help_text = """Available commands:
\\help or \\h - Show this help message
\\quit or \\q - Exit the application
\\project <name> or \\p <name> - Set the current project (default: Misc)
To add a transcription entry, simply type it and press Enter."""
        print(help_text)

    def _set_project(self, arguments: list[str]) -> None:
        """Set the current project."""
        if arguments:
            self.context['project'] = arguments[0]
        else:
            self.context['project'] = DEFAULT_PROJECT

    def _format_prompt(self) -> str:
        """Format the input prompt."""
        prompt = ''
        if self.context['project'] != DEFAULT_PROJECT:
            prompt = f"[{self.context['project']}]"
        prompt += '> '
        return prompt