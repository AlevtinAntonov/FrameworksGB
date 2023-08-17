import time

import requests
import threading

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        'https://dzen.ru/',
        'https://gb.ru/',
        'https://rambler.ru/',
        'https://vc.ru/',
        'https://mail.ru/',
        ]


def download(url):
    response = requests.get(url)
    filename = 'threading_' + url.replace('https://',
                                          '').replace('.', '_').replace('/', '') + '.html'
    with open('download/' + filename, "w", encoding='utf-8') as f:
        f.write(response.text)
        print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


threads = []

start_time = time.time()
for url in urls:
    thread = threading.Thread(target=download, args=[url])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
