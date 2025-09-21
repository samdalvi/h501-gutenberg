# tt_gutenberg/authors.py
import pandas as pd
from tt_gutenberg.data_fetcher import fetch_gutenberg_authors
from tt_gutenberg.utils import clean_aliases, count_translations

def list_authors(by_languages=False, alias=True):
    """
    Returns a list of author aliases sorted by translation count.
    """
    if not alias:
        raise ValueError("Currently only alias=True is supported")
    
    # Fetch the dataset
    df = fetch_gutenberg_authors()
    
    # Count translations
    translation_counts = count_translations(df)
    
    # Sort aliases by translation count descending
    sorted_aliases = sorted(
        translation_counts.items(), key=lambda x: x[1], reverse=True
    )
    
    # Extract aliases
    result = [alias for alias, _ in sorted_aliases]
    
    # Clean the list
    result = clean_aliases(pd.DataFrame({"alias": result}))
    
    return result
