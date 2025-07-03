import asyncio
from playwright.async_api import async_playwright
from .config import BROWSERS, CUSTOM_USER_AGENT
from .utils import auto_scroll_page

async def fetch_page_html(link, browser_index):
    async with async_playwright() as p:
        browser_type = BROWSERS[browser_index % len(BROWSERS)]
        print(f"[INFO] Launching {browser_type}")
        browser = await getattr(p, browser_type).launch(headless=True)
        context = await browser.new_context(user_agent=CUSTOM_USER_AGENT)
        page = await context.new_page()

        try:
            await page.goto(link, wait_until="domcontentloaded", timeout=30000)
        except:
            await asyncio.sleep(3)
            try:
                await page.goto(link, wait_until="domcontentloaded", timeout=30000)
            except Exception as e:
                print(f"[ERROR] Failed to load {link}: {repr(e)}")
                await browser.close()
                return None, None

        await auto_scroll_page(page)
        return page, browser
