import re

def clean_text(text):
    """
    Clean text by converting to lowercase and removing special characters.
    
    Args:
        text (str): Input text
    
    Returns:
        str: Cleaned text
    """
    if isinstance(text, str):
        text = text.lower()
        text = re.sub(r'[^a-zA-Z, ]', '', text)
        return text
    else:
        return ""
