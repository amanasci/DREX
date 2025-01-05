import requests
import feedparser

from rich.console import Console
from rich.table import Table

from rich.progress import track

console = Console()


def fetch_feed(categories, max_results=5):
    """Fetch papers from arXiv for the given categories."""
    base_url = "http://export.arxiv.org/api/query?"
    results = []

    for category in track(categories, description="Fetching feeds..."):
        query = f"cat:{category}"
        params = {
            "search_query": query,
            "start": 0,
            "max_results": max_results,
            "sortBy": "submittedDate",
            "sortOrder": "descending"
        }
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            feed = feedparser.parse(response.text)
            results.append((category, feed))
        else:
            print(f"Error fetching feed for category '{category}': {response.status_code}")

    return results

def display_feed(feed_data):
    """Display the fetched feed using rich."""
    for category, feed in feed_data:
        console.print(f"\n[bold green]=== Feed for '{category}' ===[/bold green]")
        console.print(f"[cyan]Number of results: {len(feed.entries)}[/cyan]\n")

        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Title", style="yellow")
        table.add_column("Authors", style="cyan")
        table.add_column("Published", style="blue")
        table.add_column("arXiv ID", style="green")

        for entry in feed.entries:
            title = entry.title
            authors = ", ".join(author.name for author in entry.authors)
            published = entry.published
            arxiv_id = entry.id.split("/abs/")[-1]

            table.add_row(title, authors, published, arxiv_id)

        console.print(table)
