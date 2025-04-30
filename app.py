import streamlit as st

home = st.Page("page_files/Home.py", icon='🏠')

try_model = st.Page("page_files/Try_Model.py", icon='📊')

view_model_analysis = st.Page("page_files/View_Model_Analysis.py", icon='🤖')

feedback = st.Page("page_files/Feedback.py", icon='💭')

credits = st.Page("page_files/Credits.py", icon='📇')


pg = st.navigation({
    "Home": [home],
    "Analysis": [try_model, view_model_analysis],
    "Feedback & Credits ": [feedback, credits]
})

pg.run()
