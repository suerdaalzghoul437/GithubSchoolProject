import requests

def fetch_random_data():
    # Replace with your own API key or data source
    url = "https://api.example.com/data"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to retrieve data. Status code: {response.status_code}")

def main():
    data = fetch_random_data()
    print(data)

if __name__ == "__main__":
    main()
