''' A program to automate the classic Cookie Clicker game '''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# URL of the Cookie Clicker Classic game we will be automating:
URL = "https://orteil.dashnet.org/experiments/cookie/"

# Timer Constants:
PURCHASE_SECS = 5
END_MINS = 5

# Use this code to keep the Chrome browser open until closed manually:
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=800, 1440")
chrome_options.add_experimental_option("detach", True)

# Create the Selenium webdriver:
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Find Cookie Element to be clicked, does not move:
cookie_element = driver.find_element(By.CSS_SELECTOR, value="#cookie")


# TODO: GET PRICE OF EACH PURCHASABLE ITEM AS INT:
# for item in purchasable_items:
#     price = int(item.text.split("\n")[0].split(
#         "-")[1].strip().replace(",", ""))
#     print(price)


# TODO: THEN NEED TO FIND WHICH ONE COSTS THE MOST AND CLICK ON THAT ELEMENT TO PURCHASE:


# TODO: Get list of purchasable items and click on the last item in the list:
def buy_item():
    purchasable_items = driver.find_elements(
        By.CSS_SELECTOR, "#store div:not(.grayed)")
    if len(purchasable_items) > 0:
        purchasable_items[-1].click()


# Obtain number of cookies I currently have to spend:
def get_my_cookies():
    return driver.find_element(By.ID, value="money").text


# Create everything for main game loop:
# Creat a flag to determine when to break out of while loop
is_game_running = True

# Create timers for purchasing items and ending the program:
purchase_timer = time.time() + PURCHASE_SECS
end_timer = time.time() + (60 * END_MINS)

# Create the game loop:
while is_game_running:

    # Click cookie
    cookie_element.click()

    if time.time() > purchase_timer:
        buy_item()
        purchase_timer = time.time() + PURCHASE_SECS

    # After constant number of minutes END_MINS has ellapsed finish game:
    if time.time() > end_timer:
        # Get the final Cookies Per Second (CpS):
        cps = driver.find_element(By.ID, "cps")
        # Print my CpS to stdout:
        print(cps.text)
        break


# Use this to close the browser and all tabs that the driver has opened:
driver.quit()
