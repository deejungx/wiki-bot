#!/usr/bin/python3
#Scraping wikipedia page with command line input
import sys
import requests
from bs4 import BeautifulSoup
import pyperclip

res = requests.get('https://en.wikipedia.org/wiki/' + ' '.join(sys.argv[1:]))
res.raise_for_status()
wiki = BeautifulSoup(res.text,"lxml")

def readable_strings(elem):
    return elem.getText()

elems = wiki.find_all('p')
string_elems = map(readable_strings, elems)
output = "\n".join(string_elems)
pyperclip.copy(output)
