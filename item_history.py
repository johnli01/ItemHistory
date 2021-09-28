from psaw import PushshiftAPI
from datetime import date
from dateutil.relativedelta import relativedelta

import datetime
import json
import requests
import time

api = PushshiftAPI()


def epochToReg(time):
  return int(datetime.datetime.fromtimestamp(time))

def regToEpoch(time):
  return int(datetime.datetime(time.year, time.month, time.day, 0, 0).timestamp())

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


def validData(data):



def main():
  item = input("Enter specific item to search for on /r/MechMarket: ")
  data = getData(item)
  data = validData(data)

if __name__ == "__main__":
  main()