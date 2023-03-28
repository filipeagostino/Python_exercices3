import requests
from bs4 import BeautifulSoup
import time
import threading
from colorama import Fore, init
init(autoreset=True)

url = 'https://vidadesuporte.com.br/page/'
l_urls = []

def get_urls(url):
    global l_urls
    count = 1
    while count <= 20:
        response = requests.get(f'{url}{count}')
        soup = BeautifulSoup(response.content, 'html.parser')
        for i in soup.select('img[src*="Suporte_"]'):
            url_text = i['src']
            temp_name = i['src'].split('/')[-1]
            print(Fore.YELLOW + f'Image Name: {temp_name}')
            l_urls.append(url_text)
            print(l_urls)
        count += 1


def images_downloader():
    global l_urls
    for url in l_urls:
        responsedl = requests.get(url)
        temp_name = url.split('/')[-1]
        with open('/home/filipe/Documentos/Python/modulo 3/python3_2/images/' + temp_name, 'wb') as f:
            f.write(responsedl.content)
        print(Fore.GREEN + f'Image: {temp_name} Saved!')


if __name__ == '__main__':
    get_urls(url)
    t_downloader = threading.Thread(target=images_downloader(), name='Downloader')
    t_downloader.start()