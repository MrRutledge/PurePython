from collections import Counter
from http import HTTPStatus
from typing import List, Tuple


from bs4 import BeautifulSoup

import requests
_HEADERS = {"User-Agent":"Word Counter"}



def process_page_and_get_top_word(url:str) -> Tuple[str,int]:
    html = download_webpage(url)
    text = extract_text(html)
    top_word = find_top_word(text)
    return top_word


def download_webpage(url):
    r = requests.get(url, headers = _HEADERS)
    if r.status_code == HTTPStatus.OK:
        return r.text


def extract_text(hmtl_to_process:str)->List[str]:

    """Assume all text we care about is between <p> tags"""
    soup = BeautifulSoup(hmtl_to_process, "html.parser")
    text_segments = []

    #pull out all paragraphs from html

    all_paragraphs = soup.find_all('p')
    paragraph_text = [p.get_text().split() for p in all_paragraphs]



    # flatten lists of lists
    words = [word for segment in text_segments for word in segment] 
    return words


def find_top_word(words: List[str])-> Tuple[str, int]:
    """Return top word and number of occurrences"""
    word_counter = Counter(words)
    return word_counter.most_common(1)[0]



