from psaw import PushshiftAPI
from datetime import date
from dateutil.relativedelta import relativedelta

import datetime
import json
import requests
import time

api = PushshiftAPI()

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
def validData(item, listings):
  filtered = []
  for listing in listings:
    title = listing['title']
    try:
      selling = title[title.index("[H]"):title.index("[W]")]
      if item.lower() in selling.lower():
        undesired_items = ['deskmat', 'spacebar', 'coiled', 'cable', 'clone', 'extension']
        selling = selling.lower().split()
        last_word_item = item.split()
        last_word_item = last_word_item[len(last_word_item) - 1].lower()
        if selling.index(last_word_item) + 1 >= len(selling):
          filtered.append(listing)
        else:
          next_word = selling[selling.index(last_word_item) + 1]
          if not any(x in next_word for x in undesired_items):
            filtered.append(listing)
    except ValueError:
      continue
  return filtered


# Extracts user, price, date, item from listing
def extractInfo(listing, item):
  text = listing['selftext']
  section = text.lower().split()

  start = section.index("darling")
  filtered = [word[start] for word in section]
  print(section)
  print(filtered)



def main():
  item = input("Enter specific item to search for on /r/MechMarket: ")
  data = getData(item)
  data = validData(item, data)

  for listing in data:
    extractInfo(listing, item)

if __name__ == "__main__":
  main()