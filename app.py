import streamlit as st

 
from multipage import MultiPage
from pages import about, howtouse, analysis, socialAnalysis, main, portfolio # import your pages here

# Create an instance of the app 
app = MultiPage()


st.set_page_config(layout="wide")
st.title("Cryptocurrency Analysis And Management")

# Add all your application here
app.add_page("Home", main.app)
app.add_page("Analysis",analysis.app)
app.add_page("Social Analysis", socialAnalysis.app)
app.add_page("Portfolio Manager",portfolio.app)
# app.add_page("How To Use", howtouse.app)
app.add_page("About Us", about.app)

app.run()