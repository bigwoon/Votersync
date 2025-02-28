import requests

class DataIntegration:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self, endpoint):
        url = f"{self.api_url}/{endpoint}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def post_data(self, endpoint, data):
        url = f"{self.api_url}/{endpoint}"
        response = requests.post(url, json=data)
        if response.status_code == 201:
            return response.json()
        else:
            response.raise_for_status()

# Example usage
if __name__ == "__main__":
    api_url = "https://example.com/api"
    integration = DataIntegration(api_url)

    # Fetch data from an endpoint
    try:
        data = integration.fetch_data("voters")
        print("Fetched data:", data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

    # Post data to an endpoint
    new_voter = {"name": "John Doe", "age": 30}
    try:
        response = integration.post_data("voters", new_voter)
        print("Posted data:", response)
    except requests.exceptions.RequestException as e:
        print(f"Error posting data: {e}")