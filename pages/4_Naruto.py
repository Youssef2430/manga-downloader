import os
import requests
import os
import requests
import bs4 as bs
import streamlit as st
from display import display


st.session_state.response = requests.get("https://www.scan-vf.net/naruto")
st.session_state.soup = bs.BeautifulSoup(st.session_state.response.text, 'html.parser')

st.session_state.mangas = st.session_state.soup.find_all("h5", {"class": "chapter-title-rtl"})
st.session_state.dates = st.session_state.soup.find_all("div", {"class": "date-chapter-title-rtl"})

def main():
    if "mangas" not in st.session_state:
        st.session_state.mangas = None
    if "dates" not in st.session_state:
        st.session_state.dates = None
    display("Naruto", st.session_state.mangas, st.session_state.dates)

if __name__ == '__main__':
    main()

