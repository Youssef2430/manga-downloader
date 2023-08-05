import os
import requests
import bs4 as bs
import img2pdf
from tqdm import tqdm
import streamlit as st
import shutil
import numpy as np

def download_chapter(link, number, label):
    web = requests.get(link)
    sp = bs.BeautifulSoup(web.text, 'html.parser')
    pages = sp.find_all("img", {"class": "img-responsive"})
    pages.pop()
    images = []
    i = 0
    os.mkdir("chapters/chapter"+str(number))
    for page in pages:
        p = open("chapters/chapter"+str(number)+"/"+str(i)+".png", "wb")
        p.write(requests.get(page['data-src'].strip()).content)
        images.append("chapters/chapter"+str(number)+"/"+str(i)+".png")
        i += 1
        p.close()
    with open("chapters"+"/"+label+number+".pdf", "wb") as f:
        f.write(img2pdf.convert(images))
        shutil.rmtree("chapters/chapter"+str(number))
