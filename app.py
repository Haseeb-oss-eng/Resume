import streamlit as st

#---Page Navigations---

about_page = st.Page(
    page= "views/about_me.py",
    title= "About Me",
    icon= "👦",
    default= True,
) 

education = st.Page(
    page= "views/education.py",
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
    {
        "Info": [about_page],
        "Details": [education, project, certificate]
    }
)

#--setup the webpage--
#st.logo()

#--run the pg--
pg.run()