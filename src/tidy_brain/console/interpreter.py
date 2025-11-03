class Interpreter:
    """REPL interpreter."""
    
    def __init__(self):
        self.commands = {
            'exit': self._exit,
        }
    
    def run(self):
        """Start the interactive REPL loop."""
        while True:
            try:
                input_entry = input(">>> ").strip()
                
                if not input_entry:
                    continue
                    
                self._process_input(input_entry)
                
            except (KeyboardInterrupt, EOFError):
                self._exit(self)
    
    def _process_input(self, input_entry: str):
        """Process the user input."""
        command_candidate = input_entry.lower()
        
        if command_candidate in self.commands:
            self.commands[command_candidate]()
        else:
            print(f"Unknown command: {input_entry}")
            print("Type 'help' for available commands.")
    
    def _exit(self):
        """Exit the application."""
        exit(0)