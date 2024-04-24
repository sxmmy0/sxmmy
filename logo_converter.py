import requests
from bs4 import BeautifulSoup
import os

website_url = "https://www.datacenterdynamics.com/en/dcd-connect-live/connect-madrid-en/2024/ourpartners/" 

def convert_logos_to_links(website_url):
    base_url = "https://storage.googleapis.com/connect-live-app/logos/"
    
    response = requests.get(website_url, headers={"User-Agent": "Image scraping tool"})
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")
    logo_images = soup.find_all("a", class_="sf-partner__logo")

    for image_link in logo_images:
        image = image_link.find('img')  # Find the 'img' tag within the link
        image_src = image.get('src')  
        if image_src:
            logo_link = os.path.join(base_url, os.path.basename(image_src))
            print(logo_link)

convert_logos_to_links("https://www.datacenterdynamics.com/en/dcd-connect-live/connect-madrid-en/2024/ourpartners/") 


