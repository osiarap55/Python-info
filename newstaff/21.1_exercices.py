# Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). 

import requests 
from bs4 import BeautifulSoup
import json

url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, "html.parser")

# finding the president table
presidents_table = soup.find("table", {"class": "wikitable"})

# empty list to store the data
presidents_data = []

# extracting data

for row in presidents_table.find_all("tr")[1:]: # skippping the header row
    columns = row.find_all(["th", "td"])
    president_info = {
        "number": columns[0].text.encode("utf-8").decode("utf-8").strip(),
        "president": columns[2].text.encode("utf-8").decode("utf-8").strip(),
        "term": columns[3].text.encode("utf-8").decode("utf-8").strip(),
        "party": columns[5].text.encode("utf-8").decode("utf-8").strip(),
        "vice-presindent": columns[7].text.encode("utf-8").decode("utf-8").strip(),
    }
    presidents_data.append(president_info)

# saving the data as json
with open("presidents_data.json", "w") as json_file:
    json.dump(presidents_data, json_file, indent=2)

print("data saved as presidents_data.json")
