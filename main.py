from scraper import scrape_product_page
from prompts import SUMMARY_PROMPT, CRITIQUE_PROMPT, FAKE_REVIEWS_PROMPT
from gpt_calls import call_gpt

def main():
    print("🛍️ Welcome to ReviewPilot\n")

    url = input("🔗 Enter a product page URL: ").strip()
    print("\n🔎 Scraping page...")

    content = scrape_product_page(url)
    if content.startswith("[ERROR]"):
        print(content)
        return

    print("\n✅ Page scraped successfully.\n")

    # --- Run GPT Prompts ---
    print("📄 Generating Product Summary...\n")
    summary = call_gpt(SUMMARY_PROMPT.format(content=content))
    print(summary)

    print("\n🛠️  Critiquing Product Page...\n")
    critique = call_gpt(CRITIQUE_PROMPT.format(content=content))
    print(critique)

    print("\n⭐ Creating Fake Customer Reviews...\n")
    reviews = call_gpt(FAKE_REVIEWS_PROMPT.format(content=content))
    print(reviews)

if __name__ == "__main__":
    main()