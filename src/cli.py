from src.config_manager import load_config, add_category, remove_category, show_subscribed_categories
from src.arxiv_fetcher import fetch_feed, display_feed
import questionary

def display_menu():
    """Display an interactive menu."""
    choices = [
        "View Feed",
        "Add Category",
        "Remove Category",
        "Show Subscribed Categories",
        "Exit"
    ]
    return questionary.select("Choose an option:", choices=choices).ask()

def main():
    while True:
        choice = display_menu()
        config = load_config()

        if choice == "View Feed":
            print("\nFetching feed for subscribed categories...")
            feed_data = fetch_feed(config["subscribed_categories"], config["max_results"])
            display_feed(feed_data)
        elif choice == "Add Category":
            category = input("Enter the category to add (e.g., astro-ph.HE): ")
            add_category(category)
        elif choice == "Remove Category":
            category = input("Enter the category to remove (e.g., astro-ph.HE): ")
            remove_category(category)
        elif choice == "Show Subscribed Categories":
            show_subscribed_categories()
        elif choice == "Exit":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
