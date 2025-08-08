import os
import csv
from bs4 import BeautifulSoup

# Your GitHub Pages base URL
base_url = "https://noblecomsolutionsinc.github.io/chicago-insights/"

# Folder containing the HTML files
folder_path = r"E:\chicago-insights"

# Output CSV file
output_csv = os.path.join(folder_path, "links.csv")

rows = []

for filename in os.listdir(folder_path):
    if filename.lower().endswith(".html"):
        file_path = os.path.join(folder_path, filename)

        # Try to extract <title> from the HTML
        with open(file_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")
            title_tag = soup.find("title")
            title_text = title_tag.text.strip() if title_tag else filename

        # Build the full HTTPS link
        file_link = base_url + filename

        # Append to rows
        rows.append([title_text, file_link])

# Write to CSV
with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Link"])
    writer.writerows(rows)

print(f"✅ CSV created successfully at: {output_csv}")
