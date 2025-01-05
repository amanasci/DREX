from src.config_manager import load_config, add_category, remove_category, show_subscribed_categories
from src.arxiv_fetcher import fetch_feed, display_feed

def display_menu():
    """Display the main menu."""
    print("\n=== arXiv Explorer ===")
    print("1. View Feed")
    print("2. Add Category")
    print("3. Remove Category")
    print("4. Show Subscribed Categories")
    print("5. Exit")
    choice = input("Enter your choice (1-4): ")
    return choice

def main():
    while True:
        choice = display_menu()
        config = load_config()

        if choice == "1":
            print("\nFetching feed for subscribed categories...")
            feed_data = fetch_feed(config["subscribed_categories"], config["max_results"])
            display_feed(feed_data)
        elif choice == "2":
            category = input("Enter the category to add (e.g., astro-ph.HE): ")
            add_category(category)
        elif choice == "3":
            category = input("Enter the category to remove (e.g., astro-ph.HE): ")
            remove_category(category)
        elif choice == "4":
            show_subscribed_categories()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
