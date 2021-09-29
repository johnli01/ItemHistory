from psaw import PushshiftAPI
from datetime import date
from dateutil.relativedelta import relativedelta

import datetime
import json
import requests
import time

api = PushshiftAPI()
transaction_counter = 0

# Converts Epoch time To Standard format
def epochToReg(time):
  return int(datetime.datetime.fromtimestamp(time))

# Converts Standard format to Epoch time
def regToEpoch(time):
  return int(datetime.datetime(time.year, time.month, time.day, 0, 0).timestamp())


# Retrieve item data from subreddit within specified timeframe,
# if timeframe not specified, defaults to 3 months in the past from now
def getData(item, start=regToEpoch(date.today()), end=regToEpoch(date.today()+relativedelta(months=-3))):
  url = 'https://api.pushshift.io/reddit/search/submission/?before='+str(start)+"&after="+str(end)+"&subreddit=mechmarket"+"&q="+str(item)
  print(url)
  r = requests.get(url)
  while (str(r) != "<Response [200]>"):
    print("resetting requests")
    time.sleep(60)
    r = requests.get(url)
  data = json.loads(r.text)
  return data['data']


# Filters out buyers of specified item and saves seller listings
def validData(listings):
  filtered = []
  for listing in listings:
    title = listing['title']
    try:
      if title[title.index("[H]"):title.index("[W]")]:
        filtered.append(listing)
    except ValueError:
      continue
  return filtered


def getInfo(listing):
  text = listing['selftext']


def main():
  item = input("Enter specific item to search for on /r/MechMarket: ")
  data = getData(item)
  data = validData(data)
  for listing in data:
    print(listing)

if __name__ == "__main__":
  main()