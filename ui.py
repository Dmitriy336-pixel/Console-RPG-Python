import questionary
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
class UI:
    def __init__(self):
        self.console = Console()
        
    #(rich)    
    def say(self, text="", style=None):
            self.console.print(text, style=style)
            
    def title(self, text):
            self.console.rule(text)
            
    def table(self, title, colums, rows):
            t = Table(title=title)
            for col in colums:
                t.add_column(col)
            for row in rows:
                t.add_row(*[str(x) for x in row])
            self.console.print(t)
        
    def panel(self, title, body):
        self.console.print(Panel(body, title=title, expand=False))
        
    def confirm(self, prompt):
        return bool(questionary.confirm(prompt, default=False).ask())
     
            
    #(questionary)
    def choose(self, prompt, options, cancel_value=None, search=False):
        choices = [questionary.Choice(name, value=val) for name, val in options]
        q = questionary.select(
            prompt,
            choices=choices,
            use_search_filter=search,
            use_jk_keys=not search,   # вместе эти два режима не работают
        )

        @q.application.key_bindings.add("escape", eager=True)
        def _(event):
            event.app.exit(result=cancel_value)

        answer = q.ask()
        return cancel_value if answer is None else answer
    def ask_text(self, prompt):
        return (questionary.text(prompt).ask() or "").strip()
    
    
ui=UI()    