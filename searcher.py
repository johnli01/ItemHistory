from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe",
                          chrome_options=options)
driver.get("https://www.reddit.com/r/hardwareswap/search/"
           "?q=founders&source=recent&restrict_sr=1&sort=new")

recent = driver.find_elements_by_xpath("//*[contains(@class, 'y8HYJ-y_lTUHkQIc1mdCq _2INHSNB8V5eaWp4P0rY_mE')]")

key_word = 'Founders'
filtered_list = []
print("FILTERING")
for listing in recent:
    if key_word in listing.text:
        filtered_list.append(listing)

filtered_list = filtered_list[1:]
seen = set()
print("MARKING SEEN")
for listing in filtered_list:
    seen.add(listing)

print("RUNNING WHILE LOOP")
iter = 1
while True:
    print("ITERATION : ", iter)
    recent = driver.find_elements_by_xpath("//*[contains(@class, 'SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE')]")
    unseen = []
    for listing in recent:
        if key_word in listing.text and listing not in seen:
            unseen.append(listing)
            seen.add(listing)

    # for i in range(len(unseen)):
    #     unseen[i].click()

    if len(unseen) > 0:
        unseen[0].click()
    
    time.sleep(3)
    iter = iter + 1

driver.quit()
