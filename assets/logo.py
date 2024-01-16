from rich.box import HEAVY
from rich.panel import Panel

from .console import console


LOGO = """
                            __         
 _______  ___ _  _____ ____/ /____ ____
/ __/ _ \/ _ \ |/ / -_) __/ __/ -_) __/
\__/\___/_//_/___/\__/_/  \__/\__/_/                                      
                            mp4 -> mp3
"""


class ProgramLogo:
    # @staticmethod
    def _setup_padding():
        #! Actually can use rich.text for this but the LOGO alignment is not perfect
        logo_width = max(len(line) for line in LOGO.split("\n"))
        padding = (console.width - logo_width) // 2
        return "\n".join(f"{' ' * padding}{line}" for line in LOGO.split("\n"))

    # @classmethod
    def setup_logo(cls):
        console.print(
            Panel(
                f"[blue1]{cls._setup_padding()}[/]",
                border_style="purple",
                box=HEAVY,
            ),
        )