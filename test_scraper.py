from scraper import scrape_product_page

url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
content = scrape_product_page(url)
print(content)
