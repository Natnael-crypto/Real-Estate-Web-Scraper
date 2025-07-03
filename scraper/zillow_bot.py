import asyncio
from playwright.async_api import async_playwright
import time
import csv

BROWSERS = ["chromium", "firefox", "webkit"]
CUSTOM_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
)

async def auto_scroll_page(page, scroll_delay=2000, scroll_times=22):
    for i in range(scroll_times):
        await page.evaluate("window.scrollBy(0, window.innerHeight);")
        await asyncio.sleep(scroll_delay / 1000)

async def scrape_zillow(link, max_pages=1):
    listings = []

    for page_num in range(1, max_pages + 1):
        async with async_playwright() as p:
            browser_type = BROWSERS[(page_num - 1) % len(BROWSERS)]
            print(f"[INFO] Launching {browser_type} for page {page_num}")

            browser_launcher = getattr(p, browser_type)
            browser = await browser_launcher.launch(headless=False, slow_mo=500)
            context = await browser.new_context(user_agent=CUSTOM_USER_AGENT)
            page = await context.new_page()

            url = link
            print(f"[INFO] Navigating to: {url}")

            try:
                await page.goto(url, wait_until="domcontentloaded", timeout=30000)
            except Exception as e:
                print(f"[WARN] Retry after failure...")
                await asyncio.sleep(3)
                try:
                    await page.goto(url, wait_until="domcontentloaded", timeout=30000)
                except Exception as e:
                    print(f"[ERROR] Failed to load {url}: {repr(e)}")
                    await browser.close()
                    continue

            await asyncio.sleep(1)
            await auto_scroll_page(page)

            home_cards = await page.query_selector_all('a[data-rf-test-name="basicNode-homeCard"]')
            print(f"[INFO] Found {len(home_cards)} home cards")

            for home in home_cards:
                try:
                    url = await home.get_attribute("href")
                    full_url = f"https://www.redfin.com{url}" if url.startswith("/") else url

                    aria_label = await home.get_attribute("aria-label")
                    address_text = aria_label if aria_label else "N/A"

                    price_el = await home.query_selector(".bp-Homecard__Price--value")
                    price = await price_el.inner_text() if price_el else "N/A"

                    beds_el = await home.query_selector(".bp-Homecard__Stats--beds")
                    beds = await beds_el.inner_text() if beds_el else "N/A"

                    baths_el = await home.query_selector(".bp-Homecard__Stats--baths")
                    baths = await baths_el.inner_text() if baths_el else "N/A"

                    sqft_el = await home.query_selector(".bp-Homecard__Stats--sqft")
                    sqft = await sqft_el.inner_text() if sqft_el else "N/A"

                    fact_items = await home.query_selector_all(".KeyFacts-item")
                    facts = [await item.inner_text() for item in fact_items]

                    agent_el = await home.query_selector(".bp-Homecard__Attribution")
                    agent = await agent_el.inner_text() if agent_el else "N/A"

                    listings.append({
                        "address": address_text,
                        "price": price,
                        "beds": beds,
                        "baths": baths,
                        "sqft": sqft,
                        "lot_hoa_walk": facts,
                        "agent": agent,
                        "url": full_url,
                    })

                    print(f"🏠 {address_text} | 💰 {price} | 🛏 {beds} | 🛁 {baths} | 📐 {sqft}")

                except Exception as e:
                    print(f"[ERROR] Parsing failed: {repr(e)}")
                    continue

            await browser.close()
            print(f"[INFO] Done with {browser_type} for page {page_num}")

    return listings

if __name__ == "__main__":
    try:

        page=10
        all_listing=[]
        for i in range(page):
            target_url = f"https://www.redfin.com/city/30749/NY/New-York/page-{i+1}"
            results = asyncio.run(scrape_zillow(target_url, max_pages=1))
            
            for item in results:
                all_listing.append(item)

        # Write to CSV file
        with open("listing.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=[
                "address", "price", "beds", "baths", "sqft", "lot_hoa_walk", "agent", "url"
            ])
            writer.writeheader()
            for row in all_listing:
                # Join list (lot_hoa_walk) into a semicolon-separated string
                row["lot_hoa_walk"] = "; ".join(row.get("lot_hoa_walk", []))
                writer.writerow(row)

        print("\n[💾 CSV Exported] listing.csv written successfully.")

    except Exception as e:
        print(f"[FATAL ERROR] {repr(e)}")
