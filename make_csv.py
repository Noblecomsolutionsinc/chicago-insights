import os
import csv
from bs4 import BeautifulSoup

folder = "E:\\chicago-insights"
base_url = "https://chicago-insights.vercel.app/"

rows = []

for file in os.listdir(folder):
    if file.endswith(".html"):
        path = os.path.join(folder, file)
        with open(path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")
            title = soup.title.string.strip() if soup.title else file
            link = base_url + os.path.splitext(file)[0]
            rows.append([title, link])

# Save CSV
with open(os.path.join(folder, "links.csv"), "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["name", "link"])
    writer.writerows(rows)

print("links.csv created with", len(rows), "entries")
