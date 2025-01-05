from src.cli import main
from rich.console import Console

console = Console()

def display_welcome():
    console.print("[bold blue]====================================[/bold blue]")
    console.print("[bold blue]      Welcome to arXiv Explorer     [/bold blue]")
    console.print("[bold blue]====================================[/bold blue]")
    console.print("\nExplore the latest research papers from arXiv!\n")

if __name__ == "__main__":
    display_welcome()
    main()
