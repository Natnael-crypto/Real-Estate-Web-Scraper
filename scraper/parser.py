async def parse_listings(page):
    listings = []
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

        except Exception as e:
            print(f"[ERROR] Failed to parse listing: {repr(e)}")
            continue

    return listings
