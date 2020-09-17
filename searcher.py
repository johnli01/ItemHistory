from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import sys

options = webdriver.ChromeOptions()
options.add_argument("users-data-dri=C:\\Users\\johnl\\AppData\\Local\\"
                     "Google\\Chrome\\User Data")
driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe",
                          chrome_options=options)
driver.get("https://www.bestbuy.com/site/apple-lightning-to-3-5mm-"
           "headphone-adapter-white/5622278.p?skuId=5622278")

# Add Item to Cart
print('ADDING TO CART')
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, "//*[contains(@class, 'btn btn-primary btn-lg btn-block "
        "btn-leading-ficon add-to-cart-button')]")))
    cursor = driver.find_element_by_xpath("//*[contains(@class, "
                                          "'btn btn-primary btn-lg "
                                          "btn-block btn-leading-ficon "
                                          "add-to-cart-button')]")
    cursor.click()
    print('FINISHED ADDING')
except TimeoutException:
    print("Wait Timed Out on 'ADDING TO CART'")
    sys.exit


# Go to Cart
print('GOING TO CART')
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, "//*[contains(@class, 'btn btn-secondary "
        "btn-sm btn-block ')]")))
    cursor = driver.find_element_by_xpath("//*[contains(@class, 'btn "
                                          "btn-secondary btn-sm btn-block ')]")

    cursor.click()
    print('FINISHED GOING TO CART')
except TimeoutException:
    print("Wait Timed Out on 'GOING TO CART'")
    sys.exit

# Checkout Item
print('GOING TO CHECKOUT')
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, "//*[contains(@class, 'btn btn-lg btn-block "
        "btn-primary')]")))
    cursor = driver.find_element_by_xpath("//*[contains(@class, 'btn btn-lg "
                                          "btn-block btn-primary')]")
    cursor.click()
    print('FINISHED GOING TO CHECKOUT')
except TimeoutException:
    print("Wait Timed Out on 'GOING TO CHECKOUT'")
    sys.exit
