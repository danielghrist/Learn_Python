'''
Helper module for scraping pages, with things like scrolling to bottom of page and initiating a webdriver, as well as creating a list of URLs.
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
# from selenium.webdriver import Keys
from datetime import datetime
import time
import pandas as pd

### -----BEGIN CONSTANTS----- ###
# Constant to use for which console we want to search for:
# CONSOLE = "wii"
# Amount to pause between each scroll action:
SCROLL_PAUSE_TIME = .5
# URL with filtered search for Wii game on price charting site:
# URL = f"https://www.pricecharting.com/console/{CONSOLE}?sort=name&genre-name=&exclude-variants=true&exclude-hardware=true&when=none&release-date=2023-09-07&show-images=true"
### -----END CONSTANTS----- ###


class Scraper:
    def __init__(self, console: str) -> None:
        self.__console = console.lower()
        self.__link = f"https://www.pricecharting.com/console/{self.__console}?sort=name&genre-name=&exclude-variants=true&exclude-hardware=true&when=none&release-date=2023-09-07&show-images=true"
        self.driver = self.__init_webdriver(self.__link)

    def __init_webdriver(self, url: str) -> webdriver:
        '''Set webdriver options for detach in Chrome and initialize and return a Chrome webdriver from the given URL.'''
        # Get Chrome options and set up brower to not auto close:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        # Create webdriver:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url=self.__link)
        return driver

    #
    # Code to scroll to bottom of page using execute to execute JavaScript code:
    def scroll_to_bottom(self) -> None:
        '''Scroll to the bottom of the page to be certain all elements are loaded before scraping.'''
        # Initialize webdriver and options:
        # driver = self.__init_webdriver(self.url)

        # Get current scroll height
        last_height = self.driver.execute_script(
            "return document.body.scrollHeight")

        while True:
            # Scroll to bottom of current visible window:
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")

            # Wait for the page to load:
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script(
                "return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        ### End scrolling to bottom of page ###

    # Return the current console system being scraped by this object:
    def get_console(self) -> str:
        '''Returns the platform being scraped.'''
        return self.__console

    # Return the html of a webpage for BeautifulSoup to use:
    def get_page_source(self) -> str:
        '''Returns the source code of the current webpage pointed to by self.driver.'''
        return self.driver.page_source

    # Get current date as a string in YYYY_MM_DD format:
    def get_string_date(self) -> str:
        '''Returns the current date in YYYY_MM_DD format.'''
        return datetime.today().strftime("%Y-%m-%d")

    # Close the webdriver browser:
    def close_webdriver(self) -> None:
        '''Close the webdriver that was opened when object created to close browser window.'''
        self.driver.quit()

    #
    #
    #
    # game_price_list = []

    # # Obtain all row data in the #games_table on the website:
    # game_data_row = driver.find_elements(
    #     By.CSS_SELECTOR, "#games_table tbody tr")

    # # Loop through each row and extract image, title, loose price, cib_price, and new_price
    # for row in game_data_row:
    #     # Find the URL of the thumbnail view of a game image:
    #     image_src = row.find_element(
    #         By.CSS_SELECTOR, "td div img.photo").get_property("src")
    #     title = row.find_element(By.CSS_SELECTOR, "td.title").text
    #     loose_price = row.find_element(By.CSS_SELECTOR, "td.used_price").text
    #     cib_price = row.find_element(By.CSS_SELECTOR, "td.cib_price").text
    #     new_price = row.find_element(By.CSS_SELECTOR, "td.new_price").text

    #     # Add data as dictionary for each game to game price list:
    #     game_price_list.append({
    #         "image_link": image_src,
    #         "title": title,
    #         "loose_price": loose_price,
    #         "cib_price": cib_price,
    #         "new_price": new_price
    #     })

    #     game_df = pd.DataFrame(game_price_list)
    #     print(game_df)
    #     game_df.to_csv(
    #         f"{self.getStringDate()}-{self.__console.title()}-Price_List.csv")


# nes_scrape = Scraper("nes")
# nes_scrape.scroll_to_bottom()
# html = nes_scrape.get_page_source()
# print(html)
# nes_scrape.close_webdriver()
