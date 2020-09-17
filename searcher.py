from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe",
                          chrome_options=options)
driver.get("https://www.bestbuy.com/site/apple-lightning-to-3-5mm-"
           "headphone-adapter-white/5622278.p?skuId=5622278")

recent = driver.find_element_by_xpath("//*[contains(@class, "
                                       "'btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button')]")

recent.click()

time.sleep(1)

recent = driver.find_element_by_xpath("//*[contains(@class, "
                                       "'btn btn-secondary btn-sm btn-block ')]")

recent.click()
