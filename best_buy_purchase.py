from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import sys

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\johnl\\AppData\\Local\\"
                     "Google\\Chrome\\User Data\\Default")
options.add_argument("disable-infobars")
driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe",
                          chrome_options=options)
driver.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?acampID=0&irclickid=Sm8zzUTDvzKYTR51M-XBBXePUkiX0Q1ZzTAMyE0&irgwc=1&loc=Future+PLC.&mpid=221109&ref=198&skuId=6429440")

# Add Item to Cart
print('1) ADDING TO CART')
try:
    # Waits 10 seconds to find 'Add Cart' button before quitting program
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((
        By.XPATH, "//*[contains(@class, 'btn btn-primary btn-lg btn-block "
        "btn-leading-ficon add-to-cart-button')]")))
    cursor = driver.find_element_by_xpath("//*[contains(@class, "
                                          "'btn btn-primary btn-lg "
                                          "btn-block btn-leading-ficon "
                                          "add-to-cart-button')]")
    cursor.click()
    print('   FINISHED ADDING')
except TimeoutException:
    print("Wait Timed Out on 'ADDING TO CART'")
    sys.exit


# Go to Cart
print('2) GOING TO CART')
try:
    # Waits 10 seconds to find 'Go To Cart' button before quitting program
    WebDriverWait(driver, 500).until(EC.presence_of_element_located((
        By.XPATH, "//*[contains(@class, 'btn btn-secondary "
        "btn-sm btn-block ')]")))
    cursor = driver.find_element_by_xpath("//*[contains(@class, 'btn "
                                          "btn-secondary btn-sm btn-block ')]")

    cursor.click()
    print('   FINISHED GOING TO CART')
except TimeoutException:
    print("Wait Timed Out on 'GOING TO CART'")
    sys.exit

# Checkout Item
print('3) GOING TO CHECKOUT')
try:
    # Waits 10 seconds to find 'Go To Checkout' button before quitting program
    WebDriverWait(driver, 500).until(EC.presence_of_element_located((
        By.XPATH, "//*[contains(@class, 'btn btn-lg btn-block "
        "btn-primary')]")))
    cursor = driver.find_element_by_xpath("//*[contains(@class, 'btn btn-lg "
                                          "btn-block btn-primary')]")
    cursor.click()
    print('   FINISHED GOING TO CHECKOUT')
except TimeoutException:
    print("Wait Timed Out on 'GOING TO CHECKOUT'")
    sys.exit

# Inputting Number
print('4) INPUTTING NUMBERS')
# Waits 10 seconds to find a textbox before quitting program
try:
    WebDriverWait(driver, 500).until(EC.presence_of_element_located((
        By.XPATH, "//*[contains(@id, 'credit-card-cvv')]")))
    cursor = driver.find_element_by_xpath("//*[contains(@id,"
                                          "'credit-card-cvv')]")
    cursor.send_keys('')
    print('   FINISHED INPUTTING NUMBERS')
except TimeoutException:
    print("Wait Timed Out on 'INPUTTING VAL")
    sys.exit

# Place Order
print('4) PLACING ORDER')
try:
    WebDriverWait(driver, 500).until(EC.presence_of_element_located((
        By.XPATH, "//*[contains(@class, 'btn btn-lg btn-block btn-primary button__fast-track')]")))
    cursor = driver.find_element_by_xpath("//*[contains(@class, 'btn btn-lg btn-block btn-primary button__fast-track')]")
    cursor.click()
    print('   FINISHED PLACING ORDER')
except TimeoutException:
    print("Wait Timed Out on 'PLACING ORDER")
    sys.exit
