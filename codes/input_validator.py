import streamlit as st
import numpy as np

def validate_string(input_string):
    if not (input_string.strip() or input_string==""):
        st.error("The text input is empty. Please enter some text.")