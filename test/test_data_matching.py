import pytest
import pandas as pd
from unittest.mock import patch
from src.data_matching import fuzzy_match, fetch_data_from_api

def test_fuzzy_match():
    census_data = {
        'first_name': ['john', 'jane', 'doe'],
        'last_name': ['doe', 'smith', 'johnson'],
        'address': ['123 main st', '456 elm st', '789 oak st'],
        'street_number': ['123', '456', '789'],
        'email': ['john@example.com', 'jane@example.com', 'doe@example.com'],
        'zipcode': ['12345', '67890', '11223'],
        'race': ['white', 'black', 'asian']
    }
    census_df = pd.DataFrame(census_data)
    
    row = {
        'first_name': 'john',
        'last_name': 'doe',
        'address': '123 main st',
        'street_number': '123',
        'email': 'john@example.com',
        'zipcode': '12345',
        'race': 'white'
    }
    
    matched_row = fuzzy_match(row, census_df)
    assert matched_row['first_name'] == 'john'
    assert matched_row['last_name'] == 'doe'

def test_fuzzy_match_no_match():
    census_data = {
        'first_name': ['john', 'jane', 'doe'],
        'last_name': ['doe', 'smith', 'johnson'],
        'address': ['123 main st', '456 elm st', '789 oak st'],
        'street_number': ['123', '456', '789'],
        'email': ['john@example.com', 'jane@example.com', 'doe@example.com'],
        'zipcode': ['12345', '67890', '11223'],
        'race': ['white', 'black', 'asian']
    }
    census_df = pd.DataFrame(census_data)
    
    row = {
        'first_name': 'mike',
        'last_name': 'tyson',
        'address': '999 unknown st',
        'street_number': '999',
        'email': 'mike@example.com',
        'zipcode': '99999',
        'race': 'hispanic'
    }
    
    matched_row = fuzzy_match(row, census_df)
    assert matched_row is None

@patch('src.data_matching.requests.get')
def test_fetch_data_from_api(mock_get):
    mock_response = mock_get.return_value
    mock_response.json.return_value = [
        {'first_name': 'john', 'last_name': 'doe', 'address': '123 main st', 'street_number': '123', 'email': 'john@example.com', 'zipcode': '12345', 'race': 'white'}
    ]
    mock_response.raise_for_status = lambda: None
    
    api_url = 'https://api.example.com/test_data'
    df = fetch_data_from_api(api_url)
    
    assert not df.empty
    assert df.iloc[0]['first_name'] == 'john'
    assert df.iloc[0]['last_name'] == 'doe'