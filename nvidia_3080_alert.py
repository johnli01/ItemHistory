from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\johnl\\AppData\\Local\\"
                     "Google\\Chrome\\User Data\\Default")
options.add_argument("disable-infobars")

driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe",
                          chrome_options=options)
driver.get("https://www.nvidia.com/en-us/shop/geforce/?page=1&limit=9&locale=en-us&search=RTX%203080")

# Program that checks availability of NVIDIA RTX 3080 FE cards
try:
    refresh_counter = 0
    while True:
        # Checks if RTX card is Out of Stock
        product_name = driver.find_element_by_xpath("//*[contains(text(), 'NVIDIA GEFORCE RTX 3080')]")
        out_of_stock = driver.find_element_by_xpath(
                "//*[contains(@class, 'featured-buy-link link-btn brand-green  cta-button stock-grey-out')]")

        print("======== REFRESH COUNTER: ", refresh_counter, " =========")
        print("PRODUCT NAME: ", product_name.text)
        print("CURRENTLY: ", out_of_stock.text)

        # Refreshes Page every 30 seconds
        time.sleep(30)
        driver.refresh()
        refresh_counter = refresh_counter + 1
except NoSuchElementException:
    # In Stock since it's unable to find the cards being Out of Stock
    print('!!!!!!!!!!!!!!!!!!!!!!!!!! IN STOCK !!!!!!!!!!!!!!!!!!!!!!!!!!')
