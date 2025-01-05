import json
from pathlib import Path

CONFIG_PATH = Path("config/config.json")

def load_config():
    """Load the configuration from the config file."""
    try:
        with open(CONFIG_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Config file not found. Creating a new one with default settings.")
        default_config = {"subscribed_categories": [], "max_results": 5}
        save_config(default_config)
        return default_config

def save_config(config):
    """Save the configuration to the config file."""
    with open(CONFIG_PATH, "w") as file:
        json.dump(config, file, indent=4)

def add_category(category):
    """Add a new category to the subscribed list."""
    config = load_config()
    if category not in config["subscribed_categories"]:
        config["subscribed_categories"].append(category)
        save_config(config)
        print(f"Added '{category}' to subscribed categories.")
    else:
        print(f"'{category}' is already subscribed.")

def remove_category(category):
    """Remove a category from the subscribed list."""
    config = load_config()
    if category in config["subscribed_categories"]:
        config["subscribed_categories"].remove(category)
        save_config(config)
        print(f"Removed '{category}' from subscribed categories.")
    else:
        print(f"'{category}' is not in the subscribed list.")

def show_subscribed_categories():
    """Display the list of subscribed categories."""
    config = load_config()
    categories = config.get("subscribed_categories", [])
    if categories:
        print("\n=== Subscribed Categories ===")
        for idx, category in enumerate(categories, start=1):
            print(f"{idx}. {category}")
    else:
        print("\nNo categories subscribed yet.")
