import streamlit as st



col1, col2 = st.columns([1,2], gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/passportPhoto.jpeg", width=150)
with col2:
    st.title("Haseeb Habeebulla", anchor= False)
    st.write(
        "Geospatial Developer, GeoAI, Agriculture Engineer"
    )

#---content---
st.write("\n")
st.write(
    """
    Hi, I am Haseeb Habeebulla completed my M.Tech Geoinformatics 2024. I have my
    BE in Agriculture Engineering 2022. I am passionate in Geospatial Technologies, Precision Farming,
    I love to embark and revolution in Agriculture IT.
    """
)




#--------Contact Me--------------

st.write("\n")
st.subheader("Contact Me", anchor=False)
st.write(
    """
    Haseeb Habeebulla \n
    Mob:    +91-9385926315 \n
    mailto: ibnhabeebulla@gmail.com \n
    Github: https://github.com/Haseeb-oss-eng
    """
)