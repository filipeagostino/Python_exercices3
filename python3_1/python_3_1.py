import requests
from bs4 import BeautifulSoup
import time
import threading
from colorama import Fore, init
init(autoreset=True)

url = 'https://vidadesuporte.com.br/page/'

def images_downloader(url):
    for i in range(20):
        response = requests.get(f'{url}{i}')
        soup = BeautifulSoup(response.content, 'html.parser')
        for link in soup.find_all({'img': 'src'}):
            url_text = link.get('src')
            temp_name = url_text.split('/')[-1]
            print(Fore.YELLOW + f'Image Name: {temp_name}')
            if 'Suporte_' in temp_name:
                responsedl = requests.get(url_text)
                with open('images/' + temp_name, 'wb') as f:
                    f.write(responsedl.content)
                print(Fore.GREEN + f'Image: {temp_name} Saved!')

begin = time.time()
t_downloader = threading.Thread(target=images_downloader(url), name='Downloader')
t_downloader.start()
t_downloader.join()
end = time.time()
print(f'Execution: {end - begin}')