from playwright.sync_api import sync_playwright
import json


def parser(response):
    if "getHotelRoomListOversea" in response.url:

        print("\n================ API FOUND ================\n")

        print(f"URL    : {response.url}")
        print(f"STATUS : {response.status}")

        data = response.json()
        if data:
            with open('data.json','w',encoding='utf-8') as f:
                json.dump(data,f, indent=4,default=str)
            return


city = "Surat"
city_id = 60194
country_id = 107

check_in = "2026-06-20"
check_out = "2026-07-04"

adults = 2
rooms = 1



hotel_list_url = (
    f"https://in.trip.com/hotels/list"
    f"?locale=en-IN"
    f"&lat=-1"
    f"&lon=-1"
    f"&coordType=GOOGLE"
    f"&optionName={city}"
    f"&cityId={city_id}"
    f"&checkIn={check_in}"
    f"&checkOut={check_out}"
    f"&adult={adults}"
    f"&crn={rooms}"
    f"&optionid={city_id}"
    f"&optiontype=IntlCity"
    f"&countryId={country_id}"
)

print("\nHOTEL LIST URL:\n")
print(hotel_list_url)

with sync_playwright() as p:

    browser = p.chromium.launch(
        channel="chrome",
        headless=False,
        args=[
            "--disable-blink-features=AutomationControlled",
            "--blink-settings=imagesEnabled=false"
        ]
    )

    context = browser.new_context(
        no_viewport=True
    )

    # Attach API listener
    context.on("response", parser)

    page = context.new_page()

    page.goto(
        hotel_list_url
    )

    page.locator("a.hotelName").first.click()
    print("\nHotel listing loaded successfully\n")

    
    page.wait_for_timeout(8000)


    browser.close()