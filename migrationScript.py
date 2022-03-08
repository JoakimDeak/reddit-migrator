import praw
import json
import sys

def getSubredditList(fileName):
  fileObject = open(f"{fileName}", "r")
  jsonContent = fileObject.read()
  targets = json.loads(jsonContent)
  cleanedList = []
  for i in range(len(targets)):
    if(targets[i][0:2] == 'r/'):
      cleanedList.append(targets[i][2:len(targets[i])])
  return cleanedList

def getRedditInstance():
  fileObject = open("secrets.json", "r")
  jsonContent = fileObject.read()
  secrets = json.loads(jsonContent)

  CLIENT_ID = secrets['CLIENT_ID']
  CLIENT_SECRET = secrets['CLIENT_SECRET']
  USERNAME = secrets['USERNAME']
  PASSWORD = secrets['PASSWORD']
  USER_AGENT = secrets['USER_AGENT']

  reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT, username=USERNAME, password=PASSWORD)
  return reddit

def subToList(fileName):
  targets = getSubredditList(fileName)
  first = targets.pop()
  reddit = getRedditInstance()
  reddit.subreddit(first).subscribe(targets)
  print(f"Joined {len(targets) + 1} subreddits")

subToList(sys.argv[1])