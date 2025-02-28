import pandas as pd
from fuzzywuzzy import fuzz
import os
import requests

# Function to perform fuzzy matching on a row
def fuzzy_match(row, census_df):
    potential_matches = census_df.apply(lambda x: (
        fuzz.token_sort_ratio(row['first_name'], x['first_name']) +
        fuzz.token_sort_ratio(row['last_name'], x['last_name']) +
        fuzz.token_sort_ratio(row['address'], x['address']) +
        fuzz.token_sort_ratio(row['street_number'], x['street_number']) +
        fuzz.token_sort_ratio(row['email'], x['email']) +
        fuzz.token_sort_ratio(row['zipcode'], x['zipcode']) +
        fuzz.token_sort_ratio(row['race'], x['race'])
    ) / 7, axis=1)
    
    best_match_index = potential_matches.idxmax()
    best_match_score = potential_matches.max()
    if best_match_score > 80:  # Threshold for matching
        return census_df.iloc[best_match_index]
    else:
        return None

# Function to fetch data from an API
def fetch_data_from_api(api_url):
    response = requests.get(api_url)
    response.raise_for_status()  # Raise an error for bad status codes
    return pd.DataFrame(response.json())

# Function to load data from a CSV file
def load_data(file_path):
    return pd.read_csv(file_path)

# Main function

def main():
    # Fetch data from APIs
    npg_van_api_url = 'https://api.securevan.com/v4/people/find'
    census_api_url = 'https://api.census.gov/data/'

    npg_van_df = fetch_data_from_api(npg_van_api_url)
    census_df = fetch_data_from_api(census_api_url)

    # Normalize the data
    npg_van_df['first_name'] = npg_van_df['first_name'].str.lower().str.strip()
    npg_van_df['last_name'] = npg_van_df['last_name'].str.lower().str.strip()
    npg_van_df['address'] = npg_van_df['address'].str.lower().str.strip()
    npg_van_df['street_number'] = npg_van_df['street_number'].str.lower().str.strip()
    npg_van_df['email'] = npg_van_df['email'].str.lower().str.strip()
    npg_van_df['zipcode'] = npg_van_df['zipcode'].str.lower().str.strip()
    npg_van_df['race'] = npg_van_df['race'].str.lower().str.strip()

    census_df['first_name'] = census_df['first_name'].str.lower().str.strip()
    census_df['last_name'] = census_df['last_name'].str.lower().str.strip()
    census_df['address'] = census_df['address'].str.lower().str.strip()
    census_df['street_number'] = census_df['street_number'].str.lower().str.strip()
    census_df['email'] = census_df['email'].str.lower().str.strip()
    census_df['zipcode'] = census_df['zipcode'].str.lower().str.strip()
    census_df['race'] = census_df['race'].str.lower().str.strip()

    # Load user input data from a CSV file
    user_file_path = input("Enter the path to your CSV file: ")
    user_df = load_data(user_file_path)

    # Normalize the user data
    user_df['first_name'] = user_df['first_name'].str.lower().str.strip()
    user_df['last_name'] = user_df['last_name'].str.lower().str.strip()
    user_df['address'] = user_df['address'].str.lower().str.strip()
    user_df['street_number'] = user_df['street_number'].str.lower().str.strip()
    user_df['email'] = user_df['email'].str.lower().str.strip()
    user_df['zipcode'] = user_df['zipcode'].str.lower().str.strip()
    user_df['race'] = user_df['race'].str.lower().str.strip()

    # Apply the fuzzy_match function to each row in user_df
    user_df['matched_row'] = user_df.apply(lambda row: fuzzy_match(row, census_df), axis=1)

    # Filter out rows with no match
    matched_df = user_df[user_df['matched_row'].notnull()]

    # Ensure the output directory exists
    os.makedirs('/workspaces/Voter_sync_app.py/data/input/processed/output', exist_ok=True)

    # Save the matched results to a new CSV file
    output_path = '/workspaces/Voter_sync_app.py/data/input/processed/output/matched_results.csv'
    matched_df.to_csv(output_path, index=False)

    print(f"Matched data saved to '{output_path}'")

if __name__ == "__main__":
    main()