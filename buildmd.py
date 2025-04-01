import requests
from bs4 import BeautifulSoup
import csv
import re
from duckduckgo_search import DDGS

def search_info(query):
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=1))
        if results:
            return results[0]['body']
        return "Brak opisu."
        
def search_image(query):
    with DDGS() as ddgs:
        results = list(ddgs.images(query, max_results=1))
        if results:
            return results[0]['image']
        return None
        
def save_markdown(title, description, image_url):
    filename = f"_obrazy/{title.replace(' ', '_')}.md"
    
    image_filename = f"assets/images/{title.replace(' ', '_').lower()}.jpg"
    image_data = requests.get(image_url).content
    with open(image_filename, "wb") as img_file:
        img_file.write(image_data)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"---\nlayout: obrazy\ntitle: {title}\nclass: subpage\n---\n")
        # f.write(f"# {title}\n\n")
        f.write(f"![{title}](/assets/images/{title.replace(' ', '_').lower()}.jpg)\n\n")
        f.write(f"{description}\n")

def scrape_van_gogh_paintings(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r"## \[(.*?)\]\(.*?\)"
    matches = re.findall(pattern, content)

    for match in matches:
        painting_title = match.strip()
        
        description = search_info(f"{painting_title} Vincent van Gogh site:pl.wikipedia.org")
        image = search_image(f"{painting_title} Vincent van Gogh")
	
        if image:
            save_markdown(painting_title, description, image)
        else:
            print(f"Nie znaleziono obrazu dla {painting}")

if __name__ == "__main__":
    file_name = "lista.md"
    scrape_van_gogh_paintings(file_name)
