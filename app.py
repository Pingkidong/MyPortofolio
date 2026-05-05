import streamlit as st

st.set_page_config(
    page_title="My Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

home = st.Page("pages/home.py", title="Home", icon="🏠", default=True)
car  = st.Page("pages/car_evaluation.py", title="Car Evaluation", icon="🚗")

pg = st.navigation([home, car], position="hidden")
pg.run()