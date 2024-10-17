!pip install streamlit_option_menu
import streamlit as st
from streamlit_option_menu import option_menu
import SNA_dash
import Q2_Dash
import Q3_dash

st.set_page_config(layout="wide", page_title="Group 25 Project")

# Custom CSS for styling
st.markdown("""
<style>
    .stApp {
    }
    .custom-header {
        font-size: 3rem;
        color: #ff0000;
        text-align: center;
        padding: 1rem 0;
        background-color: #191938;
        border-radius: 10px;
        margin-bottom: 1rem;
        font-weight: bold;
    }
    .stButton>button {
        background-color: #3498db;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Centered header
st.markdown("<div class='custom-header'>Group 25 Project</div>", unsafe_allow_html=True)

# Horizontal navigation
selected = option_menu(
    menu_title=None,
    options=["Social Network Analysis", "Consumer Insights", "Energy Projections"],
    icons=["graph-up", "people-fill", "lightning-charge-fill"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#ff9b9b"},
        "icon": {"color": "#00000", "font-size": "20px"}, 
        "nav-link": {"font-size": "16px", "text-align": "center", "margin":"0px", "--hover-color": "#ff5050"},
        "nav-link-selected": {"background-color": "#f40000", "color": "#000000"},
    }
)

# Display the selected page
if selected == "Social Network Analysis":
    SNA_dash.show()
elif selected == "Consumer Insights":
    Q2_Dash.show()
elif selected == "Energy Projections":
    Q3_dash.show()