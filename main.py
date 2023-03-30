# pip install beautifulsoup4
# pip install requests
import requests
from bs4 import BeautifulSoup as bs

github_profile = "https://github.com/Sh-Alexandr"
req = requests.get(github_profile)
scraper = bs(req.content, "html.parser")
profile_picture = scraper.find("img", {"alt": "Avatar"})["src"]
print(profile_picture)