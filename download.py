import requests
from bs4 import BeautifulSoup
import os
from googletrans import Translator

# Initialize Google Translate API
translator = Translator()

# Loop through all links and download images
#193 = Karina Upgrade
link = f"https://m.cafe.daum.net/GuardianTales/ARz7/194"

# Get HTML content of link
response = requests.get(link)
html_content = response.text

# Parse HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Get title of link and translate to English
title_korean = soup.find('h3', {'class': 'tit_subject'}).text.strip()
title_english = translator.translate(title_korean, dest='en').text
# print(f"{title_english}")
# Find all images with class "txc-image"

# Specify the path of the folder where you want to save the image
folder_name = 'images'
os.makedirs(folder_name, exist_ok=True)

# ...

# Find all images with class "txc-image"
image_link = soup.find_all('img', {'class': 'txc-image'})[0]['src']
image_response = requests.get(image_link)
with open(os.path.join(folder_name, f'{title_english}.png'), 'wb') as f:
    f.write(image_response.content)

