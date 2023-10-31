# Sitemap URL Extractor 🌐📝

This script allows you to extract URLs from an XML sitemap and save them to a CSV file.

## 🚀 Features

- Fetch XML sitemaps from given URLs
- Extract all URLs listed in the sitemap
- Export the extracted URLs to a CSV file

## 📦 Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`
- `csv`

## 🛠️ Installation

1. Ensure you have Python 3.x installed.
    
2. Install the required libraries using pip:
    
    bashCopy code
    
    `pip install requests beautifulsoup4`
    

## 🚀 Usage

1. Run the script:
    
    bashCopy code
    
    `python extractSitemap.py`
    
2. When prompted, enter the sitemap URL you wish to extract URLs from.
    
3. The script will save the extracted URLs to a file named `urls.csv`.
    

## 📝 Note

Make sure you have the necessary permissions to access the sitemap URL and the website does not block automated requests. If you encounter any issues with specific sitemaps, it might be due to the structure of the XML or access restrictions.