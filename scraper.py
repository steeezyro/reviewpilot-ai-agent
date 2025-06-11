# scraper.py

import requests
from bs4 import BeautifulSoup

def scrape_product_page(url):
    """
    Takes a product URL and returns the title and readable page text.
    """
    try:
        res = requests.get(url)
        res.raise_for_status()  # Raise error for bad status

        soup = BeautifulSoup(res.text, 'html.parser')

        # Try to extract the product title
        title = soup.find('h1')
        title_text = title.get_text(strip=True) if title else "No title found"

        # Try to get visible text from all <p> tags
        paragraphs = soup.find_all('p')
        paragraph_text = "\n".join(p.get_text(strip=True) for p in paragraphs)

        # Combine title and text
        full_content = f"{title_text}\n\n{paragraph_text}"
        return full_content

    except Exception as e:
        return f"[ERROR] Failed to scrape page: {e}"
