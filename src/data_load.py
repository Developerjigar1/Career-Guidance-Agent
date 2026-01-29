import pandas as pd

def load_data(file_path):
    """
    Load the career dataset from CSV.
    
    Args:
        file_path (str): Path to CSV file
    
    Returns:
        pd.DataFrame: Loaded dataset
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
