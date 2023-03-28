import requests
from bs4 import BeautifulSoup
import time
import threading
from colorama import Fore, init
init(autoreset=True)

url = 'https://vidadesuporte.com.br/page/'

def images_downloader(soup):
    for i in soup.select('img[src*="Suporte_"]'):
        responsedl = requests.get(url)
        temp_name = i['src'].split('/')[-1]
        with open('/home/filipe/Documentos/Python/modulo 3/python3_1/images/' + temp_name, 'wb') as f:
            f.write(responsedl.content)
        print(Fore.GREEN + f'Image: {temp_name} Saved!')
      
if __name__ == '__main__':
    for i in range(1, 20, 1):
        response = requests.get(f'{url}{i}')
        soup = BeautifulSoup(response.content, 'html.parser')
        images_downloader(soup)
    