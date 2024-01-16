import requests
from getpass import getpass
from pprint import PrettyPrinter


username = input("Enter Your GitHub Username: ")
token = getpass("Enter your GitHub Personal Access Token: ")


url_user = 'https://api.github.com/user'
response_user = requests.get(url_user, headers={'Authorization': f'token {token}'})

pp = PrettyPrinter()
if response_user.status_code == 200:
    user_data = response_user.json()
    pp.pprint(("User data:", user_data))
    fetch_repos = input("Do you want to fetch and print repository names? (yes/no): ").lower()
    if fetch_repos == "yes":
        url_repos = f'https://api.github.com/users/{username}/repos'
        response_repos = requests.get(url_repos, headers={'Authorization': f'token {token}'})
    
        if response_repos.status_code == 200:
            repositories = response_repos.json()
            repo_names = [repo['name'] for repo in repositories]
            pp.pprint(("Repository names:", repo_names))
        else:
            pp.pprint(("Failed to retrieve repositories. Status code:", response_repos.status_code))
else:
    pp.pprint(("Failed to authenticate. Status code:", response_user.status_code))

