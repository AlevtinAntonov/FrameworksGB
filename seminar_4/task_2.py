import requests
from multiprocessing import Process
import time

urls = urls = ['https://www.google.ru/',
               'https://gb.ru/',
               'https://ya.ru/',
               'https://www.python.org/',
               'https://habr.com/ru/all/',
               'https://dzen.ru/',
               'https://gb.ru/',
               'https://rambler.ru/',
               'https://gq.ru/',
               'https://vc.ru/',
               ]


def download(url):
    response = requests.get(url)
    filename = 'multiprocessing_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'

    with open('download/' + filename, "w", encoding='utf-8') as f:
        f.write(response.text)

    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


processes = []
start_time = time.time()

if __name__ == "__main__":
    for url in urls:
        process = Process(target=download, args=(url, ))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()