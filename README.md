# reddit-migrator

## How to use
* Create an app on https://www.reddit.com/prefs/apps
* Create a file called secrets.json with the following properties:
  * CLIENT_ID
  * CLIENT_SECRET
  * USERNAME
  * PASSWORD
  * USER_AGENT
  * NOTE: CLIENT_ID and CLIENT_SECRET are both from your reddit app. USERNAME and PASSWORD is your reddit username and password. USER_AGENT is the string describing your app, create one based on the reddit API guidelines for user agents: https://github.com/reddit-archive/reddit/wiki/API#rules
* Create a JSON file containing a list of the subreddits you want to subscribe to with the format: ["r/redditdev", "r/Python", ...]
* Clone this repo and add your secrets.json and subreddit list file to the same folder as the script.
* Run the script in a terminal with: `python migrationScript.py <JSON file with subredditlist>.json`  
