from bs4 import BeautifulSoup
import requests

# url = input('Enter the URL: ')

url = 'https://www.facebook.com/Hacker.masha/posts/pfbid0216C9SxDEQBRKRKShmUGaiAurwPNQZb4M8cWRYhC3UWBVYSBdXahWKknSpuwrtvKPl'

response = requests.get(url)

response = response.text


response = BeautifulSoup(response, 'html.parser')   

response = response.title

text = response.get_text()

print(text)

