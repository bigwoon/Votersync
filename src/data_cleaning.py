import pandas as pd

def load_data(file_path):
    """Load data from a CSV file."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Clean the data."""
    # Drop duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.fillna(method='ffill').fillna(method='bfill')

    # Convert columns to appropriate data types
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['age'] = pd.to_numeric(df['age'], errors='coerce')

    # Remove rows with invalid data
    df = df.dropna(subset=['date', 'age'])

    return df

def save_data(df, file_path):
    """Save the cleaned data to a CSV file."""
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    input_file = 'input_data.csv'
    output_file = 'cleaned_data.csv'

    # Load the data
    data = load_data(input_file)

    # Clean the data
    cleaned_data = clean_data(data)

    # Save the cleaned data
    save_data(cleaned_data, output_file)