import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error: {response.status_code}")
        return None

url = "https://example.com"
html_content = fetch_html(url)

if html_content is not None:
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extracting and printing some sample HTML elements
    heading = soup.find("h1", text="Heading")
    if heading:
        print(heading.text)
        
    paragraph = soup.find("p", text="Sample Paragraph")
    if paragraph:
        print(paragraph.text)

    # Add more code to process the HTML content as needed
else:
    print("Error: Unable to fetch the webpage.")
