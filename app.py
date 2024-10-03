import streamlit as st

# To hide Streamlit's default menu (hamburger menu) and the "Made with Streamlit" footer
st.set_page_config(
    page_title="Digital Resume", 
    page_icon=":briefcase:", 
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None,
    }
)

st.title("DIGITAL RESUME")
#---Page Navigations---

about_page = st.Page(
    page= "views/about_me.py",
    title= "About Me",
    icon= "👦",
    default= True,
) 

education = st.Page(
    page= "views/educations.py",
    title= "Education",
    icon= "👨‍🎓",
)

project = st.Page(
    page= "views/project.py",
    title="Project",
    icon= "⚒️"
)
certificate = st.Page(
    page= "views/certificates.py",
    title= "Certificates",
    icon= "🎖️"
)

#--Navigations--

pg = st.navigation(
   [about_page,education, project, certificate])
   
#--setup the webpage--
#st.logo()

#--run the pg--
pg.run()