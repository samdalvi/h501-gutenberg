# tt_gutenberg/data_fetcher.py

# tt_gutenberg/data_fetcher.py

# tt_gutenberg/data_fetcher.py

import pandas as pd

def fetch_gutenberg_authors():
    """
    Fetches the latest TidyTuesday Gutenberg authors dataset.
    """
    url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv"
    return pd.read_csv(url)
