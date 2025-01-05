import requests
import feedparser
from colorama import Fore, Style  # For colored output

def fetch_feed(categories, max_results=5):
    """Fetch papers from arXiv for the given categories."""
    base_url = "http://export.arxiv.org/api/query?"
    results = []

    for category in categories:
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
    """Display the fetched feed in a readable format."""
    for category, feed in feed_data:
        print(f"\n{Fore.GREEN}=== Feed for '{category}' ==={Style.RESET_ALL}")
        print(f"{Fore.CYAN}Number of results: {len(feed.entries)}{Style.RESET_ALL}\n")

        for entry in feed.entries:
            title = entry.title
            authors = ", ".join(author.name for author in entry.authors)
            published = entry.published
            abstract = entry.summary
            arxiv_id = entry.id.split("/abs/")[-1]

            # Display the paper details
            print(f"{Fore.YELLOW}Title:{Style.RESET_ALL} {title}")
            print(f"{Fore.YELLOW}Authors:{Style.RESET_ALL} {authors}")
            print(f"{Fore.YELLOW}Published:{Style.RESET_ALL} {published}")
            print(f"{Fore.YELLOW}arXiv ID:{Style.RESET_ALL} {arxiv_id}")
            print(f"{Fore.YELLOW}Abstract:{Style.RESET_ALL} {abstract[:200]}...")  # Truncate abstract
            print(f"{Fore.BLUE}{'-' * 80}{Style.RESET_ALL}\n")
