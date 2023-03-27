import streamlit as st
from utils import project2_desc as p2d


def app():
	st.write('''
		### Chatbot test page
		'''
		)
	p2d.desc()
