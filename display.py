import os
import requests
import bs4 as bs
import img2pdf
from tqdm import tqdm
import streamlit as st
import shutil
import numpy as np
from paginator import paginator
from downloader import download_chapter

def display(label, mangas, dates):
    st.header(label)
    bottom_colms = st.columns((4, 2, 2))
    colms = st.columns((1, 2, 2, 1))
    pagination = bottom_colms[2]
    fields = ["№", 'Title', 'Date','Download']

    for col, field_name in zip(colms, fields):
        # header
        col.write(field_name)
    
    for x, manga in paginator("", mangas, pagination, 15):
        col1, col2, col3, col4= st.columns((1, 2, 2, 1))
        number = manga.find_all("a")
        link = number[0]['href']
        n = number[0].text.split(" ")[-1]
        col1.write(n)  # index
        title = manga.find_all("em")
        col2.write(title[0].text)  # title
        col3.write(dates[x].text) #
        button_type = "Generate"
        button_phold = col4.empty()  # create a placeholder
        do_action = button_phold.button(button_type, key=x)
        if do_action:
                download_chapter(link, n, label)
                with open("chapters"+"/"+label+n+".pdf", "rb") as file:
                    col4.download_button(
                        label = "Download",
                        data = file,
                        file_name = "chapter"+n+".pdf",
                    )
                    if col4.download_button:
                        os.remove("chapters"+"/"+label+n+".pdf")

                pass
