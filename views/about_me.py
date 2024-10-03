import streamlit as st

col1, col2 = st.columns([1, 2], gap="small")

with col1:
    st.image("./assets/passportPhoto.jpeg", width=150)

with col2:
    st.title("Haseeb Habeebulla", anchor=False)
    st.write(
        "Geospatial Developer, GeoAI, Agriculture Engineer"
    )
btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 1])

with btn_col1:
        # LinkedIn Button
        st.markdown(
            """
            <a href="https://www.linkedin.com/in/haseeb-habeebulla-1b22b911b/" target="_blank">
                <button style="background-color:blue; color:white; border:none; padding: 10px 24px; cursor:pointer;">
                LinkedIn
                </button>
            </a>
            """, 
            unsafe_allow_html=True
        )

with btn_col2:
        # GitHub Button
        st.markdown(
            """
            <a href="https://github.com/Haseeb-oss-eng/" target="_blank">
                <button style="background-color:#333; color:white; border:none; padding: 10px 24px; cursor:pointer;">
                GitHub
                </button>
            </a>
            """, 
            unsafe_allow_html=True
        )

with btn_col3:
        # Resume Button
        st.markdown(
            """
            <a href='https://drive.google.com/file/d/1hDT-aiykQIHhLTSJpFk4k-x3LK_L24rP/view?usp=drive_link'>
            <button  style="color:white; border:none; padding: 10px 24px; cursor:pointer;">Resume
            </button>
            </a>
            """,
            unsafe_allow_html=True
        )

    

#---content---
st.write("\n")
st.write("\n")
st.write(
    """
    I am seeking an opportunity within a dynamic organization to kickstart my career. With a strong academic background and hands-on experience in both geospatial and AI/ML technologies—including GDAL, GeoPandas, Geemap, TensorFlow, 
    PyTorch, and Scikit-learn—I am equipped with a robust skill set that bridges 
    the worlds of IT and geospatial sciences. Eager to contribute my enthusiasm and 
    collaborate within a team, I am committed to applying and refining my geoinformatics expertise while leveraging cutting-edge technologies to solve complex, real-world challenges in both the IT and geospatial domains.
    """
)




#--------Contact Me--------------

st.write("\n")
st.subheader("Contact Me", anchor=False)
st.write(
    """
**Nationality**:          Indian \n
**Mob**:                  +91-9385926315 \n
    """
)
st.write("**Current Address:**")
st.write(
    """
    \nFlat# 08, Floor# 12A, Revolution One,  
    \nNear Chettinad Hospital, Padur,  
    \nChennai - 603103
    \nTamil Nadu, India
    """
)
st.markdown(
        """
        <a href="mailto:someone@example.com">
            <button style="background-color:red; color:white; border:none; padding: 10px 24px; cursor:pointer;">
            Send Mail
            </button>
        </a>
        """, 
        unsafe_allow_html=True
    )