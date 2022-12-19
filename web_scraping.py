import requests
from bs4 import BeautifulSoup

url = 'https://www.weddingwire.com/wedding-photos/'


page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')


galleries = soup.find_all(class_='GalleryCard-titleLink')

filtered_galleries = []
for gallery in galleries:
    if 'beach' in gallery.text.lower():
        filtered_galleries.append(gallery)


for gallery in filtered_galleries:
    print(gallery.text)
    print(gallery['href'])