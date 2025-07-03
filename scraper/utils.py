import asyncio

async def auto_scroll_page(page, scroll_delay=2000, scroll_times=22):
    for _ in range(scroll_times):
        await page.evaluate("window.scrollBy(0, window.innerHeight);")
        await asyncio.sleep(scroll_delay / 1000)
