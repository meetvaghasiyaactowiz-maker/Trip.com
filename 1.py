from playwright.sync_api import sync_playwright


def parser(response):
    if 'getHotelRoomListOversea' in response.url:
        print(response.url)


with sync_playwright() as p:
    browser = p.chromium.launch(
        channel="chrome",
        headless=False,
        args=[
            '--disable-blink-features=AutomationControlled',
            # "--blink-settings=imagesEnabled=false"
        ],
    ) 
    context = browser.new_context(
        no_viewport = True,
        permissions=[],     
        geolocation=None  
    )
    
    page = context.new_page()
    page.goto("https://in.trip.com/")
    page.wait_for_timeout(300)

    # if page.locator("//i[contains(@class,'close-icon')]"):
    #     page.locator("//i[contains(@class,'close-icon')]").click()

    page.locator("//input[@id='destinationInput']").fill('surat')
    page.keyboard.press("Enter")
    page.wait_for_timeout(1000)

    search_btn = page.locator("button:has-text('Search')")
    search_btn.click()  

    page.locator("a.hotelName").first().click()

    input('wait..')