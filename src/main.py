import argparse
import os
import time
from typing import List

from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn, TimeElapsedColumn

from src.parser import LogMessage, parse_log_file

# Shared console instance
console = Console()


# Typing animation
def typing_print(text: str, delay: float = 0.05) -> None:
    """
    Printing a single line using a lightweight typing animation.
    The goal is to add a subtle "alive" feeling to the CLI output without
    making the user wait too long. This function prints characters one by one.
    """
    for ch in text:
        console.print(ch, end="", style="white", highlight=False)
        time.sleep(delay)
    console.print()


# Animated parsing + progress bar
def animate_parsing(path: str) -> List[LogMessage]:
    """
    Wrapper around the actual binary parser that adds a small progress bar.
    This does not indicate real progress but adds a more
    polished and user-friendly experience.
    """

    # shows the filename 
    filename = os.path.basename(path)

    console.print(f"[bold cyan]Reading binary file:[/] {filename}")
    console.print("[bold cyan]Parsing messages from logi.bin...[/]")

    # Configure the Rich progress bar
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=40),
        TextColumn("{task.percentage:>3.0f}%"),
        TimeElapsedColumn(),
        console=console,
    ) as progress:
        task_id = progress.add_task("Working", total=100)

        # Parse instantly
        messages = parse_log_file(path)

        # Animate the bar for visual effect only
        for _ in range(20):  # 20 steps * 5% = 100%
            progress.update(task_id, advance=5)
            time.sleep(0.02)

        progress.update(task_id, completed=100)

    # Summary line
    console.print(f"\n[bold green]Done![/] Found [bold]{len(messages)}[/] message(s).\n")

    return messages


# Block view output
def display_block_view(messages: List[LogMessage]) -> None:
    """
    Display each message in block-style UI.
    """

    if not messages:
        console.print("[yellow]No messages to display.[/]")
        return

    # Section title separator
    console.rule("[bold cyan]Block View[/bold cyan]")

    total = len(messages)

    for idx, msg in enumerate(messages, start=1):
        console.print()  # spacing
        console.print("=" * 70, style="magenta")

        # Metadata for each message block
        console.print(f"[bold magenta]Message {idx} of {total}[/]")
        console.print(f"[bold cyan]Sequence Number:[/] {msg.sequence_number}\n")

        # Message text header
        console.print("[bold yellow]Text:[/]")
        
        # Apply typing animation per line (preserve newline formatting)
        for line in msg.text.splitlines():
            typing_print(line, delay=0.05)

        console.print("=" * 70, style="magenta")


# CLI argument parser
def parse_args() -> argparse.Namespace:
    """
    Basic command-line argument parser.
    Only the input file is required.
    No speed arguments or extras—kept intentionally simple.
    """
    parser = argparse.ArgumentParser(
        description="Parse a Logitech logi.bin file and display messages in a block view."
    )
    parser.add_argument(
        "-i",
        "--input",
        required=True,
        help="Path to the logi.bin file to parse.",
    )
    return parser.parse_args()


# Main execution entry point
def main() -> None:
    # Parse CLI args
    args = parse_args()
    bin_path = os.path.abspath(args.input)

    # Validate existence
    if not os.path.exists(bin_path):
        console.print(f"[red]File not found:[/] {bin_path}")
        raise SystemExit(1)

    # Run animation
    messages = animate_parsing(bin_path)
    display_block_view(messages)


if __name__ == "__main__":
    main()