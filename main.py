from scraper import scrape_product_page
from prompts import SUMMARY_PROMPT, CRITIQUE_PROMPT, FAKE_REVIEWS_PROMPT
from gpt_calls import call_gpt
from datetime import datetime
import os

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

    # --- Save output to a file ---
    os.makedirs("outputs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"outputs/review_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write("📄 Product Summary:\n")
        f.write(summary + "\n\n")
        f.write("🛠️ Product Critique:\n")
        f.write(critique + "\n\n")
        f.write("⭐ Fake Reviews:\n")
        f.write(reviews + "\n")

    print(f"\n📁 Results saved to {filename}")

if __name__ == "__main__":
    main()