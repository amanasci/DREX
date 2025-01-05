# DREX
---

DREX (Daily ArXiv EXplorer) is a Python-based command-line tool that allows users to fetch and display
the latest research papers from arXiv.org based on specified categories. The tool provides an interactive
menu for managing subscribed categories and viewing the latest papers.

## Features

- Fetch the latest research papers from arXiv.org for specified categories.
- Display fetched papers in a formatted table using the `rich` library.
- Manage subscribed categories (add, remove, and view).
- Interactive command-line interface using `questionary`.

## Installation

1. Clone the repository:

```sh
git clone https://github.com/amanasci/DREX.git
cd DREX
```

2. Create a virtual environment (optional but recommended):

```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required dependencies:

```sh
pip install -r requirements.txt
```

## Usage

1. Run the main script:

```sh
python main.py
```

2. Follow the interactive menu to choose an option:

- **View Feed**: Fetch and display the latest papers for subscribed categories.
- **Add Category**: Add a new category to the subscribed list.
- **Remove Category**: Remove a category from the subscribed list.
- **Show Subscribed Categories**: Display the list of currently subscribed categories.
- **Exit**: Exit the program.

## Configuration

The configuration is stored in a JSON file located at `config/config.json`. The configuration file includes the following settings:

- `subscribed_categories`: A list of categories to fetch papers from.
- `max_results`: The maximum number of results to fetch for each category.

### Example Configuration

```json
{
    "subscribed_categories": ["astro-ph.HE", "cs.AI"],
    "max_results": 5
}
```

## Project Structure

```
DREX/
├── config/
│   └── config.json
│
│──── src/
│       ├── arxiv_fetcher.py
│       ├── cli.py
│       └── config_manager.py
├── requirements.txt
├── main.py
└── README.md
```



## Acknowledgements

- [arXiv.org](https://arxiv.org/) for providing access to research papers.
- The authors of the `requests`, `feedparser`, `rich`, and `questionary` libraries for their excellent tools.

---
