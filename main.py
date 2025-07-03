import asyncio
from scraper.fetcher import fetch_page_html
from scraper.parser import parse_listings
from scraper.exporter import export_to_csv

async def scrape_pages(base_url, total_pages):
    all_listings = []
    for i in range(total_pages):
        url = f"{base_url}/page-{i+1}"
        print(f"[INFO] Scraping: {url}")
        page, browser = await fetch_page_html(url, browser_index=i)
        if page:
            listings = await parse_listings(page)
            all_listings.extend(listings)
            await browser.close()
    return all_listings

if __name__ == "__main__":
    try:
        base_url = "https://www.redfin.com/city/30749/NY/New-York"
        results = asyncio.run(scrape_pages(base_url, total_pages=9))
        export_to_csv(results, "data/listings.csv")
    except Exception as e:
        print(f"[FATAL ERROR] {repr(e)}")
