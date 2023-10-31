import requests
from bs4 import BeautifulSoup
import csv

# Prompt the user to enter the sitemap URL
sitemap_url = input("Enter the sitemap URL: ")

# Fetch the sitemap
sitemap_xml = requests.get(sitemap_url).text

# Parse the sitemap using BeautifulSoup
soup = BeautifulSoup(sitemap_xml, "xml")

# Extract all URLs from the sitemap
urls = []
for loc in soup.find_all("loc"):
    urls.append(loc.text)

# Export URLs to CSV file
with open("urls.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    for url in urls:
        writer.writerow([url])

