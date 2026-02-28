import requests
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

# API endpoint
url = "https://jsonplaceholder.typicode.com/posts"

try:
    # Make GET request
    response = requests.get(url)
    response.raise_for_status()  # Will raise an exception for 4xx/5xx errors
    
    # If successful, parse and display data
    posts = response.json()
    logging.info("Fetched Posts:")
    for post in posts[:5]:
        logging.info(f"Title: {post['title']}\nBody: {post['body']}\n")
    
except requests.exceptions.RequestException as e:
    logging.error(f"Error fetching data: {e}")