# web scraping
import asyncio
from encodings.punycode import T
from playwright.async_api import async_playwright, Page, Browser, BrowserContext


class ContextManager:
    def __init__(self, browser : Browser, max_contexts: int = 5):
        self.semephore = asyncio.BoundedSemaphore(max_contexts)
        self.browser = browser

    async def __aenter__(self) -> BrowserContext:
        await self.semephore.acquire()
        self.context = await self.browser.new_context()
        return self.context

    async def __aexit__(self, exc_type, exc, tb):
        if isinstance(self.context, BrowserContext):
            await self.context.close()
        self.semephore.release()


async def main():
    async with async_playwright() as ap:
        browser = await ap.chromium.launch(headless=True)
        async with ContextManager(browser) as context:
            page = await context.new_page()
            await page.goto("https://playwright.dev/")
            html_content = await page.content()
            print(html_content)
        await browser.close()

asyncio.run(main())



async def main2():
    async with async_playwright() as ap:
        browser = await ap.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://playwright.dev/")
        html_content = await page.content()
        print(html_content)
        await browser.close()

asyncio.run(main2())
