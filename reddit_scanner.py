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
driver.get("https://www.reddit.com/r/mechmarket/search?q=Zealios%20v2&restrict_sr=1&sort=new")

recent_listings = driver.find_elements_by_class_name("_eYtD2XCVieq6emjKBH3m")
filtered_listing = []
for listing in recent_listings:
  if "zealios" in listing.text or "Zealios" in listing.text:
    filtered_listing.append(listing)

print(filtered_listing)

for listing in filtered_listing:
  print("FILTERED: ", listing.text)
sys.exit