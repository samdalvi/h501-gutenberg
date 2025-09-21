# tt_gutenberg/utils.py

def clean_aliases(df, alias_col="alias"):
    """
    Returns a cleaned list of aliases, removing empty or null values.
    """
    return df[alias_col].dropna().unique().tolist()


def count_translations(df, alias_col="alias"):
    """
    Returns a dictionary mapping each alias to its translation count.
    """
    counts = df.groupby(alias_col).size().to_dict()
    return counts
