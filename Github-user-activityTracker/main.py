from urllib import response
import requests
import json
import argparse


def get_user_activity(username):
    """ fetch and display GitHub user latest activity for a given username"""
    url = f"https://api.github.com/users/<username>/events"
    requests = requests.get(url)
    
    if response.status_code == 200:
            return response.json()
    else:
            print("Error fetching data: {response.status_code}")
            return None

def display_activity(activity_data):
      """"Display the fetched activity data."""
      if not  activity_data:
            print("No activity found.")
            return
      
      for event in activity_data:
            event_type = event['type']
            repo_name = event['repo']['name']
            created_at = event['created_at']
            print(f"{event_type} at {repo_name} on {created_at}")

def main():
    parser = argparse.ArgumentParser(description="Github user activity Tracker")
    subparsers = parser.add_subparsers(dest="command")
    
    get_user = subparsers.add_parser("get", help="Get user acticity")
    get_user.add_argument("user", help="Github username")

    args = parser.parse_args()

    if args.command == "get":
          activity = get_user_activity(args.user)
          display_activity(activity)

if __name__ == "__main__":
      main()



            