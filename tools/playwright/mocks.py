from playwright.async_api import Page, Route


def mock_static_resources(page: Page):
    page.route("**/*.{ico,png,jpg,svg,webp,mp3,mp4,woff,woof2}", lambda route: route.abort())