import time
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ProcessPoolExecutor, as_completed
URLs = ["https://www.google.com/", "https://www.youtube.com/" ] 

def parse(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    return soup.find_all('a')
  
with ProcessPoolExecutor(max_workers=4) as executor:
    start = time.time()
    futures = [ executor.submit(parse, url) for url in URLs ]
    results = []
    for result in as_completed(futures):
        results.append(result)
    end = time.time()
    print("Time Taken: {f}".format(end-start))
